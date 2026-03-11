#exercicio 1
def ParesImp():
 pares = []
 impares = []
 for i in range(1,61):
  if i % 2 == 0:
   pares.append(i)
  else:
   impares.append(i) 
 return pares , impares
pares,impares = ParesImp()

print("Pares:",pares)
print("Impares:",impares)

#exercicio 2
def lernum():
 par = 0
 impar = 0
 for i in range(1,11):
  num = int(input("\nDigite 10 numeros: "))
  if num % 2 == 0:
   par += 1
  else:
   impar += 1
 return par,impar

par,impar = lernum()
print("Pares:",par)
print("Impares:",impar)

#exercicio 3
def media():
 media = 0
 soma = 0
 for i in range(1,11):
  num = float(input("\nDigite 10 numeros: "))
  soma += num 
  media = soma / 10
 return media
media = media()
print("Media:",media) 

#exercicio 4
def primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
n = int(input("\nDigite um número para ver se é primo: "))
if primo(n):
    print("O número é primo")
else:
    print("O número não é primo")

#exercicio 5
def first():
  print("\n")
  for i in range(1,1001):
    print(i)
first()

#exercicio 6
def primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def mostrar_primos():
    count = 0
    num = 2
    while count < 10:
        if primo(num):
            print(num)
            count += 1
        num += 1
mostrar_primos()

#exercicio 7
def dez():
   print("\n")
   for i in range (10 ,1001, 10):
      print(i)
dez()

#exercicio 8
def dezQuin():
   print("\nComeça no 10")
   for i in range (10,1001, 10):
      print(i)
   print("\nComeça no 15")
   for j in range (15,1001 ,10):
      print(j)
dezQuin()

#exercicio 9
def u():
 num = int(input("\nDigite um num entre 1 a 100: "))
 while num < 1 or num > 100:
    print("Numero Invalido")
    num = int(input("\nDigite novamente: "))
 print("Numero valido")
u()

#exercicio 10
def contar_divisores(num):
    divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
    return divisores
n = int(input("\nDigite um número: "))
resultado = contar_divisores(n)
print("O número tem", resultado, "divisores.")

#exercicio 11
def padrao():
    print("\n")
    for i in range(1, 6):
        print(str(i) * i)
padrao()

#exercicio 12
def operacoes():
    num = int(input("\nDigite um número: "))
    cont = 0
    for i in range(1, num):
        print(num, "+", i, "=", num + i)
        cont += 1
        print(num, "-", i, "=", num - i)
        cont += 1
        print(num, "*", i, "=", num * i)
        cont += 1
        print(num, "/", i, "=", num / i)
        cont += 1
    print("\nTotal de operações:", cont)
operacoes()

