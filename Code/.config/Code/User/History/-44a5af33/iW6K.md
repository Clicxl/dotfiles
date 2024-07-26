
## Overview of Kesh's `.bashrc` Configuration

The `.bashrc` file is a script that runs every time a new terminal session is started in Unix-like operating systems. It is used to configure the shell session, set up aliases, define functions, and more, making the terminal easier to use and more powerful. Below is a summary of the key sections and functionalities defined in the provided `.bashrc` file.

### Installation
Paste this command in your terminal 
```fallback
mkdir -p ~/build
cd ~/build
git clone https://github.com/Clicxl/mybash
cd mybash
./setup.sh
```
After this is completed run `source ~./bashrc` and restart your terminal

### Initial Setup and System Checks

- **Environment Checks**: The script checks if it is running in an interactive mode and sets up the environment accordingly.
- **System Utilities**: It checks for the presence of utilities like `fastfetch`, `bash-completion`, and system-specific configurations (`/etc/bashrc`).

### Aliases and Functions

- **ls revamp**: Rebind ls to a new, modern, minimalist eza 
- **Update**: Update the whole PC with one `update` command, It updates System, Flatpak and Homebew. 
- **Windows**: Switch to you windows OS with `windows` command using grub(Dual Booting)

### Prompt Customisation and History Management

- **Prompt Command**: The `PROMPT_COMMAND` variable is set to automatically save the command history after each command.
- **History Control**: Settings to manage the size of the history file and how duplicates are handled.

### System-Specific Aliases and Settings

- **Conditional Aliases**: Depending on the system type (like Fedora), it sets specific aliases, e.g., replacing `cat` with `bat`.

### Enhancements and Utilities

- **Color and Formatting**: Enhancements for command output readability using colors and formatting for tools like `ls`, `grep`, and `man`.
- **Navigation Shortcuts**: Aliases to simplify directory navigation, e.g., `alias ..='cd ..'` to go up one directory.
- **Safety Features**: Aliases for safer file operations, like using `trash` instead of `rm` for deleting files, to prevent accidental data loss.
- **Extensive Autojump support**: Easily navigate with `z`, `zi`, or pressing Ctrl+f to launch zi to see frequently used navigation directories.

### Advanced Functions

- **System Information**: Functions to display system information like `distribution()` to identify the Linux distribution.
- **Networking Utilities**: Tools to check internal and external IP addresses.
- **Resource Monitoring**: Commands to monitor system resources like disk usage and open ports.

### Installation and Configuration Helpers

- **Auto-Install**: A function `install_dependencies()` to automatically install necessary utilities based on the system type.

### Conclusion

This `.bashrc` file is a comprehensive setup that not only enhances the shell experience with useful aliases and functions but also provides system-specific configurations and safety features to cater to different user needs and system types. It is designed to make the terminal more user-friendly, efficient, and powerful for an average user.


