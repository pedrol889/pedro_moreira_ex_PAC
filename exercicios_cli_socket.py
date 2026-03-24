import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
porta = 12340

clientSocket.connect((host, porta))
print("Ligado ao servidor!")

while True:
    mensagem = input("Escreve uma mensagem (ou 'sair'): ")

    clientSocket.send(mensagem.encode())

    if mensagem.lower() == "sair":
        print("A terminar conexão...")
        break

    resposta = clientSocket.recv(1024).decode()
    print("Servidor:", resposta)

clientSocket.close()
print("Conexão fechada.")