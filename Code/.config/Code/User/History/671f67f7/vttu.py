import pyautogui as pag
from time import sleep
from datetime import date

WIDTH, HEIGHT = pag.size()


def mousePos():
    print(pag.position())


def comapreDate(prevDate: date):
    return (date.today() - prevDate).days


def shotMatch(file: str):
    try:
        if pag.locateOnScreen(file):
            print(f"{file} Located")
            return True, pag.center(pag.locateOnScreen(file))
    except:
        print(f"{file} Not Located")
        return False


def todayChal():
    challenges = []
    for i in range(0, int(input("Enter No of Challenges: "))):
        challenges.append(str(input(f"Enter Challenge {i+1}: ")))
    return challenges


def combinePost(header: str, footer: str, middle:list):
    midSection: str = ""
    challenges: list = middle
    for i in range(0, len(challenges)):
        midSection += f"- {challenges[i]} \n"

    Post: str = header + midSection + footer
    return Post


TWHeader: str = f"""Day 0{comapreDate(date(2024, 6, 7))} of #30DaysJS
Today's Challenge: \n"""
TWFooter = """\nContinuing to build and improve my JavaScript skills!
Thank you @wesbos

#learninpublic #javascript"""

LIHeader = f"""🚀 Day 0{comapreDate(date(2024,6,7))} of hashtag#30DaysJS
Today's Challenge:\n"""
LIFooter = """"\nContinuing to build and improve my JavaScript skills!

hashtag#learninpublic hashtag#javascript
Project Source Code: https://lnkd.in/e4PR9jCz"""

todayChallenges:list = todayChal()

TWPostDetails = combinePost(TWHeader, TWFooter , todayChallenges)
LIPostDetails = combinePost(LIHeader,LIFooter, todayChallenges)

def twitterCreate():
    sleep(5)
    pag.hotkey("ctrl", "t")
    pag.write("https://twitter.com/compose/post")
    pag.press("enter")
    sleep(10)
    pag.write(TWPostDetails)
    sleep(3)

    # Gif Loader
    if shotMatch("assets/upload.png"):
        pag.doubleClick(shotMatch("assets/upload.png")[1])
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


# twitterCreate()
# mousePos()
