FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    curl git unzip xdg-utils libgtk-3-0 libxss1 libasound2 libnss3 libx11-xcb1 \
    && useradd -ms /bin/bash drawio

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