#exercicio 13
def tabuada():
    num = int(input("\nDigite um número: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
tabuada()

#exercicio 14
def t_tabuadas():
    for num in range(1, 101):
        print(f"\nTabuada do {num}")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
t_tabuadas()

#exercicio 15
def tabela_ascii():
    for i in range(0, 256):
        print(i, "=", chr(i))
        if (i + 1) % 20 == 0:
            op = input("\nContinuar? (s/n): ")
            if op.lower() != "s":
                break
tabela_ascii()

#exercicio 16
def media_pares():
    soma = 0
    contador = 0
    while contador < 30:
        num = int(input("\nDigite um número par entre 1 e 50: "))
        if num >= 1 and num <= 50 and num % 2 == 0:
            soma += num
            contador += 1
        else:
            print("Número inválido")
    media = soma / 30
    print("Média:", media)
media_pares()

#exercicio 17
def multiplos():
    print("\n")
    for i in range(1, 1001):
        if i % 5 == 0 and i % 3 != 0:
            print(i)
multiplos()

#exercicio 18
def numeros_perfeitos():
    num = int(input("\nDigite um número: "))
    contador = 0
    for i in range(1, num + 1):
        soma = 0
        for j in range(1, i):
            if i % j == 0:
                soma += j
        if soma == i:
            print("Número perfeito:", i)
            contador += 1
    print("Total de números perfeitos:", contador)
numeros_perfeitos()
 
#exercicio 19
def bonatchi():
    a = 1
    b = 1
    print(a)
    print(b)
    for i in range(58):
        c = a + b
        print(c)
        a = b
        b = c
bonatchi()

#teste_final1
def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def contar_divisores(num):
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1
    return contador
def eh_perfeito(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    return soma == num
def analisar_numeros():
    num = int(input("\nDigite um valor entre 1 e 30000: "))
    while num < 1 or num > 30000:
        print("Valor inválido.")
        num = int(input("\nDigite um valor entre 1 e 30000: "))
    contador = 0
    for i in range(1, num + 1):
        print("\nNúmero:", i)
        if eh_primo(i):
            print("Primo: Sim")
        else:
            print("Primo: Não")
        print("Quantidade de divisores:", contar_divisores(i))
        if eh_perfeito(i):
            print("Número perfeito: Sim")
        else:
            print("Número perfeito: Não")
        contador += 1
        if contador % 10 == 0:
            op = input("\nContinuar? (s/n): ")
            if op.lower() != "s":
                break
def calculadora():
    n1 = float(input("Digite o 1º número: "))
    while n1 < 1 or n1 > 1000:
        print("Valor inválido.")
        n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    while n2 < 1 or n2 > 1000:
        print("Valor inválido.")
        n2 = float(input("Digite o 2º número: "))
    op = input("Operação (+, -, *, /): ")
    if op == "+":
        print("Resultado:", n1 + n2)
    elif op == "-":
        print("Resultado:", n1 - n2)
    elif op == "*":
        print("Resultado:", n1 * n2)
    elif op == "/":
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Não é possível dividir por zero.")
    else:
        print("Operação inválida.")
def tabuada():
    num = int(input("Digite o número da tabuada (1 a 1000): "))
    while num < 1 or num > 1000:
        print("Valor inválido.")
        num = int(input("Digite o número da tabuada (1 a 1000): "))

    maximo = int(input("Até onde quer multiplicar? (1 a 1000): "))
    while maximo < 1 or maximo > 1000:
        print("Valor inválido.")
        maximo = int(input("Até onde quer multiplicar? (1 a 1000): "))
    contador = 0
    for i in range(1, maximo + 1):
        print(f"{num} x {i} = {num * i}")
        contador += 1

        if contador % 20 == 0:
            op = input("\nContinuar? (s/n): ")
            if op.lower() != "s":
                break
def menu_principal():
    opcao = ""

    while opcao != "0":
        print("\n===== MENU =====")
        print("1 - Analisar números")
        print("2 - Calculadora")
        print("3 - Tabuada")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            analisar_numeros()
        elif opcao == "2":
            calculadora()
        elif opcao == "3":
            tabuada()
        elif opcao == "0":
            print("Programa terminado.")
        else:
            print("Opção inválida.")
menu_principal()

#teste_final2
clientes = []
num_cliente = 1

def calcular_divfin(compra):
    if compra >= 100 and compra <= 200:
        desconto = compra * 0.05
    elif compra > 200 and compra < 500:
        desconto = compra * 0.10
    elif compra > 500:
        desconto = compra * 0.15
    else:
        desconto = 0
    divfin = compra - desconto
    return divfin
def inserir_cliente():
    global num_cliente
    nome = input("Nome do cliente: ")
    while nome == "":
        print("Nome inválido.")
        nome = input("Nome do cliente: ")
    morada = input("Morada: ")
    while morada == "":
        print("Morada inválida.")
        morada = input("Morada: ")
    tel = input("Telefone: ")
    while not tel.isdigit() or len(tel) < 9:
        print("Telefone inválido.")
        tel = input("Telefone: ")
    nif = input("NIF: ")
    while not nif.isdigit() or len(nif) != 9:
        print("NIF inválido.")
        nif = input("NIF: ")
    compra = float(input("Valor da compra: "))
    while compra < 0:
        print("Compra inválida.")
        compra = float(input("Valor da compra: "))
    divfin = calcular_divfin(compra)
    cliente = {
        "numcli": num_cliente,
        "nome": nome,
        "morada": morada,
        "tel": tel,
        "nif": nif,
        "compra": compra,
        "divfin": divfin
    }
    clientes.append(cliente)
    print("Cliente inserido com sucesso.")
    print("Número do cliente:", num_cliente)
    num_cliente += 1
def listar_clientes():
    if len(clientes) == 0:
        print("Não existem clientes registados.")
        return
    for cliente in clientes:
        print("\n======================")
        print("Númcli:", cliente["numcli"])
        print("NomCli:", cliente["nome"])
        print("Morada:", cliente["morada"])
        print("Tel:", cliente["tel"])
        print("NIF:", cliente["nif"])
        print("Compra:", cliente["compra"])
        print("Divfin:", cliente["divfin"])
        op = input("\nContinuar para o próximo cliente? (s/n): ")
        if op.lower() != "s":
            break
def procurar_cliente():
    if len(clientes) == 0:
        print("Não existem clientes registados.")
        return
    numero = int(input("Digite o número do cliente: "))
    encontrado = False
    for cliente in clientes:
        if cliente["numcli"] == numero:
            print("\n===== CLIENTE ENCONTRADO =====")
            print("Númcli:", cliente["numcli"])
            print("NomCli:", cliente["nome"])
            print("Morada:", cliente["morada"])
            print("Tel:", cliente["tel"])
            print("NIF:", cliente["nif"])
            print("Compra:", cliente["compra"])
            print("Divfin:", cliente["divfin"])
            encontrado = True
            break
    if not encontrado:
        print("Cliente não encontrado.")
def menu_clientes():
    opcao = ""
    while opcao != "0":
        print("\n===== MENU CLIENTES =====")
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Procurar cliente por número")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            procurar_cliente()
        elif opcao == "0":
            print("Programa terminado.")
        else:
            print("Opção inválida.")
menu_clientes()
