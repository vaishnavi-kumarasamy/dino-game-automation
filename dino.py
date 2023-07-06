import pyautogui as p
import time

time.sleep(5)
while True:
    x,y = p.position() ## x, y = (1000, 500)
    color_val = (p.pixel(x,y))
    if(color_val[0]!=255 and color_val[1]!=255 and color_val[2]!=255):
        p.press('space')

