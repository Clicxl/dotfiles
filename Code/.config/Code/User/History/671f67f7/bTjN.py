from pyautogui import confirm #type: ignore
from models import Twitter,LinkedIn,Base
from sys import exit

if __name__ == "__main__":
    Base().todayChal(Base)
    print(Base.)
    while True:
        whichPost:str = confirm(text="Which Media Do you want To Post?",title="Post",buttons=['Twitter','LinkedIn','Quit'])

        if whichPost == "LinkedIn":
            linkedin = LinkedIn()
        elif whichPost == "Twitter":
            twitter = Twitter()
        elif whichPost == 'Quit':
            exit()
