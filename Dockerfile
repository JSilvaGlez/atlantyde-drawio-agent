FROM debian:bullseye

# Actualiza el índice de paquetes e instala dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    xdg-utils \
    libgtk-3-0 \
    libxss1 \
    libasound2 \
    libnss3 \
    libx11-xcb1 \
    bsdutils \
    && useradd -ms /bin/bash drawio

# Descarga e instalación robusta del paquete draw.io-desktop (versión 26.2.2)
RUN curl -fL https://github.com/jgraph/drawio-desktop/releases/download/v26.2.2/drawio-amd64-26.2.2.deb -o drawio.deb && \
    dpkg -i drawio.deb || (apt-get install -yf && dpkg -i drawio.deb) && \
    rm drawio.deb

# Copia scripts, entrypoint y plantillas al contenedor
COPY scripts/ /usr/local/bin/
COPY entrypoint.sh /entrypoint.sh
COPY templates/ /home/drawio/templates/

# Otorga permisos de ejecución a los scripts y entrypoint
RUN chmod +x /entrypoint.sh /usr/local/bin/*.sh

# Define el volumen donde se almacenarán los diagramas
VOLUME ["/home/drawio/diagrams"]

# Establece el directorio de trabajo y cambia al usuario no privilegiado
WORKDIR /home/drawio
USER drawio

# Define el punto de entrada del contenedor
ENTRYPOINT ["/entrypoint.sh"]
