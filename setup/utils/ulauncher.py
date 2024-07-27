from subprocess import run


def Ulauncher():
    module = "ulauncher"

    want = input(f"Do you want to Install {module}: (y/n) ")

    if want.lower() in ["y", "yes"]:
        print(f"Installing {module}")

        run("sudo add-apt-repository universe -y", shell=True)
        run("sudo add-apt-repository ppa:agornostal/ulauncher -y", shell=True)
        run("sudo nala update", shell=True)
        run("sudo nala install ulauncher", shell=True)

    elif want.lower() in ["n", "no"]:
        pass
    else:
        print("Please Enter Correct input")
        Ulauncher()
        return

    print(f"Connecting {module}")
    run(f"stow {module}",shell=True)

