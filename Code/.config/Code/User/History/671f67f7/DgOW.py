import pyautogui as pag
from time import sleep
from datetime import date
from utils import Utils
from models import *

WIDTH, HEIGHT = pag.size()



def comapreDate(prevDate: date):
    return (date.today() - prevDate).days







TWHeader: str = f"""Day 0{comapreDate(date(2024, 6, 7))} of #30DaysJS
Today's Challenge: \n"""
TWFooter = """\nContinuing to build and improve my JavaScript skills!
Thank you @wesbos

#learninpublic #javascript"""

LIHeader = f"""🚀 Day 0{comapreDate(date(2024,6,7))} of hashtag#30DaysJS
Today's Challenge:\n"""
LIFooter = """\nContinuing to build and improve my JavaScript skills!

hashtag#learninpublic hashtag#javascript
Project Source Code: https://lnkd.in/e4PR9jCz"""

todayChallenges:list = todayChal()


def twitterCreate():

    TWPostDetails = combinePost(TWHeader, TWFooter , todayChallenges)
    sleep(5)
    pag.hotkey("ctrl", "t")
    pag.write("https://twitter.com/compose/post")
    pag.press("enter")
    sleep(10)
    pag.write(TWPostDetails)
    sleep(3)

    # Gif Loader
    if shotMatch("assets/Twitter/upload.png"):
        pag.doubleClick(shotMatch("assets/Twitter/upload.png")[1])
        sleep(2)
        # Explorer
        if shotMatch("assets/video.png"):
            pag.click(shotMatch("assets/video.png")[1])
            sleep(1)
            if shotMatch("assets/modified1.png"):
                pag.doubleClick(618, 119)
            elif shotMatch("assets/modified2.png"):
                pag.click(shotMatch("assets/modified2.png")[1])
                pag.doubleClick(618, 119)

            pag.doubleClick(618, 119)


def linkedinCreate():
    LIPostDetails = combinePost(LIHeader,LIFooter, todayChallenges)
    sleep(5)
    pag.hotkey("ctrl", "t")
    pag.write("https://www.linkedin.com/feed/")
    pag.press("enter")
    sleep(30)
    pag.click(951,215)
    sleep(3)

    # Gif Picker
    if shotMatch("assets/Linkedin/upload.png"):
        pag.click(shotMatch("assets/Linkedin/upload.png")[1])
        sleep(2)

        # Explorer
        if shotMatch("assets/video.png"):
            pag.click(shotMatch("assets/video.png")[1])
            sleep(1)
            if shotMatch("assets/modified1.png"):
                pag.doubleClick(618, 119)
            elif shotMatch("assets/modified2.png"):
                pag.click(shotMatch("assets/modified2.png")[1])
                pag.doubleClick(618, 119)

            pag.doubleClick(618, 119)
            sleep(2)
            pag.click(1514,942)
            sleep(2)
    pag.write(LIPostDetails)



# twitterCreate()
# mousePos()
linkedinCreate()
