#!/bin/bash

#Update && Switching to Windows
function updateSys() {
  # Apt or Nala
  sudo nala update
  sudo nala upgrade -y

  #Brew
  brew update
  brew upgrade

  #Flatpak - Flathub
  flatpak update -y
}

function switchWindows() {
  sudo grub-reboot 'Windows Boot Manager (on /dev/sda1)'
  sudo reboot
}

alias update="updateSys"
alias windows="switchWindows"
alias cls=clear

# ls to eza
alias ls="eza --color=always --long --git --no-filesize --icons=always --no-time --no-user --no-permissions"                                            # Replace the standard `ls` command with `eza` using the specified arguments
alias ll="eza --group --header --group-directories-first --color=always --long --git --no-filesize --icons=always --no-time --no-user --no-permissions" # Show a detailed long-format listing with headers and group directories first, using the specified arguments
alias l="eza -albGF --header --git --color=always --long --no-filesize --icons=always --no-time --no-user --no-permissions"                             # Provide a comprehensive long-format listing with file type indicators, Git status, and icons, using the specified arguments
alias lS="eza -1 --color=always --group-directories-first --icons=always --no-filesize --no-time --no-user --no-permissions"                            # Show the file/folder names in a single column, using the specified arguments
alias lt="eza --tree --level=2 --color=always --group-directories-first --icons=always --no-filesize --no-time --no-user --no-permissions"              # Display the directory contents in a tree-like format, 2 levels deep, using the specified arguments

# tldr
alias what=tldr

# Cat -> Bat
# alias cat=bat

#Copy Paste - Interactive mode
alias cp='cp -i'

#Git
alias init="git init"
alias add='git add'
alias addall='git add .'
alias commit='git commit -m'
alias status='git status'
alias branch='git branch'
alias uninit='rm -rf .git'
alias push='git push origin'
alias clone='git clone'
alias fetch='git fetch'
alias pull='git pull origin'
alias checkout='git checkout'

#fzf
alias fcode='code  $(find . -type d -print | fzf )'
alias fcd='cd $(find . -type d -print | fzf )'
alias fls='eza $(find * -type d | fzf)'
alias fzed='zed  $(find . -type d -print | fzf )'

# Zellij
alias zeload='zellij --layout'

#Replace cd with zoxide
alias cd='z'
