from utils import Utils,date,pyautogui,sleep

utils = Utils()

class Base:
    todayChallenges: list = []

    def __init__(self):
        if self.todayChallenges == []:
            self.todayChallenges = self.todayChal()
            self.header:str = ""
            self.footer:str = ""

    def todayChal(self):
        challenges:list = []
        for i in range(0, int(input("Enter No of Challenges: "))):
            challenges.append(str(input(f"Enter Challenge {i+1}: ")))
        return challenges

    def combinePost(self):
        midSection: str = ""
        challenges: list = self.todayChallenges
        for i in range(0, len(challenges)):
            midSection += f"- {challenges[i]} \n"

        Post: str = f"{self.header}\n{midSection}\n{self.footer}"
        return Post

    def vidSelector(self):
        sleep(1)
        # Explorer
        if utils.shotMatch("assets/video.png", True, True):
            sleep(1)
            if utils.shotMatch("assets/modified1.png", True):
                pyautogui.doubleClick(618, 119)
            elif utils.shotMatch("assets/modified2.png", True):
                pyautogui.click(utils.shotMatch("assets/modified2.png")[1])  # type: ignore
                pyautogui.doubleClick(618, 119)
            else:
                pyautogui.doubleClick(618, 119)
        else:
            pyautogui.doubleClick(618, 119)


class Twitter(Base):
    def __init__(self):
        super().__init__()
        self.header = f"""Day 0{utils.comapreDate(date(2024, 6, 7))} of #30DaysJS
Today's Challenge:"""

        self.footer = """Continuing to build and improve my JavaScript skills!
Thank you @wesbos

#learninpublic #javascript"""

    def construct(self):
        sleep(5)
        pyautogui.hotkey("ctrl", "t")
        pyautogui.write("https://twitter.com/compose/post")
        pyautogui.hotkey("enter")
        sleep(10)
        pyautogui.write(self.combinePost(),interval=0.08)
        sleep(1)
        if utils.shotMatch("assets/Twitter/upload.png", True):
            pyautogui.doubleClick(utils.shotMatch("assets/Twitter/upload.png", True)[1]) #type: ignore
            self.vidSelector()


class LinkedIn(Base):
    def __init__(self):
        super().__init__()
        self.header = f"""🚀 Day 0{utils.comapreDate(date(2024,6,7))} of hashtag#30DaysJS
# Today's Challenge:"""

        self.footer = """Continuing to build and improve my JavaScript skills!

# hashtag#learninpublic hashtag#javascript
# Project Source Code: https://lnkd.in/e4PR9jCz"""

    def construct(self):
        sleep(2)
        pyautogui.hotkey("ctrl", "t")
        pyautogui.write("https://www.linkedin.com/feed/")
        pyautogui.press("enter")
        sleep(30)

        pyautogui.click(951, 215)
        sleep(3)
