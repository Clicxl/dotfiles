from subprocess import run


def commandExists(command:str):
  if run(f"{command} -v", shell=True, capture_output=True, text=True) != "":
    return True

  return False
