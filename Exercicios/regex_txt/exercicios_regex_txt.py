import re
from datetime import datetime
from urllib.parse import urlparse

# =========================
# FICHEIRO 1: dados2.txt
# =========================

# Exercício 1: Ler o ficheiro
with open("dados2.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

print("EXERCÍCIO 1 - Conteúdo de dados2.txt:")
print(conteudo)
print("=" * 50)

# Exercício 2: Encontrar todos os emails
regex_email = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
emails = re.findall(regex_email, conteudo)

print("EXERCÍCIO 2 - Emails encontrados:")
for email in emails:
    print(email)
print("=" * 50)

# Exercício 3: Encontrar todos os números de telemóvel
regex_telemovel = r"\b\d{9}\b|\b\d{3}[- ]\d{3}[- ]\d{3}\b"
telemoveis = re.findall(regex_telemovel, conteudo)

print("EXERCÍCIO 3 - Telemóveis encontrados:")
for telemovel in telemoveis:
    print(telemovel)
print("=" * 50)

# Exercício 4: Extrair apenas os nomes
regex_nome = r"Nome:\s*([^,\n]+)"
nomes = re.findall(regex_nome, conteudo)

print("EXERCÍCIO 4 - Nomes encontrados:")
for nome in nomes:
    print(nome)
print("=" * 50)

# Exercício 5: Guardar os dados extraídos num novo ficheiro
regex_linhas = r"Nome:\s*([^,\n]+),\s*Email:\s*([^,\n]+),\s*Telemóvel:\s*([^\n]+)"
registos_extraidos = re.findall(regex_linhas, conteudo)

with open("extraidos.txt", "w", encoding="utf-8") as f:
    for nome, email, telemovel in registos_extraidos:
        f.write(f"{nome} | {email} | {telemovel.strip()}\n")

print("EXERCÍCIO 5 - Ficheiro extraidos.txt criado.")
print("=" * 50)

# Exercício 6: Validar emails que terminam em .pt
emails_pt = [email for email in emails if email.endswith(".pt")]

print("EXERCÍCIO 6 - Emails que terminam em .pt:")
for email in emails_pt:
    print(email)
print("=" * 50)

# =========================
# FICHEIRO 2: registos.txt
# =========================

with open("registos.txt", "r", encoding="utf-8") as f:
    conteudo2 = f.read()

# Exercício 7: Extrair todos os NIFs
regex_nif = r"\b\d{9}\b"
nifs = re.findall(regex_nif, conteudo2)

print("EXERCÍCIO 7 - NIFs encontrados:")
for nif in nifs:
    print(nif)
print("=" * 50)

# Exercício 8: Extrair datas no formato DD/MM/AAAA
regex_data = r"\b\d{2}/\d{2}/\d{4}\b"
datas = re.findall(regex_data, conteudo2)

print("EXERCÍCIO 8 - Datas encontradas:")
for data in datas:
    print(data)
print("=" * 50)

# Exercício 9: Extrair códigos postais portugueses
regex_cp = r"\b\d{4}-\d{3}\b"
codigos_postais = re.findall(regex_cp, conteudo2)

print("EXERCÍCIO 9 - Códigos postais encontrados:")
for cp in codigos_postais:
    print(cp)
print("=" * 50)

# Exercício 10: Extrair apenas os domínios dos sites
regex_sites = r"https?://[^\s|]+"
sites = re.findall(regex_sites, conteudo2)

dominios = []
for site in sites:
    dominio = urlparse(site).netloc
    dominios.append(dominio)

print("EXERCÍCIO 10 - Domínios encontrados:")
for dominio in dominios:
    print(dominio)
print("=" * 50)

# Exercício 11: Validar se todos os NIFs começam com um dígito válido
regex_nif_valido = r"^[123568]\d{8}$"

print("EXERCÍCIO 11 - Validação dos NIFs:")
for nif in nifs:
    if re.match(regex_nif_valido, nif):
        print(f"{nif} -> válido")
    else:
        print(f"{nif} -> inválido")
print("=" * 50)

# Exercício 12: Criar um ficheiro resumo.txt com os dados organizados
regex_registos = r"Nome:\s*([^|]+)\|\s*NIF:\s*(\d{9})\s*\|\s*Data:\s*(\d{2}/\d{2}/\d{4})\s*\|\s*Código Postal:\s*(\d{4}-\d{3})\s*\|\s*Site:\s*(https?://[^\s|]+)"
registos = re.findall(regex_registos, conteudo2)

with open("resumo.txt", "w", encoding="utf-8") as f:
    for nome, nif, data, cp, site in registos:
        dominio = urlparse(site).netloc
        f.write(f"{nome.strip()} | {nif} | {data} | {cp} | {dominio}\n")

print("EXERCÍCIO 12 - Ficheiro resumo.txt criado.")
print("=" * 50)

# Exercício 13: Encontrar registos com datas anteriores a 2025
print("EXERCÍCIO 13 - Registos com datas anteriores a 2025:")
for nome, nif, data, cp, site in registos:
    data_obj = datetime.strptime(data, "%d/%m/%Y")
    if data_obj.year < 2025:
        print(f"{nome.strip()} | {nif} | {data} | {cp} | {urlparse(site).netloc}")
