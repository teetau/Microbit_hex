# 03_04_kirkastuva_kuva.py
from microbit import *

teho = 0

while True:
    if button_a.was_pressed():
        for kirkkaus in range(10):
            for x in range(5):
                display.set_pixel(x, x, kirkkaus)
                sleep(50)
    if button_b.was_pressed():
        display.show("a")
