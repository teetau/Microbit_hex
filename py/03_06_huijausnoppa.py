# 03_06_huijausnoppa.py
from microbit import *
import random

# tehdään kaksi muuttujaa
huijaus = random.randint(1, 2)
numero = random.randint(1, 6)

# ohjelma tarkkailee muuttujaa "huijaus"
# huijataanko (1) vai ei (2)
# muuten näytetään satunnaisluku 1-6

while True:
    if huijaus == 1:
        display.show("6")
    else:
        display.show(numero)

