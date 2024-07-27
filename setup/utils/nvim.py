from subprocess import run
from utils.functions import commandExists


def Nvim():
    module = "nvim"

    want = input(f"Do you want to Install {module}: (y/n) ")

    if want.lower() in ["y", "yes"] and commandExists(module) is False:
        print(f"Installing {module}")
        run(f"sudo nala install {module}", shell=True)
        print("Installing LazyVim")

    elif commandExists(f"{module}"):
        print(f"You Already Have {module}")
    elif want.lower() in ["n", "no"]:
        pass
    else:
        print("Please Enter Correct input")
        Nvim()
        return

    print(f"Connecting {module}")
    run(f"stow {module}",shell=True)

