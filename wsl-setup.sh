#!/bin/bash
echo "WSL Setup Script"
#read -srp $'If ssh key is NOT installed press CTRL + C now.\nIf ready to proceed press ENTER...'
#echo

cd ~
sudo apt install -y build-essential unzip curl git wget ssh
git clone https://github.com/lukesnc/scripts.git

cp scripts/.bash_aliases .
echo "Installed .bash_aliases."

cat scripts/ps1/arch.sh >> .bashrc
echo "Set bash prompt to Arch."

ln -sf "/mnt/c/Users/$USER" ~/winhome
echo "Created symlink to Windows home dir."

echo "Done."
