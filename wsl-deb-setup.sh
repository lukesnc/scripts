#!/bin/bash
# Only use on Debian based distros

# Updates
sudo apt update
sudo apt full-upgrade -y
sudo apt autoclean
sudo apt autoremove -y

# Base
sudo apt install -y build-essential unzip curl git wget ssh
# Langs
sudo apt install -y python3 python3-pip python3-venv ruby-full golang-go php gcc g++ default-jdk nodejs
# Extras
sudo apt install -y vim ranger nmap jq netcat neofetch man-db

# Append bashrc
echo >> ~/.bashrc
echo "#####" >> ~/.bashrc
echo "cd ~" >> ~/.bashrc
echo 'export PATH="$PATH:/mnt/c/Program Files/Microsoft VS Code/bin"' >> ~/.bashrc

# Symlink to windows home dir
ln -s "/mnt/c/Users/$USER" "~/win-home"

echo "Done. Restart bash."
