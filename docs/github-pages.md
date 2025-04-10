## Despliegue en GitHub Pages con MkDocs

1. Asegúrate de tener `mkdocs` y `mkdocs-material` instalados:

```bash
pip install mkdocs mkdocs-material
```

2. Lanza el servidor local para revisar:

```bash
mkdocs serve
```

3. Publica en GitHub Pages usando:

```bash
mkdocs gh-deploy --clean
```

Esto desplegará el sitio web en la rama `gh-pages` del repositorio actual. Asegúrate de habilitar GitHub Pages desde esa rama en la configuración del repositorio.
