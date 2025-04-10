#!/bin/bash
NAME=$1
cp /home/drawio/templates/base.drawio /home/drawio/diagrams/"$NAME".drawio
echo "Plantilla creada: $NAME.drawio"
