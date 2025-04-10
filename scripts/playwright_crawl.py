import os
from urllib.parse import urljoin, urlparse
from markdownify import markdownify as md
from playwright.sync_api import sync_playwright

BASE_URL = "https://jsilvaglez.github.io/atlantyde-drawio-agent/"

os.makedirs("extracted_docs", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(BASE_URL)

    links = set()
    for link in page.locator("a").all():
        href = link.get_attribute("href")
        if href and href.startswith("/") and not href.startswith("/assets"):
            full_url = urljoin(BASE_URL, href)
            links.add(full_url)

    # Agregar la home
    links.add(BASE_URL)

    for url in links:
        try:
            print(f"🌐 Visitando: {url}")
            page.goto(url)
            page.wait_for_load_state('networkidle')

            content_html = page.locator("article").inner_html()
            markdown = md(content_html, heading_style="ATX")

            parsed = urlparse(url)
            filename = parsed.path.strip("/").replace("/", "_") or "index"
            with open(f"extracted_docs/{filename}.md", "w") as f:
                f.write(f"# QA/UAT Extracted from {url}\n\n")
                f.write(markdown)

        except Exception as e:
            print(f"⚠️ Error procesando {url}: {e}")

    browser.close()

