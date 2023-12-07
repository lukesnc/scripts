#!/bin/bash
git config --global core.editor vim
git config --global pull.rebase false

# Symlink to Windows home dir
ln -sf "/mnt/c/Users/$USER" ~/winhome
