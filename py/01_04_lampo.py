# 01_04_lampo.py
from microbit import *

# kaikki loopin sisään, jotta lämpötilaa tarkistetaan koko ajan.
while True:
    # luodaan muuttuja lampo
    lampo = temperature()
    # Näytetään muuttujan arvo
    display.scroll(lampo)
    sleep(500)