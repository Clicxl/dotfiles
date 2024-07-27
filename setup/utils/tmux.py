from subprocess import run


def Tmux():
    module = "tmux"

    want = input(f"Do you want to Install {module}: (y/n) ")

    if want.lower() in ["y", "yes"]:
        print(f"Installing {module}")
        run(f"sudo nala install {module}", shell=True)
    elif want.lower() in ["n", "no"]:
        pass
    else:
        print("Please Enter Correct input")
        Tmux()
        return

    print(f"Connecting {module}")
    run(f"stow {module}",shell=True)

