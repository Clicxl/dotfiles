from subprocess import run
from os import path
from utils.functions import commandExists

from utils.bat import Bat
from utils.vscode import Code
from utils.nvim import Nvim
from utils.fastfetch import fastFetch
from utils.kitty import Kitty
from utils.tmux import Tmux
from utils.ulauncher import Ulauncher


HOME = path.expanduser("~")
DOTFILES = HOME + "/dotfiles"


# install function
def installStart():
    Code()
    print("\n")
    Bat()
    print("\n")
    Nvim()
    print("\n")
    fastFetch()
    print("\n")
    Kitty()
    print("\n")
    Tmux()
    print("\n")
    Ulauncher()
    print("\n")
    print("Installation Completed")


print(f"Changing to the {DOTFILES} directory")
run(["cd", DOTFILES], shell=True)


if commandExists("stow"):
    if commandExists("stow"):
        installStart()

    else:
        run("sudo nala install stow", shell=True)
        installStart()
