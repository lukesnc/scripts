alias multipull="find . -mindepth 1 -maxdepth 1 -type d -print -exec git -C {} pull \;"
alias cd..="cd .."
alias lt='du -sh * | sort -h'
alias pacman-autoremove="pacman -Qtdq | sudo pacman -Rs -"
