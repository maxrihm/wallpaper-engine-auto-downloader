import actions as a
from time import sleep as sleep
import pyautogui as p


def createPlaylist():
    a.installed()
    a.click(170, 252)
    a.ctrlA()
    a.subAll(170, 252)
    a.configure()
    a.changeWhilePausedInConfigure()



def downloadNewApproved():
    sleep(2)
    subcribed = None
    subcribed = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\subscribe.png")
    if subcribed is not None:
        a.subAll(170, 252)
    else:
        a.unsubscribe()
        a.subAll(170, 252)
    sleep(75)  # download time


def downloadAllTimeClassic():
    sleep(2)
    button = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\all_time.png")
    wallpaperCoords = button[0] + 75, button[1] + 75
    subcribed = None
    subcribed = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\subscribe.png")
    if subcribed is not None:
        a.subAll(*wallpaperCoords)
    else:
        a.unsubscribe()
        a.subAll(*wallpaperCoords)
    sleep(25)  # download time
