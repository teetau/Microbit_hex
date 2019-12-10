# 02_02_vatupassi.py
from microbit import*

while True:
    asento = accelerometer.current_gesture()
    if asento == "left":
        display.show(Image.ARROW_W)
    elif asento == "right":
        display.show(Image.ARROW_E)
    else:
        display.show("-")