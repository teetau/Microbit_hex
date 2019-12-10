# 02_03_virtuaalilemmikki.py
from microbit import *

while True:
    # kun a-nappia painetaan...
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        # kun b-nappia painetaan...
    elif button_b.is_pressed():
        break
    # muuten näytä ...
    else:
        display.show(Image.SAD)
display.clear()