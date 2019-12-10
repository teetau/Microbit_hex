# 07_animaatio.py
from microbit import *
risti = Image("00000:""00900:""09090:""00900:""00000")
salmiakki = Image("00900:""09090:""90009:""09090:""00900")
nelio = Image("99999:""90009:""90009:""90009:""99999")
while True:
    if button_a.was_pressed():
        kirkkaus = 1
        for x in range(0, 5):
            display.set_pixel(x, 2, kirkkaus)
            sleep(50)
            display.set_pixel(x, 2, 0)
            kirkkaus = kirkkaus + 2
    if button_b.was_pressed():
        for i in range(0, 5):
            display.set_pixel(2, 2, 9)
            sleep(100)
            display.show(risti)
            sleep(100)
            display.show(salmiakki)
            sleep(100)
            display.show(nelio)
            sleep(100)
            display.show(salmiakki)
            sleep(100)
            display.show(risti)
            sleep(100)
            display.clear()
