#exercicio 1
day = input("\nDigite um dia da semana:")
match day:
    case "Segunda" | "Terca" | "Quarta" | "Quinta" | "Sexta":
        print("Dia de semana")
    case "Sabado" | "Domingo":
        print("Fim de Semana")
    case _:
        print("Invalido")

#exercicio 2
nota = int(input("\nDigite um numero entre 0 a 100:"))
match nota:
    case n if 90 <= n <= 100:
        print("Excelente")
    case n if 70 <= n <= 89:
        print("Bom") 
    case n if 50 <= n <= 69:
        print("Suficiente")
    case n if 0 <= n <= 49:
        print("Insuficiente")
    case _:
        print("Invalido")  

#exercicio 3
pedido = eval(input("\nEntrada: "))
match pedido:
    case {"tipo": "compra", "valor": v}:
        print(f"Compra de {v}€")
    case {"tipo": "venda", "valor": v}:
        print(f"Venda de {v}€")
    case _:
        print("Invalido")

# exercicio 4
valor = eval(input("\nDigite um valor: "))
match valor:
    case int():
        print("Numero Inteiro")
    case float():
        print("Numero Decimal")
    case str() if valor.isnumeric():
        print("String numerica")
    case str():
        print("String textual")
    case list():
        print("Lista")
    case _:
        print("Invalido")
  
#exercicio 5
opcao = str(input("\nEscreva uma mensagem:"))
match opcao:
    case "ola" | "olá" | "bom dia":
        print("Saudação")
    case _ if opcao.endswith("?"):
        print("Pergunta")
    case "tchau" | "adeus":
        print("Despedida")
    case _:
        print("Mensagem genérica")

#exercicio 6
server = eval(input("\nEntrada: "))
match server:
    case {"status": "ok", "tempo_resposta": v} if v >= 200:
        print(f"Servidor lento")
    case {"status": "ok", "tempo_resposta": v}:
        print(f"Servidor ativo")
    case {"status": "erro", "tempo_resposta": v}:
        print(f"Servidor indesponivel")
    case _:
        print("Estado desconhecido")

#exercicio 7
produto = eval(input("\nEntrada: "))
match produto:
    case {"categoria": "eletronico", "preço": v} if v > 1000:
        print(f"Produto de luxo")
    case {"categoria": "eletronico", "preço": v} if v <=1000:
        print(f"Produto de comum")
    case {"categoria": "alimento", "preço": v}:
        print(f"Produto alimentar")
    case _:
        print("Categoria desconhecida")

#exercicio 8
operacao = input("\nOperação: ").lower()
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

match operacao:
    case "soma":
        print(n1 + n2)
    case "subtrai":
        print(n1 - n2)
    case "multiplica":
        print(n1 * n2)
    case "divide":
        print(n1 / n2)
    case _:
        print("Operação inválida")

#exercicio 9
req = eval(input("\nEntrada: "))
match req:
    case {"metodo": "GET", "conteudo": _}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c != "":
        print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": ""}:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")

# exercicio 10
j1 = input("\nJogador 1: ").lower()
j2 = input("\nJogador 2: ").lower()
match (j1, j2):
    case ("pedra", "tesoura"):
        print("Jogador 1 venceu")
    case ("tesoura", "papel"):
        print("Jogador 1 venceu")
    case ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra"):
        print("Jogador 2 venceu")
    case ("papel", "tesoura"):
        print("Jogador 2 venceu")
    case ("pedra", "papel"):
        print("Jogador 2 venceu")
    case (x, y) if x == y:
        print("Empate")
    case _:
        print("Jogada inválida")
