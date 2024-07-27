from subprocess import run
from utils.functions import commandExists


def Kitty():
    module = "kitty"

    want = input(f"Do you want to Install {module}: (y/n) ")

    if want.lower() in ["y", "yes"] and commandExists(module) is False:
        print(f"Installing {module}")
        run(
            "curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin",
            shell=True,
        )

        print("Creating A .desktop file")
        run(
            "ln -sf ~/.local/kitty.app/bin/kitty ~/.local/kitty.app/bin/kitten ~/.local/bin/",
            shell=True,
        )
        run(
            "cp ~/.local/kitty.app/share/applications/kitty.desktop ~/.local/share/applications/",
            shell=True,
        )
        run(
            "cp ~/.local/kitty.app/share/applications/kitty-open.desktop ~/.local/share/applications/",
            shell=True,
        )
        run(
            'sed -i "s|Icon=kitty|Icon=$(readlink -f ~)/.local/kitty.app/share/icons/hicolor/256x256/apps/kitty.png|g" ~/.local/share/applications/kitty*.desktop',
            shell=True,
        )
        run(
            'sed -i "s|Exec=kitty|Exec=$(readlink -f ~)/.local/kitty.app/bin/kitty|g" ~/.local/share/applications/kitty*.desktop', shell=True
        )
        run("echo 'kitty.desktop' > ~/.config/xdg-terminals.list", shell=True)

    elif commandExists(f"{module}"):
        print(f"You Already Have {module}")
    elif want.lower() in ["n", "no"]:
        pass
    else:
        print("Please Enter Correct input")
        Kitty()
        return

    print(f"Connecting {module}")
    run(f"stow {module}",shell=True)

