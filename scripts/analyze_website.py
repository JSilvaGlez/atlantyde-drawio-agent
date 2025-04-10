import os
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_URL = "https://jsilvaglez.github.io/atlantyde-drawio-agent/"
PAGES = [
    "",
    "getting-started/overview/",
    "user-guide/user-guide-overview/",
    "ci-cd/",
    "security/"
]

os.makedirs("extracted_docs", exist_ok=True)

for page in PAGES:
    url = BASE_URL + page
    print(f"📥 Fetching: {url}")
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        content = soup.find("article") or soup.body
        markdown = md(str(content), heading_style="ATX")

        filename = page.strip("/").replace("/", "_") or "index"
        with open(f"extracted_docs/{filename}.md", "w") as f:
            f.write(f"# QA/UAT Extracted from {url}\n\n")
            f.write(markdown)
    else:
        print(f"⚠️ Failed to fetch {url} with status {r.status_code}")
