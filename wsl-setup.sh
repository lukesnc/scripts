#!/bin/bash
sudo apt install -y build-essential bash-completion unzip curl git wget ssh vim python3 python3-pip python3-venv jq

git config --global core.editor vim
git config --global pull.rebase false

# Source: https://github.com/amix/vimrc
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh

# Symlink to Windows home dir
ln -sf "/mnt/c/Users/$USER" ~/winhome

echo "Done."
