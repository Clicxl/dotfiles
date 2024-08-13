from subprocess import run
from utils.functions import install_module
import inquirer

def Multiplexer():

    plexer_choices = ["tmux", "zellij", "both"]
    plexer = [inquirer.List(
        "plexer",
        message="Select Terminal Multiplexer",
        choices=plexer_choices,
    )]
    plexer_choices = inquirer.prompt(plexer)["plexer"]

    # Install the module if it is not already installed
    install_module(plexer_choices,["tmux", "zellij"])

    # Prompt the user to decide whether to link the terminal multiplexer module
    link_question = [
        inquirer.List(
            "link",
            message=f"Do you want to link {plexer_choices}?",
            choices=["yes", "no"],
        )
    ]
    link_desired = inquirer.prompt(link_question)["link"]

    # If the user wants to link and both are selected, link both tmux and zellij
    if link_desired == "yes":

        if plexer_choices == "both":
            print("Linking both tmux and zellij")
            run("stow tmux", shell=True)
            run("stow zellij", shell=True)

        # If the user wants to link and a single plexer is selected, link the selected plexer
        else:
            print(f"Linking {plexer_choices}")
            run(f"stow {plexer_choices}", shell=True)
