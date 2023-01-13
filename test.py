import pyautogui as p
import cv2
import pytesseract
import numpy as np
import time
import re


def coords():
    p.mouseInfo()


def ocr():
    p.screenshot(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\screenshot.png", region=(0, 860, 250, 50))
    img = cv2.imread(r"C:\Users\Maxim\Desktop\Projects\Python\WEDownloader\screenshot.png")
    # Alternatively: can be skipped if you have a Blackwhite image
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Maxim\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    out_below = pytesseract.image_to_string(img)
    out_below = re.sub('[^0-9]', '', out_below)
    out_below = int(out_below)
    return out_below
