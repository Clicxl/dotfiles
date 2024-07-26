from pyautogui import confirm
from models import Twitter,LinkedIn

if __name__ == "__main__":
    whichPost:str = confirm(text="Which Media Do you want To Post?",title="Post",buttons=['Twitter','LinkedIn'])

    if whichPost == "LinkedIn":


    twitter = Twitter()
    twitter.construct()
