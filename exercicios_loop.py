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
