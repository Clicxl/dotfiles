#fzf - For fzf 0.48.0 or more
#eval "$(fzf --zsh)"

#fzf for lower versions
# Source FZF key bindings for Zsh
source /usr/share/doc/fzf/examples/key-bindings.zsh

# Source FZF completion for Zsh
source /usr/share/doc/fzf/examples/completion.zsh

# fzf Catppuccin theme
export FZF_DEFAULT_OPTS=" \
--color=bg+:#313244,bg:#1e1e2e,spinner:#f5e0dc,hl:#f38ba8 \
--color=fg:#cdd6f4,header:#f38ba8,info:#cba6f7,pointer:#f5e0dc \
--color=marker:#f5e0dc,fg+:#cdd6f4,prompt:#cba6f7,hl+:#f38ba8"

