#ex 1 
palavras = ["banana", "uva", "abacaxi", "laranja"]

houve_troca = True

while houve_troca:
    houve_troca = False
    
    for i in range(len(palavras) - 1):
        
        p1 = palavras[i]
        p2 = palavras[i + 1]
        
        # comparar letra a letra
        j = 0
        trocar = False
        
        while j < len(p1) and j < len(p2):
            if ord(p1[j]) > ord(p2[j]):
                trocar = True
                break
            elif ord(p1[j]) < ord(p2[j]):
                break
            j += 1
        
        # caso uma seja prefixo da outra
        if j == len(p1) and len(p1) < len(p2):
            trocar = False
        elif j == len(p2) and len(p2) < len(p1):
            trocar = True
        
        if trocar:
            palavras[i], palavras[i + 1] = palavras[i + 1], palavras[i]
            houve_troca = True

print(palavras)


#ex2
palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]

houve_troca = True

while houve_troca:
    houve_troca = False
    
    for i in range(len(palavras) - 1):
        
        p1 = palavras[i].lower()
        p2 = palavras[i + 1].lower()
        
        j = 0
        trocar = False
        
        while j < len(p1) and j < len(p2):
            if ord(p1[j]) < ord(p2[j]):  # invertido
                trocar = True
                break
            elif ord(p1[j]) > ord(p2[j]):
                break
            j += 1
        
        if trocar:
            palavras[i], palavras[i + 1] = palavras[i + 1], palavras[i]
            houve_troca = True

print(palavras)

#ex3
palavra = "algoritmo"

letras = list(palavra)

houve_troca = True

while houve_troca:
    houve_troca = False
    
    for i in range(len(letras) - 1):
        if ord(letras[i]) > ord(letras[i + 1]):
            letras[i], letras[i + 1] = letras[i + 1], letras[i]
            houve_troca = True

resultado = "".join(letras)

print(resultado)

#ex4
palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

def contar_minusculas(palavra):
    contador = 0
    for letra in palavra:
        if 'a' <= letra <= 'z':
            contador += 1
    return contador

houve_troca = True

while houve_troca:
    houve_troca = False
    
    for i in range(len(palavras) - 1):
        if contar_minusculas(palavras[i]) > contar_minusculas(palavras[i + 1]):
            palavras[i], palavras[i + 1] = palavras[i + 1], palavras[i]
            houve_troca = True

print(palavras)

#ex5
palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

grupos = {}

# agrupar
for palavra in palavras:
    inicial = palavra[0]
    
    if inicial not in grupos:
        grupos[inicial] = []
    
    grupos[inicial].append(palavra)

# ordenar cada grupo
for chave in grupos:
    lista = grupos[chave]
    
    houve_troca = True
    
    while houve_troca:
        houve_troca = False
        
        for i in range(len(lista) - 1):
            
            p1 = lista[i]
            p2 = lista[i + 1]
            
            j = 0
            trocar = False
            
            while j < len(p1) and j < len(p2):
                if ord(p1[j]) > ord(p2[j]):
                    trocar = True
                    break
                elif ord(p1[j]) < ord(p2[j]):
                    break
                j += 1
            
            if trocar:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                houve_troca = True

print(grupos)