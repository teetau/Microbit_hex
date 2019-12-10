# 02_05_kps.py
from microbit import *
import random

# luodaan kuvat
kivi = Image("00000:""09990:""09990:""09990:""00000:")
paperi = Image("99999:""99999:""99999:""99999:""99999:")
sakset = Image("99009:""99090:""00900:""99090:""99009:")
# luodaan muuttuja ja annetaan sille arvo 0 nyt aluksi
heitto = 0
while True:
    if button_a.was_pressed():
        heitto = random.randint(1, 3)
        if heitto == 1:
            display.show(kivi)
        elif heitto == 2:
            display.show(paperi)
        else:
            display.show(sakset)