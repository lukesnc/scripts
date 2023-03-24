#!/bin/bash
sudo apt install -y build-essential unzip curl git wget ssh vim python3 python3-pip
git config --global core.editor vim
git config --global pull.rebase false

# Install awesome vimrc
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh

ln -sf "/mnt/c/Users/$USER" ~/winhome
echo "Created symlink to Windows home dir."

echo "Done."
