#!/bin/bash
# Only use on Debian based distros

# Updates
sudo apt update
sudo apt full-upgrade -y
sudo apt autoclean
sudo apt autoremove -y

# Base
sudo apt install -y build-essential curl
# Langs
sudo apt install -y python3 python3-pip python3-venv python2 ruby golang-go perl php gcc g++ default-jdk
# Extras
sudo apt install -y libimage-exiftool-perl gdb vim ranger nmap netcat neofetch man-db

# Append bashrc
echo >> ~/.bashrc
echo "#####" >> ~/.bashrc
echo "cd ~" >> ~/.bashrc
echo 'export PATH="$PATH:/mnt/c/Program Files/Microsoft VS Code/bin"' >> ~/.bashrc

echo "Done. Restart bash."
