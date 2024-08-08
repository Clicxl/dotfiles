from subprocess import run
from utils.functions import commandExists


def Code():
    module = "code"

    want = input(f"Do you want to Install {module}: (y/n) ")

    if want.lower() in ["y", "yes"] and commandExists(module) is False:
        print(f"Installing {module}")
        run(f"sudo nala install {module}", shell=True)
    elif commandExists(f"{module}"):
        print(f"You Already Have {module}")
    elif want.lower() in ["n", "no"]:
        pass
    else:
        print("Please Enter Correct input")
        Code()
        return

    print(f"Connecting {module}")
    run(f"stow --adopt {module}", shell=True)
