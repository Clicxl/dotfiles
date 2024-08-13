# Kesh
## _Kesh's Dotfiles_


🔧 My Dotfiles Repository: A centralized hub for all my configuration files. Includes settings for my terminal, editor, shell, and more. Easily manage and update my configurations across all devices (Linux / Mac).📁🔧

## Features
Import Installs and Syncs the following setups/configurations
- Code
- Tmux
- Zellij
- Zsh
- Ulauncher
- Fastfetch
- neoVim
- Kitty terminal
- Bat
- Bash


> A very quick and interactive setup for a linux ubuntu based systems

## Installation

Dotfile requires [Python](https://www.python.org/) v3.10+ to run.
1. You can install python from the below command:
    ```sh 
    sudo nala install python3
    ```
2. After installing python update you ubuntu system to get the latest versions of all Files
    ```sh 
    sudo nala update
    sudo nala upgrade -y
    ```
3. Now clone the repo into your dotfiles folder
    ```sh
    git clone https://github.com/Clicxl/dotfiles ~/dotfiles
    ```
4. Now enter into the dotfiles folder 
    ```sh
    cd ~/dotfiles
    ```
5. Install Needed Depencies such as inquirer and run the setup.py script in the setup folder
    ```sh
    pip install inquirer
    python3 setup/setup.py
    ```
6. Complete the installation setup and you are good to go.
