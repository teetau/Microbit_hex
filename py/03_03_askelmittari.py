# 03_03_askelmittari.py
from microbit import *

askeleet = 0

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    # herkkyys -> muuta x arvoa
    if x > 500 and y > 500:
        askeleet = askeleet + 1
        sleep(100) 
    elif button_a.was_pressed():
        display.show(askeleet)
        sleep(500)
        display.clear()