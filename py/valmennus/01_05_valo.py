# 01_05_valo.py
from microbit import *

# kaikki loopin sisään, jotta valon määrää tarkistetaan koko ajan
while True:
    # luetaan valon määrää ja asetetaan se muuttujan arvoksi
    valo = display.read_light_level()
    display.scroll(valo)
    sleep(500)