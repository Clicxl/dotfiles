#!/usr/bin/zsh
# Set the directory we want to store zinit and plugins
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.get"

# Download Zinit, if it's not there yet
if [ ! -d "$ZINIT_HOME" ]; then
  mkdir -p "$(dirname $ZINIT_HOME)"
  git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi

# Source/Load zsh
source "${ZINIT_HOME}/zinit.zsh"

# Importing Extras
if [ -f ~/zshrc/zsh_extras.zsh ]; then
  . ~/zshrc/zsh_extras.zsh
fi

# Importing Aliases
if [ -f ~/zshrc/zsh_aliases.zsh ]; then
  . ~/zshrc/zsh_aliases.zsh
fi

if [ -f ~/zshrc/zsh_plugins.zsh ]; then
  . ~/zshrc/zsh_plugins.zsh
fi


#Node And NPM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
[ -s "$NVM_DIR/zsh_completion" ] && \. "$NVM_DIR/zsh_completion" # This loadsvm zsh_completion

