from subprocess import run
from utils.functions import install_module
import inquirer


def shell():
    """
    Prompt the user to select a shell and link it if desired.
    """
    shell_choices = ["bash", "zsh", "both"]
    shell_question = [inquirer.List(
        "shell",
        message="Select Shell",
        choices=shell_choices,
    )]
    selected_shell = inquirer.prompt(shell_question)["shell"]

    if selected_shell != "bash":
        install_module("zsh")

        switching_question = [inquirer.List(
            "switch",
            message="Do you want to switch to zsh?",
            choices=["yes", "no"],
        )]

        if inquirer.prompt(switching_question)["switch"] == "yes":
            run("chsh -s $(which zsh)", shell=True)
            print("After this setup is complete, please log out and log back in to see changes")

    link_question = [
        inquirer.List(
            "link",
            message=f"Do you want to link {selected_shell}?",
            choices=["yes", "no"],
        )
    ]
    link_desired = inquirer.prompt(link_question)["link"]

    if link_desired == "yes":
        if selected_shell == "both":
            run("stow zsh", shell=True)
            run("stow bash", shell=True)
        else:
            run(f"stow {selected_shell}", shell=True)


if __name__ == "__main__":
    shell(  )