# ⚙️ Entorno Docker "Atlantyde Diagram Agent"

## 🎯 Objetivos

- Editor Draw.io local en entorno aislado
- Scripts de automatización para:
  - Crear plantillas base
  - Exportar masivamente a PDF/SVG
  - Control de versiones con Git
- Integrable vía volumen compartido en ATLANTYDE

---

## 📦 Estructura del Proyecto

```
atlantyde-drawio-agent/
├── Dockerfile
├── entrypoint.sh
├── scripts/
│   ├── create_template.sh
│   ├── export_all.sh
│   └── sync_git.sh
├── templates/
│   └── base.drawio
├── diagrams/ (volumen compartido)
└── README.md
```

---

## 🐳 Dockerfile

```Dockerfile
FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    curl git unzip xdg-utils libgtk-3-0 libxss1 libasound2 libnss3 libx11-xcb1 \
    && useradd -ms /bin/bash drawio

# Instalar Draw.io Desktop
RUN curl -L https://github.com/jgraph/drawio-desktop/releases/download/v22.0.3/drawio-x64-22.0.3.deb -o drawio.deb && \
    apt install -y ./drawio.deb && rm drawio.deb

COPY scripts/ /usr/local/bin/
COPY entrypoint.sh /entrypoint.sh
COPY templates/ /home/drawio/templates/

RUN chmod +x /entrypoint.sh /usr/local/bin/*.sh

VOLUME ["/home/drawio/diagrams"]

WORKDIR /home/drawio
USER drawio

ENTRYPOINT ["/entrypoint.sh"]
```

---

## 🚀 entrypoint.sh

```bash
#!/bin/bash
mkdir -p /home/drawio/diagrams
cd /home/drawio/diagrams
exec "$@"
```

---

## 🧰 Scripts útiles (`scripts/*.sh`)

- `create_template.sh` – Crea un nuevo archivo basado en una plantilla.
- `export_all.sh` – Exporta todos los `.drawio` a PDF y SVG.
- `sync_git.sh` – Hace commit automático y push opcional.

---

## 🧪 Ejemplo de uso

```bash
docker build -t atlantyde/drawio-agent .
docker run --rm -v $PWD/diagrams:/home/drawio/diagrams -it atlantyde/drawio-agent bash
```

Una vez dentro del contenedor puedes usar:

```bash
create_template.sh infraestructura
export_all.sh
sync_git.sh
```


---

## ✅ Integración Continua (CI)

Este repositorio utiliza [GitHub Actions](https://github.com/features/actions) para automatizar la construcción y verificación del contenedor Docker.

![Atlantyde CI](https://github.com/your-org/atlantyde-drawio-agent/actions/workflows/ci.yml/badge.svg)

---

## 🤝 Colaboración y Flujo de Trabajo

Este proyecto sigue el modelo de colaboración **GitHub Flow**:
1. Crea una rama desde `main` (`feature/mi-nueva-funcionalidad`)
2. Realiza tus cambios y asegúrate de que pasen los tests.
3. Abre un **Pull Request** con una buena descripción.
4. Espera revisión y aprobación.
5. Mergea solo después de pasar los checks de CI.

### Seguridad
- Sigue las buenas prácticas de Dockerfile y configuración.
- Los scripts están revisados para evitar sobreescrituras peligrosas.
- Validación de datos y plantillas asegurada antes del uso.

---

## 📌 Templates para Issues y Pull Requests

Incluye templates para estandarizar la gestión de cambios y solicitudes.
