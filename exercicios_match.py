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
