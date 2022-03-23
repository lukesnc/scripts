#!/bin/bash

sudo apt install -y build-essential unzip curl git wget ssh
# Arch
# sudo pacman -S base-devel unzip wget openssh git

# Symlink to windows home dir
ln -sf "/mnt/c/Users/$USER" ~/winhome

# zsh (Add the plugin to the list of plugins inside ~/.zshrc)
sudo apt install -y zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
