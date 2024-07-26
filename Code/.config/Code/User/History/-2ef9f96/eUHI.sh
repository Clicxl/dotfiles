#!/bin/bash

# Bash Extras

# Linking
# Homebrew
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# Bat Config
export BAT_THEME=Catppuccin Mocha

# Autojump
. /usr/share/autojump/autojump.bash

# --------------------------------------------------------------------------------- #
# Fastfetch
fastfetch


# Download All required Dependiencies
# function

# IP address lookup
alias whatismyip="whatsmyip"
function whatsmyip ()
{
	# Internal IP Lookup.
	if [ -e /sbin/ip ]; then
		echo -n "Internal IP: "
		/sbin/ip addr show wlan0 | grep "inet " | awk -F: '{print $1}' | awk '{print $2}'
	else
		echo -n "Internal IP: "
		/sbin/ifconfig wlan0 | grep "inet " | awk -F: '{print $1} |' | awk '{print $2}'
	fi

	# External IP Lookup
	echo -n "External IP: "
	curl -s ifconfig.me
}

function install_dependencies() {
    local dtype
    dtype=$(distribution)


    case $dtype in "debian")

    sudo apt-get install nala # Install Nala
    sudo nala install fzf # Installing Main Dependencies

    # Installing Home Brew
    sudo nala install build-essential procps curl file git
    home
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Installing Brew Formulae
    brew install autojump eza fastfetch

    ;;

    esac
}