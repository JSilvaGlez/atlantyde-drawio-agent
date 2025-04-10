# Guía de Uso: Atlántyde MkDocs + GitHub Pages

Este proyecto documenta todo el ciclo de vida del Agente RPA DrawIO de Atlantyde, alineado con estándares SDLC y buenas prácticas colaborativas.

## 📦 Estructura

- **`docs/`** contiene la documentación en Markdown.
- **`mkdocs.yml`** define la navegación y configuración del sitio.
- **`.github/workflows/gh-pages.yml`** automatiza el despliegue a GitHub Pages.
- **Cada archivo `.md`** incluye una introducción motivadora + una sección final común de colaboración.

## 🚀 Despliegue

Este sitio se despliega automáticamente en cada `push` a `main`:

```bash
mkdocs gh-deploy --force
```

## 📚 Cómo contribuir

1. Lee el archivo `CONTRIBUTING.md`.
2. Edita los archivos en `docs/` o agrega nuevas secciones.
3. Haz commit y push. El workflow se encarga del despliegue.

¡Tu aporte ayuda a crear un sistema colaborativo de documentación que crece con el conocimiento colectivo!

---
