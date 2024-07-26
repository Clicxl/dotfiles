#------------------------------------------------------------------------------#

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
#------------------------------------------------------------------------------#

    ## Check Package Handeler
    PACKAGEMANAGER='nala yum dnf pacman zypper emerge xbps-install nix-env'

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
#------------------------------------------------------------------------------#

# Checks if a command exsists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

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