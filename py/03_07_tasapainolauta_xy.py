# 03_07_tasapainolauta_xy.py
# luetaan x ja y-akselin arvoja
# ja näytetään ruudulla arvon mukainen merkki (nuoli)
# luodaan muuttuja "lukemax" ja "lukemay" johon arvoja kirjoitetaan koko ajan
from microbit import *
while True:
    lukemax = accelerometer.get_x()
    lukemay = accelerometer.get_y()
    # kallistukset kulmiin
    if lukemax > 20 and lukemay < -20:
        display.show(Image.ARROW_NE)
    elif lukemax > 20 and lukemay > 20:
        display.show(Image.ARROW_SE)
    elif lukemax < -20 and lukemay < -20:
        display.show(Image.ARROW_NW)
    elif lukemax < -20 and lukemay > 20:
        display.show(Image.ARROW_SW)
    elif lukemax > 20 and lukemay > -20 and lukemay < 20:
        display.show(Image.ARROW_E)
    elif lukemax < -20 and lukemay > -20 and lukemay < 20:
        display.show(Image.ARROW_W)
    elif lukemax > -20 and lukemax < 20 and lukemay < -20:
        display.show(Image.ARROW_N)
    elif lukemax > -20 and lukemax < 20 and lukemay > 20:
        display.show(Image.ARROW_S)
    else:
        display.clear()