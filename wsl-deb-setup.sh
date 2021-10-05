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

# Append bashrc
echo >> ~/.bashrc
echo "#####" >> ~/.bashrc
echo "cd ~" >> ~/.bashrc
echo 'export PATH="$PATH:/mnt/c/Program Files/Microsoft VS Code/bin"' >> ~/.bashrc

# Symlink to windows home dir
ln -sf "/mnt/c/Users/$USER" ~/win-home

echo "Done. Restart bash."
