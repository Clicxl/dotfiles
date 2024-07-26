#!/bin/bash

RC='\e[0m'
RED='\e[31m'
YELLOW='\e[33m'
GREEN='\e[32m'

# Check if the home directory and bashtoolbox folder exist, create them if they don't
BASHTOOLBOX="$HOME/bashtoolbox"

if [[ ! -d "$BASHTOOLBOX" ]]; then
    echo -e "${YELLOW}Creating bashtoolbox directory: $BASHTOOLBOX${RC}"
    mkdir -p "$BASHTOOLBOX"
    echo -e "${GREEN}bashtoolbox directory created: $BASHTOOLBOX${RC}"
fi

if [[ ! -d "$BASHTOOLBOX/mybash" ]]; then
    echo -e "${YELLOW}Cloning mybash repository into: $BASHTOOLBOX/mybash${RC}"
    git clone https://github.com/Clicxl/mybash "$BASHTOOLBOX/mybash"
    if [[ $? -eq 0 ]]; then
        echo -e "${GREEN}Successfully cloned mybash repository${RC}"
    else
        echo -e "${RED}Failed to clone mybash repository${RC}"
        exit 1
    fi
fi

cd "$LINUXTOOLBOXDIR/mybash" || exit


# Checks if a command exsists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# --------------------------------------------------------------------------------- #

# Checking if Requirments
checkEnv() {
    ## Check for requirements.
    REQUIREMENTS='' #TODO
    for req in ${REQUIREMENTS}; do
        if ! command_exists ${req}; then
            echo -e "${RED}To run me, you need: ${REQUIREMENTS}${RC}"
            exit 1
        fi
    done
# --------------------------------------------------------------------------------- #

    ## Check Package Handeler
    PACKAGEMANAGER='nala apt yum dnf pacman zypper emerge xbps-install nix-env'

    for pgm in ${PACKAGEMANAGER}; do
        if command_exists ${pgm}; then
            PACKAGER=${pgm}
            echo -e "Using ${pgm}"
            break
        fi
    done

    if [ -z "${PACKAGER}" ]; then
        echo -e "${RED}Can't find a supported package manager${RC}"
        exit 1
    fi
# --------------------------------------------------------------------------------- #

    #Checks if sudo previalges are given
    if command_exists sudo; then
        SUDO_CMD="sudo"
    elif command_exists doas && [ -f "/etc/doas.conf" ]; then
        SUDO_CMD="doas"
    else
        SUDO_CMD="su -c"
    fi

    echo "Using ${SUDO_CMD} as privilege escalation software"
# --------------------------------------------------------------------------------- #

    ## Check if the current directory is writable.
    GITPATH="$(dirname "$(realpath "$0")")"
    if [[ ! -w ${GITPATH} ]]; then
        echo -e "${RED}Can't write to ${GITPATH}${RC}"
        exit 1
    fi
# --------------------------------------------------------------------------------- #

    ## Check SuperUser Group
    SUPERUSERGROUP='wheel sudo root'
    for sug in ${SUPERUSERGROUP}; do
        if groups | (command_exists rg && rg -q ${sug} || grep -q ${sug}); then
            SUGROUP=${sug}
            echo -e "Super user group ${SUGROUP}"
            break
        fi
    done
# --------------------------------------------------------------------------------- #

    ## Check if member of the sudo group.
    if ! groups | (command_exists rg && rg -q ${SUGROUP} || grep -q ${SUGROUP}); then
        echo -e "${RED}You need to be a member of the sudo group to run me!${RC}"
        exit 1
    fi
}

# --------------------------------------------------------------------------------- #

# Install the Dependecies
installDepend() {
    ## Check for dependencies.
    DEPENDENCIES='bash bash-completion tar bat tree multitail fastfetch'
    if ! command_exists nvim; then
        DEPENDENCIES="${DEPENDENCIES} neovim"
    fi
# --------------------------------------------------------------------------------- #



}