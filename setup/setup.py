from subprocess import run
from os import path

from utils.functions import link_module,commandExists

from utils.kitty import Kitty
from utils.terminalMultiplexer import Multiplexer
from utils.ulauncher import Ulauncher
from utils.shell import shell


HOME = path.expanduser("~")
DOTFILES = HOME + "/dotfiles"


# install function
def install():

    module_installer = ['code','bat','nvim','fastfetch','fzf']

    for module in module_installer:
        link_module(module)

    Kitty()
    Multiplexer()
    Ulauncher()
    shell()

    print("Installation completed")


if __name__ == "__main__":

    print(f"Changing to the {DOTFILES} directory")
    run(["cd", DOTFILES], shell=True)

    if commandExists("stow"):
        install()
    else:
        run("sudo nala install stow", shell=True)
        install()


