#!/bin/bash

sudo apt install -y build-essential unzip curl git wget ssh
sudo apt install -y vim nmap netcat man-db

# Symlink to windows home dir
ln -sf "/mnt/c/Users/$USER" ~/winhome

# Use custom aliases
cp ./.bash_aliases ~

echo "Done. Restart bash."
