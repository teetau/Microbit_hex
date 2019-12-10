from microbit import *
# 05_vatupassi.py
while True:
    x = accelerometer.get_x()
    if x > 20:
        display.show(Image.ARROW_E)
    if x < -20:
        display.show(Image.ARROW_W)
    if x >= -20 and x <= 20:
        display.show("--")
