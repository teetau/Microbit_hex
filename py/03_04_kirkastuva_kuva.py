# 03_04_kirkastuva_kuva.py
from microbit import *

heart1 = Image("02020:""22222:""22222:""02220:""00200:")
heart2 = Image("04040:""44444:""44444:""04440:""00400:")
heart3 = Image("06060:""66666:""66666:""06660:""00600:")
heart4 = Image("07070:""77777:""77777:""07770:""00700:")
heart5 = Image("08080:""88888:""88888:""08880:""00800:")
heart6 = Image("09090:""99999:""99999:""09990:""00900:")

kirkastuva = [heart1, heart2, heart3, heart4, heart5, heart6]

while True:
    if button_a.was_pressed():
        # kirkkaus kasvaa 0-9
        for kirkkaus in range(10):
            for x in range(5):
                display.set_pixel(x, x, kirkkaus)
                sleep(50)
        display.clear()
    if button_b.was_pressed():
        for x in range(5):
            display.show(kirkastuva)
            sleep(100)
            display.clear()