#exercicio 1
segundos = int(input("Digite os segundos: "))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_finais = resto % 60
if horas == 1:
    h = "hora"
else:
    h = "horas"
if minutos == 1:
    m = "minuto"
else:
    m = "minutos"
if segundos_finais == 1:
    s = "segundo"
else:
    s = "segundos"
print(f"{horas} {h}, {minutos} {m} e {segundos_finais} {s}.")

#exercicio 2
num1 = int(input("\nNum1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))
# valores iniciais
maior = num1
menor = num1
# verificar maior
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
# verificar menor
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print("Maior:", maior)
print("Menor:", menor)

#exercicio 3
num1 = int(input("\nNum1: "))
num2 = int(input("Num2: "))
if num1 < num2:
    crescente1 = num1
    crescente2 = num2
else:
    crescente1 = num2
    crescente2 = num1
print("Crescente:", crescente1, ",", crescente2)
print("Decrescente:", crescente2, ",", crescente1)

#exercicio 4
saldo = float(input("\nSaldo inicial: "))
cheque = float(input("Valor do cheque: "))
if cheque <= saldo:
    saldo = saldo - cheque
    print("Cheque descontado, saldo:", saldo)
else:
    print("Cheque não pode ser descontado")

#exercicio 5
num1 = int(input("\nNum1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))
# ordenar
if num1 <= num2 <= num3:
    a, b, c = num1, num2, num3
elif num1 <= num3 <= num2:
    a, b, c = num1, num3, num2
elif num2 <= num1 <= num3:
    a, b, c = num2, num1, num3
elif num2 <= num3 <= num1:
    a, b, c = num2, num3, num1
elif num3 <= num1 <= num2:
    a, b, c = num3, num1, num2
else:
    a, b, c = num3, num2, num1
print("Crescente:", a, b, c)
print("Decrescente:", c, b, a)

#exercicio 6
nome = input("\nNome do cliente: ")
compra = float(input("Valor da compra: "))

# calcular desconto
if compra <= 200:
    desconto = compra * 0.10
elif compra <= 500:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20
total = compra - desconto
print("Nome:", nome)
print(f"Compra: {compra:.2f}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total a pagar: {total:.2f}€")

#exercicio 7
nota1 = float(input("\nNota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1*2 + nota2*3 + nota3*5) / 10
print(f"Média: {media:.1f}")
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

#exercicio 8
notas = []
# ler 10 notas
for i in range(10):
    nota = float(input(f"\nNota do aluno {i+1}: "))
    notas.append(nota)
# calcular média
media = sum(notas) / len(notas)
# contar alunos >= média
contador = 0
for nota in notas:
    if nota >= media:
        contador += 1
print(f"Média: {media:.2f}")
print("Alunos com nota igual ou acima da média:", contador)

#exercicio 9
mes = int(input("\nDigite um número (1-12): "))
if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Número inválido")

#exercicio 10
pares = 0
impares = 0
for i in range(10):
    num = int(input(f"\nNúmero {i+1}: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Pares:", pares)
print("Ímpares:", impares)