from subprocess import run


def Bash():
    module = "bash"

    want = input(f"Do you want to Install {module}: (y/n) ")

    if want.lower() in ["y", "yes"]:
        print(f"Connecting {module}")
        run(f"stow {module}", shell=True)

    elif want.lower() in ["n", "no"]:
        pass
    else:
        print("Please Enter Correct input")
        Bash()
        return
