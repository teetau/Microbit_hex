# 03_05_kertolaskukone.py
from microbit import *

kertoja = 0
kerrottava = 0

while True:
    tarkistus = accelerometer.current_gesture()
    tulo = kertoja * kerrottava
    if button_a.was_pressed():
        kertoja = kertoja + 1
        display.show(kertoja)
    elif button_b.was_pressed():
        kerrottava = kerrottava + 1
        display.show(kerrottava)
    elif tarkistus =="shake":
        display.clear()
        sleep(100)
        display.scroll(tulo)
        