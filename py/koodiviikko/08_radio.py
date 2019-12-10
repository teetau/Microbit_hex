# 08_radio.py
from microbit import *
import radio
# radio päälle
radio.on()
# valitaan kanava (0-100)
radio.config(channel=7)
while True:
    asento = accelerometer.current_gesture()
    if asento == "left":
        radio.send("0")
    if asento == "right":
        radio.send("1")
    viesti = radio.receive()
    if viesti == "0":
        display.show(Image.ARROW_W)
    if viesti == "1":
        display.show(Image.ARROW_E)
