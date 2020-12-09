#!/bin/bash
# Only use on Debian based distros

# Updates
sudo apt update
sudo apt full-upgrade -y
sudo apt autoclean
sudo apt autoremove -y

# Base
sudo apt install -y build-essential curl git wget ssh
# Langs
sudo apt install -y python3 python3-pip python3-venv ruby-full golang-go perl php gcc g++ default-jdk nodejs
# Extras
sudo apt install -y libimage-exiftool-perl vim ranger nmap netcat neofetch man-db

# Append bashrc
echo >> ~/.bashrc
echo "#####" >> ~/.bashrc
echo "cd ~" >> ~/.bashrc
echo 'export PATH="$PATH:/mnt/c/Program Files/Microsoft VS Code/bin"' >> ~/.bashrc

echo "Done. Restart bash."
