!${SHELL}

. function.sh

#dotfile directory
dotfiledir="${HOME}/dotfiles"

# List of files to create syslink
files=(bash nvim fastfetch bat ulauncher Code tmux)

#Changing to dotfiles directory
echo "Changing to the ${dotfiledir} directory"

# Create syslink (will overwrite oldfiles)


if command_exists stow; then
  for file in "${files[@]}"; do
    echo "Creating symlink to ${file}"
    stow ${file}
  done
else
  sudo apt install stow

  for file in "${files[@]}"; do
    echo "Creating symlink to ${file}"
    stow ${file}
  done
fi



