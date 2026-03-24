import os as osvar
filename = "pedro_moreira_ex_PAC/pessoas.txt"
nomes = []
morada = []
texto= "ola"
if osvar.path.exists(filename): 
 with open(filename, "r", encoding="utf-8") as manipfile:
    texto = manipfile.read()
while True:
    print("1 - Escreve")
    print("2 - Lista")
    print("3 - Salva")
    print("4 - Sair")
    opc = input("Escolhe uma opção: ")
    match opc:
        case "1":
            nomes.append(input("Escreve o nome: "))
            morada.append(input("Escreve a morada: "))
        case "2":
            for nome in nomes:
                print(nome)
            for morada in morada:
                print(morada)
        case "3":
            print("Salvo")
            with open(filename, "w", encoding="utf-8") as manipfile:
                manipfile.write(texto)
        case "4":
            print("Sair")
            with open(filename, "w", encoding="utf-8") as manipfile:
                manipfile.write(texto)
            break
        case _:
            print("Opção inválida.")