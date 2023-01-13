from time import sleep as sleep
import complex as c, actions as a, pyautogui as p
import test as t


def mainMacro():
    a.openSteam()
    sleep(40)
    a.openWE()  # open wallpaper engine
    sleep(40)
    wallpapers_current = t.ocr()
    a.clear()  # clear playlist
    sleep(5)
    a.discover()  # discover tab
    sleep(35)  # wait for Steam to respond
    a.click(170, 252)  # click first wallpaper (New approved wallpapers)
    sleep(3)
    c.downloadNewApproved()
    a.scroll()
    if a.secondIsAllTime():
        c.downloadAllTimeClassic()
    else:
        pass
    c.createPlaylist()
    wallpapers_new = t.ocr()
    print("+" + str(wallpapers_new - wallpapers_current) + " new wallpapers")
    print(str(wallpapers_current) + " wallpapers in playlist")
    a.nextWall()
    a.closeSteam()


mainMacro()
