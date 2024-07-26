from pyautogui import confirm #type: ignore
from models import Twitter,LinkedIn
from sys import exit

if __name__ == "__main__":

    whichPost:str = confirm(text="Which Media Do you want To Post?",title="Post",buttons=['Twitter','LinkedIn','Quit'])

    if whichPost == "LinkedIn":
        linkedin = LinkedIn()
    elif whichPost == "Twitter":
        twitter = Twitter()
    elif whichPost == 'Quit':
        exit()
