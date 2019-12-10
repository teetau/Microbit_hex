# 06_valo_lampo.py
from microbit import *
while True:
    lampo = temperature()
    valo = display.read_light_level()
    if button_a.was_pressed():
        display.scroll(lampo)
    if button_b.was_pressed():
        display.scroll(valo)
