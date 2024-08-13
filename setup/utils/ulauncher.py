from subprocess import run
from utils.functions import commandExists
import inquirer

def Ulauncher():
    module = "ulauncher"

    if not commandExists(module):
            print(f"Installing {module}")

            run("sudo add-apt-repository universe -y", shell=True)
            run("sudo add-apt-repository ppa:agornostal/ulauncher -y", shell=True)
            run("sudo nala update", shell=True)
            run("sudo nala install ulauncher", shell=True)


    # Prompt the user to decide whether to link the ulauncher module
    link_question = [
        inquirer.List(
            "link",
            message=f"Do you want to link {module}?",
            choices=["yes", "no"],
        )
    ]
    link_desired = inquirer.prompt(link_question)["link"]

    # If the user chooses to link it, link the ulauncher module
    if link_desired == "yes":
        print(f"Linking {module}")
        run(f"stow --adopt {module}", shell=True)


