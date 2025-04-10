import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_URL = "https://jsilvaglez.github.io/atlantyde-drawio-agent/"
DOMAIN = urlparse(BASE_URL).netloc

visited = set()
to_visit = set([""])

os.makedirs("extracted_docs", exist_ok=True)

print("🌐 Iniciando análisis dinámico de navegación...")

while to_visit:
    path = to_visit.pop()
    if path in visited:
        continue
    visited.add(path)

    full_url = urljoin(BASE_URL, path)
    print(f"📥 Fetching: {full_url}")
    try:
        res = requests.get(full_url, timeout=10)
    except Exception as e:
        print(f"⚠️ Error al acceder a {full_url}: {e}")
        continue

    if res.status_code != 200:
        print(f"⚠️ Código inesperado {res.status_code} en {full_url}")
        continue

    soup = BeautifulSoup(res.text, 'html.parser')
    article = soup.find("article") or soup.body
    markdown = md(str(article), heading_style="ATX")

    filename = path.strip("/").replace("/", "_") or "index"
    with open(f"extracted_docs/{filename}.md", "w") as f:
        f.write(f"# QA/UAT Extracted from {full_url}\n\n")
        f.write(markdown)

    # Extraer nuevos enlaces dentro del sitio
    for link in soup.find_all("a", href=True):
        href = link['href']
        parsed = urlparse(href)

        # Solo enlaces relativos o internos al dominio
        if parsed.netloc and parsed.netloc != DOMAIN:
            continue
        if parsed.scheme and parsed.scheme not in ["", "http", "https"]:
            continue

        # Normalizar la URL relativa
        full_path = parsed.path
        if full_path.startswith("/") and not full_path.startswith("/assets"):
            rel_path = full_path.lstrip("/")
            if not rel_path.endswith("/") and '.' not in rel_path:
                rel_path += "/"
            if rel_path not in visited:
                to_visit.add(rel_path)
