from subprocess import run
from utils.functions import commandExists
import inquirer


def Kitty():
    module = "kitty"

    if not commandExists(module):
        print(f"Installing {module}")
        print("Downloading kitty installer")
        run("curl -L https://sw.kovidgoyal.net/kitty/installer.sh > installer.sh", shell=True)
        print("Running kitty installer")
        run("bash installer.sh /dev/stdin", shell=True)
        print("Creating symbolic links")
        run("ln -sf ~/.local/kitty.app/bin/kitty ~/.local/kitty.app/bin/kitten ~/.local/bin/", shell=True)
        run("ln -sf ~/.local/kitty.app/share/applications/kitty.desktop ~/.local/share/applications/", shell=True)
        run("ln -sf ~/.local/kitty.app/share/applications/kitty-open.desktop ~/.local/share/applications/", shell=True)
        print("Updating .desktop files")
        run('sed -i "s|Icon=kitty|Icon=$(readlink -f ~)/.local/kitty.app/share/icons/hicolor/256x256/apps/kitty.png|g" ~/.local/share/applications/kitty*.desktop', shell=True)
        run('sed -i "s|Exec=kitty|Exec=$(readlink -f ~)/.local/kitty.app/bin/kitty|g" ~/.local/share/applications/kitty*.desktop', shell=True)
        print("Updating xdg-terminals.list")
        run("echo 'kitty.desktop' > ~/.config/xdg-terminals.list", shell=True)
        run("rm installer.sh", shell=True)

        # Prompt the user to decide whether to link the kitty module
    link_question = [
        inquirer.List(
            "link",
            message=f"Do you want to link {module}?",
            choices=["yes", "no"],
        )
    ]
    link_desired = inquirer.prompt(link_question)["link"]

    # If the user chooses to link it, link the kitty module
    if link_desired == "yes":
        print(f"Linking {module}")
        run(f"stow {module}", shell=True)
