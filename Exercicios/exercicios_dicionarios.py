#exercicio 1
alunos = {}

quantidade = int(input("Quantos alunos queres inserir ? "))

for i in range(quantidade):
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    curso = input("Curso do aluno: ")
    alunos[nome] = {
        "idade": idade,
        "curso": curso
    }
for nome, dados in alunos.items():
    print(f"\nnome: {nome}")
    print(f"idade: {dados['idade']}")
    print(f"curso: {dados['curso']}")
    print()

#exercicio 2
carro = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020}
print(carro['modelo'])

#exercicio 3
produto = {}
print("\n")
produto["nome"] = "Telemóvel"
produto["preço"] = 1500
produto["stock"] = 30

del produto["stock"]
print(produto)

#exercicio 4
utilizador = {'nome': 'Carlos', 'idade': 28}
if "email" in utilizador:
    print("Email encontrado.")
else:
    print("\nEmail não encontrado.")

#exercicio 5
palavra = input("\nIntroduz uma palavra: ")
contador = {}
for letra in palavra:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1
print(contador)

#exercicio 6
vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}
total = sum(vendas.values())
print("\nTotal de vendas do trimestre:", total)

#exercicio 7
d = {'a': 1, 'b': 2, 'c': 3}
invertido = {}
print("\n")
for chave, valor in d.items():
    invertido[valor] = chave
print(invertido)

#exercicio 8
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d3 = {**d1, **d2}
print(d3)

#exercicio 9
notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}
for aluno, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"{aluno}: {media}")

#exercicio 10
frase = input("\nIntroduz uma frase: ")
palavras = frase.split()
contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1
print(contador) 