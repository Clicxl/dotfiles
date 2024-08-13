#!/usr/bin/zsh
#Add Plugins to Zsh

#ZSH Syntax Highlighting
zinit light zsh-users/zsh-syntax-highlighting
#ZSH completions
zinit light zsh-users/zsh-completions
#ZSH autosuggestions
zinit light zsh-users/zsh-autosuggestions
#ZSH Fzf-Tab
zinit light Aloxaf/fzf-tab

#Key Bindings
bindkey "^f" autosuggest-accept
bindkey "^p" history-search-backward
bindkey "^n" history-search-forward



#ZSH Snippets
zinit snippet OMZP::sudo

#ZSH Options
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups


# Autoload completions
autoload -Uz compinit && compinit

zinit cdreplay -q

#Autosuggestions History
HISTSIZE=5000
HISTFILE=~/.zsh_history
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

#Completion styling
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'
zstyle ':fzf-tab:complete:__zoxide_z:*' fzf-preview 'ls --color $realpath'