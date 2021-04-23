import mss
import numpy as np
import cv2
import pyautogui
import time
import keyboard

def take_screenshot():
    with mss.mss() as sct:
        filename = sct.shot(output='fullscreen.png')
    return filename
take_screenshot()

def get_frame(region):
    with mss.mss() as sct:
        screen = np.asarray(sct.grab(region))
        screen_grayscale = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        print(screen_grayscale.shape)
        cv2.imwrite("region.png",screen_grayscale)
    return screen_grayscale
region = {"top": 440, "left": 75, "width": 100, "height": 30}
frame = get_frame(region)
print(frame.shape)
