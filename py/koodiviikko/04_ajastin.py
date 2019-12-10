from microbit import *
# 04_ajastin.py
sekunnit = 0
while True:
    asento = accelerometer.current_gesture()
    if asento == "shake":
        sekunnit = 0
        display.show(sekunnit)
    elif button_a.was_pressed():
        sekunnit = sekunnit + 1
        display.show(sekunnit)
    elif button_b.was_pressed():
        while sekunnit > 0:
            display.show(sekunnit)
            sleep(1500)
            sekunnit = sekunnit - 1
        display.clear()
