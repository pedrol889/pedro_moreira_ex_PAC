"""
Servidor principal do chat multiutilizador com deteção de dados pessoais.
"""

import sys
import os

# Permite correr diretamente com: python server\chat_server.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import socket
import threading
from typing import Dict, Tuple, Optional

from common.config import HOST, PORT, BUFFER_SIZE, ENCODING
from common.protocol import encode_message, decode_message
from common.detector import detect_personal_data, should_block_message, format_findings
from server.logger_setup import setup_server_logger, setup_gdpr_logger


class ChatServer:
    def __init__(self, host: str = HOST, port: int = PORT) -> None:
        self.host = host
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # socket_cliente -> (username, (ip, porta))
        self.clients: Dict[socket.socket, Tuple[str, Tuple[str, int]]] = {}

        self.lock = threading.Lock()
        self.logger = setup_server_logger()
        self.gdpr_logger = setup_gdpr_logger()

    def start(self) -> None:
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()

        self.logger.info(f"Servidor iniciado em {self.host}:{self.port}")
        print(f"[SERVIDOR] À escuta em {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()

            client_thread = threading.Thread(
                target=self.handle_client,
                args=(client_socket, client_address),
                daemon=True
            )
            client_thread.start()

    def handle_client(self, client_socket: socket.socket, client_address: Tuple[str, int]) -> None:
        username = "Desconhecido"

        try:
            raw_data = client_socket.recv(BUFFER_SIZE).decode(ENCODING).strip()
            hello_message = decode_message(raw_data)

            if hello_message.get("type") != "join":
                client_socket.close()
                return

            username = hello_message.get("username", "Anónimo")

            with self.lock:
                self.clients[client_socket] = (username, client_address)

            self.logger.info(f"Cliente ligado: {username} ({client_address[0]}:{client_address[1]})")
            print(f"[LIGAÇÃO] {username} entrou no chat.")

            self.broadcast_system_message(f"{username} entrou no chat.", exclude_socket=client_socket)

            buffer = ""

            while True:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break

                buffer += data.decode(ENCODING)

                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)

                    if not line.strip():
                        continue

                    payload = decode_message(line)

                    if payload.get("type") == "chat":
                        message = payload.get("message", "").strip()

                        if message.lower() == "exit":
                            raise ConnectionResetError("Cliente pediu saída.")

                        self.process_chat_message(client_socket, username, message)

        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            pass
        except Exception as error:
            self.logger.error(f"Erro com o cliente {username}: {error}")
        finally:
            self.remove_client(client_socket)

    def process_chat_message(self, client_socket: socket.socket, username: str, message: str) -> None:
        findings = detect_personal_data(message)

        if should_block_message(findings):
            details = format_findings(findings)

            self.logger.warning(
                f"Mensagem bloqueada de {username}: {message} | Dados detetados: {details}"
            )
            self.gdpr_logger.warning(
                f"Utilizador={username} | Mensagem={message} | Dados={details}"
            )

            warning_payload = {
                "type": "warning",
                "message": "A tua mensagem foi bloqueada por conter possíveis dados pessoais.",
                "details": details,
            }
            client_socket.sendall(encode_message(warning_payload))
            return

        self.logger.info(f"Mensagem aceite de {username}: {message}")

        chat_payload = {
            "type": "chat",
            "username": username,
            "message": message,
        }
        self.broadcast(chat_payload)

    def broadcast(self, payload: dict, exclude_socket: Optional[socket.socket] = None) -> None:
        with self.lock:
            disconnected_clients = []

            for client_socket in list(self.clients.keys()):
                if exclude_socket is not None and client_socket == exclude_socket:
                    continue

                try:
                    client_socket.sendall(encode_message(payload))
                except Exception:
                    disconnected_clients.append(client_socket)

        for dead_socket in disconnected_clients:
            self.remove_client(dead_socket)

    def broadcast_system_message(self, message: str, exclude_socket: Optional[socket.socket] = None) -> None:
        payload = {
            "type": "system",
            "message": message
        }
        self.broadcast(payload, exclude_socket=exclude_socket)

    def remove_client(self, client_socket: socket.socket) -> None:
        with self.lock:
            client_data = self.clients.pop(client_socket, None)

        if client_data:
            username, address = client_data
            self.logger.info(f"Cliente desligado: {username} ({address[0]}:{address[1]})")
            print(f"[SAÍDA] {username} saiu do chat.")
            self.broadcast_system_message(f"{username} saiu do chat.", exclude_socket=client_socket)

        try:
            client_socket.close()
        except Exception:
            pass


if __name__ == "__main__":
    server = ChatServer()
    server.start()
