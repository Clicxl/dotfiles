import pyautogui
from datetime import date


class Utils:
    def __init__(self) -> None:
        self.WIDTH, self.HEIGHT = pyautogui.size()

    def mousePos(self):
        print(pyautogui.position())

    def shotMatch(self,file: str,grayscale:bool=False,click:bool=False):
        try:
            if pyautogui.locateOnScreen(file):
                print(f"{file} Located")
                if click:
                    pyautogui.click(pyautogui.locateCenterOnScreen(file,grayscale=grayscale))

                return True, pyautogui.locateCenterOnScreen(file, grayscale=grayscale)
            
        except Exception as e:
            print(f"{file} Not Located")
            return False

    def comapreDate(self,prevDate: date):
        return (date.today() - prevDate).days