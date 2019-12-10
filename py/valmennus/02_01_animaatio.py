# 02_01_animaatio.py
from microbit import *

# luodaan kuvasarja tippuvasta kuutiosta
kuva1 = Image("90000:""00000:""00000:""00000:""00000:")
kuva2 = Image("99000:""99000:""00000:""00000:""00000:")
kuva3 = Image("00000:""09900:""09900:""00000:""00000:")
kuva4 = Image("00000:""00000:""00990:""00990:""00000:")
kuva5 = Image("00000:""00000:""00000:""00099:""00099:")
kuva6 = Image("00000:""00000:""00000:""00000:""00009:")
# tehdään lista (animaatio), jossa on kaikki sydänkuvat
animaatio = [kuva1, kuva2, kuva3, kuva4, kuva5, kuva6]

risti = Image("00000:""00900:""09090:""00900:""00000:")
salmiakki = Image("00900:""09090:""90009:""09090:""00900:")
nelio = Image("99999:""90009:""90009:""90009:""99999:")

animaatio2 = [risti, salmiakki, nelio, salmiakki, risti]


while True:
    if button_a.was_pressed():
        # näytetään animaatio, välissä 100ms tauko
        display.show(animaatio, loop=False, delay=100)
        display.clear()
    elif button_b.was_pressed():
        display.show(animaatio2, loop=False, delay=150)
        display.clear()