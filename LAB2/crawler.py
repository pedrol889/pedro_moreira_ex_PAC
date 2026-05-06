import json
import time
import logging
import requests
import os

from config import HEADERS, DELAY, TIMEOUT, OUTPUT_JSON, LOG_FILE, APENAS_MESMO_DOMINIO
from utils import (
    obter_robots_parser,
    permitido_por_robots,
    extrair_dados_pagina,
    mesmo_dominio
)

# Garantir que as pastas existem
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)

# Configuração dos logs
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def crawler(url_inicial, max_paginas):
    """
    Crawler ético simples
    """

    resultados = []
    visitadas = set()
    por_visitar = [url_inicial]

    robots_parser = obter_robots_parser(url_inicial, HEADERS)
    user_agent = HEADERS.get("User-Agent", "*")

    # 🔧 NOVO: não bloquear se não existir robots.txt
    if robots_parser is None:
        print("[AVISO] robots.txt não encontrado ou inacessível. O crawler vai continuar com cuidado.")
        logging.warning("robots.txt não encontrado ou inacessível.")
    else:
        print("[INFO] robots.txt lido com sucesso.")
        logging.info("robots.txt lido com sucesso.")

    while por_visitar and len(visitadas) < max_paginas:
        url_atual = por_visitar.pop(0)

        if url_atual in visitadas:
            continue

        # Respeitar robots.txt (se existir)
        if not permitido_por_robots(url_atual, user_agent, robots_parser):
            print(f"[IGNORADO] Bloqueado pelo robots.txt: {url_atual}")
            logging.warning(f"Bloqueado pelo robots.txt: {url_atual}")
            continue

        try:
            print(f"[INFO] A visitar: {url_atual}")
            logging.info(f"A visitar: {url_atual}")

            resposta = requests.get(url_atual, headers=HEADERS, timeout=TIMEOUT)

            if resposta.status_code != 200:
                print(f"[ERRO] Status code {resposta.status_code} em {url_atual}")
                logging.error(f"Status code {resposta.status_code} em {url_atual}")
                continue

            dados = extrair_dados_pagina(resposta.text, url_atual)

            resultado_pagina = {
                "url": url_atual,
                "titulo": dados["titulo"],
                "links": dados["links"],
                "h1": dados["h1"],
                "h2": dados["h2"],
                "paragrafos": dados["paragrafos"]
            }

            resultados.append(resultado_pagina)
            visitadas.add(url_atual)

            # Adicionar novos links à fila
            for link in dados["links"]:
                if link not in visitadas and link not in por_visitar:
                    if APENAS_MESMO_DOMINIO:
                        if mesmo_dominio(url_inicial, link):
                            por_visitar.append(link)
                    else:
                        por_visitar.append(link)

            # Delay 
            time.sleep(DELAY)

        except requests.RequestException as e:
            print(f"[EXCEÇÃO] Erro ao visitar {url_atual}: {e}")
            logging.error(f"Erro ao visitar {url_atual}: {e}")

    # Guardar resultados em JSON
    try:
        with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=4)

        print(f"\n[SUCESSO] Dados guardados em: {OUTPUT_JSON}")
        logging.info(f"Dados guardados em: {OUTPUT_JSON}")

    except Exception as e:
        print(f"[ERRO] Falha ao guardar JSON: {e}")
        logging.error(f"Erro ao guardar JSON: {e}")

    return resultados


# Execução direta
if __name__ == "__main__":
    url = "https://example.com"
    max_paginas = 3

    dados_recolhidos = crawler(url, max_paginas)

    print("\nResumo:")
    print(f"Total de páginas visitadas: {len(dados_recolhidos)}")