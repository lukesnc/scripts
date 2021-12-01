#!/bin/bash
# Only use on Debian based distros

# Updates
sudo apt update
sudo apt dist-upgrade -y
sudo apt autoremove -y
sudo apt autoclean

# Base
sudo apt install -y build-essential unzip curl git wget ssh
# Extras
sudo apt install -y vim nmap jq netcat neofetch man-db

# Symlink to windows home dir
ln -sf "/mnt/c/Users/$USER" ~/win-home

# Use custom aliases
cp ./.bash_aliases ~

echo "Done. Restart bash."
