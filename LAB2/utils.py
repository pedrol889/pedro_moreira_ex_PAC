import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser


def obter_base_site(url):
    """
    Devolve a base do site, por exemplo:
    https://example.com
    """
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"


def obter_robots_parser(url, headers):
    """
    Tenta ler o robots.txt do site.
    Se existir, devolve o parser.
    Se não existir ou houver erro, devolve None.
    """
    base_site = obter_base_site(url)
    robots_url = urljoin(base_site, "/robots.txt")

    rp = RobotFileParser()
    rp.set_url(robots_url)

    try:
        resposta = requests.get(robots_url, headers=headers, timeout=5)

        if resposta.status_code == 200:
            rp.parse(resposta.text.splitlines())
            return rp

        # Se não existir robots.txt, devolve None
        return None

    except requests.RequestException:
        return None


def permitido_por_robots(url, user_agent, robots_parser):
    """
    Verifica se a URL pode ser visitada segundo o robots.txt.
    Se não existir robots.txt, assume permitido.
    """
    if robots_parser is None:
        return True

    return robots_parser.can_fetch(user_agent, url)


def normalizar_url(link, base_url):
    """
    Converte links relativos em absolutos e remove fragmentos.
    """
    if not link:
        return None

    link_absoluto = urljoin(base_url, link)
    parsed = urlparse(link_absoluto)

    if parsed.scheme not in ["http", "https"]:
        return None

    link_sem_fragmento = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    if parsed.query:
        link_sem_fragmento += f"?{parsed.query}"

    return link_sem_fragmento


def mesmo_dominio(url1, url2):
    """
    Verifica se duas URLs pertencem ao mesmo domínio.
    """
    return urlparse(url1).netloc == urlparse(url2).netloc


def extrair_dados_pagina(html, url_atual):
    """
    Extrai título, links, h1, h2 e parágrafos de uma página.
    """
    soup = BeautifulSoup(html, "html.parser")

    titulo = "Sem título"
    if soup.title and soup.title.string:
        titulo = soup.title.string.strip()

    links = []
    for a in soup.find_all("a", href=True):
        href = a.get("href")
        link_normalizado = normalizar_url(href, url_atual)
        if link_normalizado:
            links.append(link_normalizado)

    links = list(set(links))

    h1 = [tag.get_text(strip=True) for tag in soup.find_all("h1")]
    h2 = [tag.get_text(strip=True) for tag in soup.find_all("h2")]
    paragrafos = [tag.get_text(strip=True) for tag in soup.find_all("p")]
    paragrafos = [p for p in paragrafos if p]

    return {
        "titulo": titulo,
        "links": links,
        "h1": h1,
        "h2": h2,
        "paragrafos": paragrafos
    }