import pyautogui as pag
from time import sleep
from models import Twitter, Utils


LIHeader = f"""🚀 Day 0{comapreDate(date(2024,6,7))} of hashtag#30DaysJS
# Today's Challenge:\n"""
LIFooter = """\nContinuing to build and improve my JavaScript skills!

# hashtag#learninpublic hashtag#javascript
# Project Source Code: https://lnkd.in/e4PR9jCz"""


def linkedinCreate():
    LIPostDetails = combinePost(LIHeader, LIFooter, todayChallenges)
    sleep(5)
    pag.hotkey("ctrl", "t")
    pag.write("https://www.linkedin.com/feed/")
    pag.press("enter")
    sleep(30)
    pag.click(951, 215)
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
            pag.click(1514, 942)
            sleep(2)
    pag.write(LIPostDetails)


# twitterCreate()
# mousePos()

if __name__ == "__main__":
    twitter = Twitter()
    twitter.construct()
