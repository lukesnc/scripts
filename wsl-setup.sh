#!/bin/sh

# Deb
# sudo apt install -y build-essential unzip curl git wget ssh

# Arch
sudo pacman -S base-devel unzip wget openssh git

# Symlink to windows home dir
ln -sf "/mnt/c/Users/$USER" ~/winhome
