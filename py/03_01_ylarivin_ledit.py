# 03_01_ylarivin_ledit.py
from microbit import *

while True:
    if button_a.was_pressed():
        # sytytetään kaikki ylärivin ledit
        for x in range(5):
            # x saa arvot 0,1,2,3,4
            display.set_pixel(x, 0, 9)
            # pieni tauko väliin, jotta syttyvät vaiheittain
            sleep(100)
        sleep(500)
        for x in range(4, -1, -1):
            # x saa arvot 4,3,2,1,0 ja kirkkaus 0 eli sammuu
            display.set_pixel(x, 0, 0)
            # pieni tauko väliin, jotta syttyvät vaiheittain
            sleep(100)
    if button_b.was_pressed():
        display.show(Image.ARROW_W)
        sleep(500)
        display.clear()
