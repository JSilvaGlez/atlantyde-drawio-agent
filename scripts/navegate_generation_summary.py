#!/usr/bin/env python3
"""
Genera una tabla resumen de navegación a partir del archivo mkdocs.yml.
Ideal para mostrar en index.md o para sitemap.md.
"""

import yaml
import os

mkdocs_path = os.path.abspath("mkdocs.yml")
docs_path = os.path.abspath("docs")
output_path = os.path.join(docs_path, "index.md")

def format_nav(nav, indent=0):
    lines = []
    prefix = "  " * indent
    for item in nav:
        if isinstance(item, dict):
            for title, sub in item.items():
                if isinstance(sub, list):
                    lines.append(f"{prefix}- **{title}**")
                    lines.extend(format_nav(sub, indent + 1))
                else:
                    path = sub.replace(".md", "").strip("/")
                    lines.append(f"{prefix}- [{title}]({path}/)")
        elif isinstance(item, str):
            lines.append(f"{prefix}- [{item}]({item.replace('.md', '')}/)")
    return lines

def generate_index():
    with open(mkdocs_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    nav = data.get("nav", [])
    lines = [
        "# 🌐 Navegación del Proyecto\n",
        "Este resumen fue generado automáticamente desde `mkdocs.yml`.\n",
        "## 📁 Estructura:\n",
        *format_nav(nav),
        "\n> Generado con `scripts/generate_navigation_summary.py`"
    ]

    os.makedirs(docs_path, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("✅ index.md generado con resumen de navegación.")

if __name__ == "__main__":
    generate_index()
