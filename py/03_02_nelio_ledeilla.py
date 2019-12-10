# 03_02_nelio_ledeilla.py
from microbit import *

while True:
    asento = accelerometer.current_gesture()
    if button_a.was_pressed():
        # sytytetään kaikki ylärivin ledit
        for x in range(5):
            # x saa arvot 0,1,2,3,4
            display.set_pixel(x, 0, 9)
            # pieni tauko väliin, jotta syttyvät vaiheittain
            sleep(100)
        sleep(500)
        # oikean reunan ledit ylhäältä alas
        for y in range(5):
            # y saa arvot 0,1,2,3,4
            display.set_pixel(4, y, 9)
            # pieni tauko väliin, jotta syttyvät vaiheittain
            sleep(100)
        sleep(500)
        # alareuna oikealta vasemmalle
        for x in range(4, -1, -1):
            # x saa arvot 4, 3, 2, 1, 0
            display.set_pixel(x, 4, 9)
            # pieni tauko väliin, jotta syttyvät vaiheittain
            sleep(100)
        sleep(500)
        # vasen reuna alhaalta ylös
        for y in range(4, -1, -1):
            # y saa arvot 4, 3, 2, 1, 0
            display.set_pixel(0, y, 9)
            # pieni tauko väliin, jotta syttyvät vaiheittain
            sleep(100)
    if asento == "shake":
        display.clear()