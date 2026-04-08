import socket
import re
from datetime import datetime

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
porta = 12340

serverSocket.bind((host, porta))
serverSocket.listen(1)

print(f"Servidor ligado em {host}:{porta}")
print("A aguardar conexão de cliente...")

clientSocket, enderecoCliente = serverSocket.accept()
print(f"Conexão estabelecida com {enderecoCliente}")

while True:
    try:
        mensagem = clientSocket.recv(1024)

        if not mensagem:
            print("Cliente desconectou.")
            break

        mensagem = mensagem.decode().strip()

        if mensagem.lower() == "sair":
            print("Cliente terminou a conexão.")
            break

        print("Mensagem recebida:", mensagem)

        dados_guardar = []

        # Data e hora atual
        agora = datetime.now()
        data_hora = agora.strftime("%d/%m/%Y %H:%M:%S")

        # TELEFONE
        telefones = re.findall(r"\b\d{9}\b", mensagem)
        for telefone in telefones:
            dados_guardar.append(f"Telefone: {telefone}")

        # EMAIL
        emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", mensagem)
        for email in emails:
            dados_guardar.append(f"Email: {email}")

        # MORADA
        morada = None

        padrao_morada1 = re.search(r"(?:morada\s*[:=-]?\s*)(.+)", mensagem, re.IGNORECASE)
        padrao_morada2 = re.search(r"(?:a\s+minha\s+morada\s+é\s+)(.+)", mensagem, re.IGNORECASE)
        padrao_morada3 = re.search(r"(?:moro\s+em\s+)(.+)", mensagem, re.IGNORECASE)
        padrao_morada4 = re.search(
            r"\b(Rua|Avenida|Av\.?|Travessa|Praça|Largo|Alameda|Estrada|Beco|Rotunda)\s+.+",
            mensagem,
            re.IGNORECASE
        )

        if padrao_morada1:
            morada = padrao_morada1.group(1).strip()
        elif padrao_morada2:
            morada = padrao_morada2.group(1).strip()
        elif padrao_morada3:
            morada = padrao_morada3.group(1).strip()
        elif padrao_morada4:
            morada = padrao_morada4.group(0).strip()

        if morada:
            dados_guardar.append(f"Morada: {morada}")

        # PASSWORD
        password = None

        padrao_pass1 = re.search(r"(?:password|pass|senha)\s*[:=]\s*(.+)", mensagem, re.IGNORECASE)
        padrao_pass2 = re.search(r"(?:a\s+minha\s+(?:password|pass|senha)\s+é\s+)(.+)", mensagem, re.IGNORECASE)
        padrao_pass3 = re.search(r"(?:password|pass|senha)\s+(.+)", mensagem, re.IGNORECASE)

        if padrao_pass1:
            password = padrao_pass1.group(1).strip()
        elif padrao_pass2:
            password = padrao_pass2.group(1).strip()
        elif padrao_pass3:
            password = padrao_pass3.group(1).strip()

        if password:
            dados_guardar.append(f"Password: {password}")

        # Guardar tudo organizado por mensagem
        if dados_guardar:
            with open("dados.txt", "a", encoding="utf-8") as ficheiro:
                ficheiro.write(f"Data e hora: {data_hora}\n")
                ficheiro.write(f"Mensagem original: {mensagem}\n")
                for dado in dados_guardar:
                    ficheiro.write(dado + "\n")
                ficheiro.write("--------------------------------------------------\n")

            print("Dados guardados no ficheiro dados.txt")

        resposta = "Recebi: " + mensagem
        clientSocket.send(resposta.encode())

    except:
        print("Erro na conexão.")
        break

clientSocket.close()
serverSocket.close()

print("Servidor encerrado.")