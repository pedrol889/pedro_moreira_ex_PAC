import os

# Diretório base do projeto (onde está este ficheiro)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Cabeçalhos HTTP (identificação do crawler)
HEADERS = {
    "User-Agent": "EducationalCrawler/1.0 (uso académico; contacto: estudante@exemplo.pt)"
}

# Delay entre pedidos
DELAY = 1  # segundos
# Timeout das requisições
TIMEOUT = 5  # segundos
# Caminho para o ficheiro JSON de saída
OUTPUT_JSON = os.path.join(BASE_DIR, "data", "resultados.json")
# Caminho para o ficheiro de logs
LOG_FILE = os.path.join(BASE_DIR, "logs", "crawler.log")
# Bónus: limitar crawling ao mesmo domínio
APENAS_MESMO_DOMINIO = True