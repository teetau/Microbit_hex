# 01_06_kompassi.py
from microbit import *
# kalibroidaan kompassi kallistelemalla
compass.calibrate()
while True:
    suunta = compass.heading()
    display.scroll(suunta)
    sleep(500)
