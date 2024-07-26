#!/bin/bash

# Bash Extras

# Linking
# Homebrew
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# Bat Config
export BAT_THEME=Catppuccin Mocha

# Autojump
[ -f "$HOMEBREW_PREFIX"/etc/profile.d/autojump.sh ] && . "$HOMEBREW_PREFIX"/etc/profile.d/autojump.sh

# --------------------------------------------------------------------------------- #
# Fastfetch
if [ -f /usr/bin/fastfetch ]; then
	fastfetch
fi


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

# Install the Dependecies
install_dependencies() {
    local dtype
    dtype=$(if [ -f /etc/os-release ]; then . /etc/os-release && echo "$ID"; elif type lsb_release >/dev/null 2>&1; then echo "$(lsb_release -si)"; elif [ -f /etc/debian_version ]; then echo "debian"; else echo "unknown"; fi)

    DEPENDENCIES="fzf build-essential procps curl file git"

    case $dtype in
        "debian")
            ${SUDO_CMD} apt-get install nala
            ${SUDO_CMD} nala install "${DEPENDENCIES}"
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            brew install eza zoxide
            ;;
        *)
            echo "Unsupported distribution: $dtype"
            ;;
    esac
}

#fzf - For fzf 0.48.0 or more 
# eval "$(fzf --bash)"
#zoxide
eval "$(zoxide init bash)"
