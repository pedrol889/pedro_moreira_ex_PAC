"""
Cliente CLI para o sistema de chat.
"""

import sys
import os

# Permite correr diretamente com: python client\chat_client.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import socket
import threading

from common.config import HOST, PORT, BUFFER_SIZE, ENCODING
from common.protocol import encode_message, decode_message


class ChatClient:
    def __init__(self, username: str, host: str = HOST, port: int = PORT) -> None:
        self.username = username
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True

    def connect(self) -> None:
        self.client_socket.connect((self.host, self.port))

        join_payload = {
            "type": "join",
            "username": self.username
        }
        self.client_socket.sendall(encode_message(join_payload))
        print(f"[CLIENTE] Ligado ao servidor em {self.host}:{self.port}")

    def receive_messages(self) -> None:
        buffer = ""

        while self.running:
            try:
                data = self.client_socket.recv(BUFFER_SIZE)
                if not data:
                    print("\n[INFO] Ligação ao servidor terminada.")
                    self.running = False
                    break

                buffer += data.decode(ENCODING)

                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)

                    if not line.strip():
                        continue

                    payload = decode_message(line)
                    self.handle_server_payload(payload)

            except Exception:
                if self.running:
                    print("\n[ERRO] Falha ao receber mensagens do servidor.")
                self.running = False
                break

    def handle_server_payload(self, payload: dict) -> None:
        msg_type = payload.get("type")

        if msg_type == "chat":
            username = payload.get("username", "Desconhecido")
            message = payload.get("message", "")
            print(f"\n[{username}] {message}")
        elif msg_type == "system":
            print(f"\n[SISTEMA] {payload.get('message', '')}")
        elif msg_type == "warning":
            print("\n[ALERTA GDPR] A mensagem foi bloqueada.")
            print(f"[DETALHES] {payload.get('details', '')}")
        else:
            print(f"\n[DESCONHECIDO] {payload}")

    def send_messages(self) -> None:
        while self.running:
            try:
                message = input("> ").strip()

                if not message:
                    continue

                payload = {
                    "type": "chat",
                    "message": message
                }
                self.client_socket.sendall(encode_message(payload))

                if message.lower() == "exit":
                    self.running = False
                    break

            except (KeyboardInterrupt, EOFError):
                print("\n[INFO] A terminar cliente...")
                self.running = False
                break
            except Exception:
                print("\n[ERRO] Não foi possível enviar a mensagem.")
                self.running = False
                break

        self.close()

    def close(self) -> None:
        try:
            self.client_socket.close()
        except Exception:
            pass

    def run(self) -> None:
        self.connect()

        receiver_thread = threading.Thread(target=self.receive_messages, daemon=True)
        receiver_thread.start()

        print("Escreve mensagens e prime Enter para enviar.")
        print('Escreve "exit" para sair do chat.')
        self.send_messages()


if __name__ == "__main__":
    username = input("Nome de utilizador: ").strip()
    if not username:
        username = "Anónimo"

    client = ChatClient(username=username)
    client.run()
