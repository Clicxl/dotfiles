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


# Checking if Requirments
checkEnv() {
    ## Check for requirements.
    REQUIREMENTS='curl groups sudo'
    for req in ${REQUIREMENTS}; do
        if ! command_exists ${req}; then
            echo -e "${RED}To run me, you need: ${REQUIREMENTS}${RC}"
            exit 1
        fi
    done
    
}