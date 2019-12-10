from microbit import *
# 03_nimikyltti.py
while True:
    if button_a.was_pressed():
        display.scroll("Teemu")
    elif button_b.was_pressed():
        for i in range(0, 8):
            display.show(Image.HEART)
            sleep(400)
            display.show(Image.HEART_SMALL)
            sleep(400)
        display.clear()
