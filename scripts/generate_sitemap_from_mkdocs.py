import yaml
import os
import json
from datetime import datetime

MKDOCS_YML = "mkdocs.yml"
OUTPUT_MD = "docs/sitemap.md"
OUTPUT_JSON = "docs/sitemap.json"

def flatten_nav(nav, parent=""):
    entries = []
    for item in nav:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, list):
                    entries.extend(flatten_nav(value, parent + key + " / "))
                elif isinstance(value, str):
                    entries.append((parent + key, value))
        else:
            entries.append((parent + item, item))
    return entries

with open(MKDOCS_YML, "r") as f:
    config = yaml.safe_load(f)

nav = config.get("nav", [])
flattened = flatten_nav(nav)

md_lines = [ "# Sitemap del Proyecto", "_Este archivo se genera automáticamente desde mkdocs.yml "]
json_output = {
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "entries": []
}

missing_files = []

for title, path in flattened:
    full_path = os.path.join("docs", path)
    url_path = path.replace(".md", "").replace(" ", "-")
    if url_path.endswith("index"):
        url_path = url_path[:-5]
    url = f"https://jsilvaglez.github.io/atlantyde-drawio-agent/{url_path}"

    exists = os.path.exists(full_path)
    if not exists:
        missing_files.append(path)

    md_lines.append(f"- [{title}]({url}) {'⚠️' if not exists else ''}")
    json_output["entries"].append({
        "title": title,
        "path": path,
        "url": url,
        "exists": exists
    })

# Guardar sitemap.md
with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

# Guardar sitemap.json
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(json_output, f, indent=2)

if missing_files:
    print("⚠️ Archivos faltantes detectados:")
    for m in missing_files:
        print(" -", m)
else:
    print("✅ Todos los archivos existen.")
