#!/bin/bash
# sync_git.sh
# Sincroniza los cambios en el directorio "diagrams" con el repositorio Git.

set -e

# Verificar que nos encontramos en un repositorio Git.
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "Este directorio no es un repositorio Git."
  exit 1
fi

# Configurar el usuario (ajusta estos valores según tu entorno)
git config user.name "CI Bot"
git config user.email "ci-bot@example.com"

echo "Agregando cambios en el directorio 'diagrams'..."
git add diagrams

# Comprobar si hay cambios para commitear.
if git diff-index --quiet HEAD; then
  echo "No hay cambios para sincronizar."
else
  COMMIT_MSG="Automated sync: Exported diagrams updated on $(date +'%Y-%m-%d %H:%M:%S')"
  echo "Realizando commit con mensaje: $COMMIT_MSG"
  git commit -m "$COMMIT_MSG"
  echo "Realizando push..."
  git push
fi
