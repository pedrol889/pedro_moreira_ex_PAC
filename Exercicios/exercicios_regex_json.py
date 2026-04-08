import json
import re
from urllib.parse import urlparse

# Exercicio 1: Ler o ficheiro JSON
with open("exercicios_regex.json", "r", encoding="utf-8") as f:
    registos = json.load(f)

# Exercicio 2: Validar emails com regex
regex_email = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

# Exercicio 3: Extrair domínios dos sites
def extrair_dominio(url):
    dominio = urlparse(url).netloc.lower()
    if dominio.startswith("www."):
        dominio = dominio[4:]
    return dominio

# Exercicio 4: Validar NIFs com regex
regex_nif = re.compile(r"^[123568]\d{8}$")

# Exercicio 5: Guardar apenas os registos válidos num novo ficheiro JSON
def telemovel_valido(telemovel):
    digitos = re.sub(r"\D", "", telemovel)
    return len(digitos) == 9

registos_validos = []

for registo in registos:
    email_ok = bool(regex_email.match(registo["email"]))
    nif_ok = bool(regex_nif.match(registo["nif"]))
    telemovel_ok = telemovel_valido(registo["telemovel"])
    dominio = extrair_dominio(registo["site"])

    print(f'Nome: {registo["nome"]}')
    print(f'Email válido: {email_ok}')
    print(f'Domínio do site: {dominio}')
    print(f'NIF válido: {nif_ok}')
    print(f'Telemóvel válido: {telemovel_ok}')
    print("-" * 30)

    if email_ok and nif_ok and telemovel_ok:
        registos_validos.append(registo)

with open("registos_validos.json", "w", encoding="utf-8") as f:
    json.dump(registos_validos, f, ensure_ascii=False, indent=2)

# Exercicio 6: Criar um ficheiro .txt com as keys nome e email
with open("nome_email.txt", "w", encoding="utf-8") as f:
    for registo in registos:
        f.write(f'Nome: {registo["nome"]} | Email: {registo["email"]}\n')
