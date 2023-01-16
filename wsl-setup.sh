#!/bin/bash
echo "WSL Setup Script"

cd ~
sudo apt install -y build-essential unzip curl git wget ssh vim
git clone https://github.com/lukesnc/scripts.git
git config --global core.editor vim

cp scripts/.bash_aliases .
echo "Installed .bash_aliases."

cat scripts/ps1/arch.sh >> .bashrc
echo "Set bash prompt to Arch."

ln -sf "/mnt/c/Users/$USER" ~/winhome
echo "Created symlink to Windows home dir."

echo "Done."
