# 02_04_ajastin.py
from microbit import *

sekunnit = 0
while True:
    asento = accelerometer.current_gesture()
    if button_a.was_pressed():
        sekunnit = sekunnit + 1
        display.show(sekunnit)
    elif button_b.was_pressed():
        while sekunnit > 0:
            display.show(sekunnit)
            sleep(1000)
            sekunnit = sekunnit - 1
        display.clear()
    elif asento == "shake":
        sekunnit = 0
        display.show(sekunnit)