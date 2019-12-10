from microbit import *
import random

while True:
    noppa = random.randint(1, 6)
    asento = accelerometer.current_gesture()
    if asento == "shake":
        display.show(noppa)
