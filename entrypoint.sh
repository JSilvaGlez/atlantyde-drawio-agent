#!/bin/bash
mkdir -p /home/drawio/diagrams
cd /home/drawio/diagrams || exit 1
exec "$@"


# This script creates a directory for diagrams and changes the working directory to it.
# It then executes the command passed as arguments to the script.
# The script is intended to be used as an entrypoint for a Docker container.
# It ensures that the diagrams directory exists and is the current working directory before executing the command.
# The script uses the `mkdir` command to create the directory and the `cd` command to change the working directory.
# The `exec` command is used to replace the shell with the command specified in the arguments.
# The `|| exit 1` part ensures that if the `cd` command fails, the script will exit with a status code of 1.
# This is a simple shell script that creates a directory for diagrams and changes the working directory to it.
# It is intended to be used as an entrypoint for a Docker container.