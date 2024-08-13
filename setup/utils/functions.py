from subprocess import run
import inquirer

def commandExists(command:str):
  if run(f"which {command}", shell=True, capture_output=True) != f"{command} not found":
    return True
  return False

def install_module(module_name: str, module_list=None) -> None:
    """
    Install the given module if it is not already installed.

    Args:
        module_name (str): The name of the module to install.
    """

    if module_name == "both" and module_list is not None:
        for module in module_list:
            install_command = f"sudo nala install {module}"
            run(install_command, shell=True)

    if not commandExists(module_name):
        install_command = f"sudo nala install {module_name}"
        run(install_command, shell=True)
    else:
        print(f"{module_name} is already installed")


def link_module(module: str) -> None:
    """
    Install and link the given module.

    This function checks if the given module is already installed. If not, it installs it.
    Then, it prompts the user to decide whether to link the given module.
    If the user chooses to link it, the function runs the appropriate command to stow the given module.
    """

    # Install the module if it is not already installed
    install_module(module)

    # Prompt the user to decide whether to link the given module
    link_question = [
        inquirer.List(
            "link",
            message=f"Do you want to link {module.capitalize()}?",
            choices=["yes", "no"],
        )
    ]
    link_desired = inquirer.prompt(link_question)["link"]

    # If the user chooses to link it, link the given module
    if link_desired == "yes":
        print(f"Linking {module}")
        if module in ['code', 'nvim']:
            run(f"stow --adopt {module}", shell=True)
        else :
           run(f"stow {module}", shell=True)
