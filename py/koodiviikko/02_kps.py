from microbit import *
# kivi - paperi - sakset

import random
# luodaan kuvat
kivi = Image("00000:""09990:""09990:""09990:""00000:")
paperi = Image("99999:""99999:""99999:""99999:""99999:")
sakset = Image("99009:""99090:""00900:""99090:""99009:")
# tehdään lista kuvista
kuvat = [kivi, paperi, sakset]
# ikuisesti - luuppi
while True:
    asento = accelerometer.current_gesture()
    if asento == "shake":
        display.show(random.choice(kuvat))
