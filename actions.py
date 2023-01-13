from time import sleep as sleep
import pyautogui as p
import os

button_buffer = 0, 0


def openSteam():
    sleep(1)
    os.startfile(r"C:\Users\Maxim\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User "
                 r"Pinned\TaskBar\Steam.lnk")
    sleep(1)


def openWE():
    sleep(1)
    os.startfile(r"C:\Users\Maxim\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Wallpaper Engine.url")
    sleep(1)


def click(x, y):
    sleep(1)
    p.click(x, y)
    sleep(1)


def rclick(x, y):
    sleep(1)
    p.rightClick(x, y)
    sleep(1)


def ctrlA():
    sleep(1)
    p.hotkey('ctrl', 'a')
    sleep(1)


def subAll(x, y):
    sleep(1)
    ctrlA()
    rclick(x, y)
    sleep(1)
    p.move(50, 15)
    sleep(1)
    p.click()


def unsubscribe():
    sleep(1)
    button = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\unsubscribe.png")
    p.leftClick(button)
    sleep(1)
    button = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\ok_confirm.png")
    p.click(button)
    sleep(1)


def clear():
    sleep(1)
    button = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\clear.png")
    if button is not None:
        p.leftClick(button)
    else:
        pass
    sleep(1)

def closeSteam():
    sleep(1)
    os.system('taskkill /f /im steam.exe')
    sleep(1)

def discover():
    sleep(1)
    button = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\discover.png")
    p.leftClick(button)
    sleep(1)


def installed():
    sleep(1)
    button = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\installed.png")
    p.click(button)
    sleep(1)


def configure():
    sleep(2)
    button = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\configure.png")
    sleep(1)
    p.click(button)


def changeWhilePausedInConfigure():
    sleep(1)
    button = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\allow_change_while_paused.png")
    if button is not None:
        pass
    else:
        p.click(1030, 300)
        sleep(1)
    p.click(1193, 472)
    sleep(1)


def closeOkButton():
    sleep(1)
    p.click(1750,1012)
    sleep(1)


def secondIsAllTime():
    Found = False
    button = p.locateOnScreen(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\all_time.png")
    wallpaperCoords = button[0] + 75, button[1] + 75
    if button is not None:
        Found = True
        p.moveTo(wallpaperCoords)
        sleep(1)
        p.click(wallpaperCoords)
        sleep(1)
    else:
        pass
    sleep(3)
    return Found


def scroll():
    p.sleep(1)
    p.click(1309, 433)  # neutral position
    p.sleep(1)
    p.scroll(-400)
    p.sleep(1)


def nextWall():
    closeOkButton()
    sleep(5)
    p.hotkey('shiftleft', 'f5')
    sleep(1)
