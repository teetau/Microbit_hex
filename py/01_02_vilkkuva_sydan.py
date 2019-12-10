# 01_02_vilkkuva_sydan.py
from microbit import *
# luodaan sydänkuvia eri kirkkauksilla
heart1 = Image("09090:""99999:""99999:""09990:""00900:")
heart2 = Image("07070:""77777:""99999:""09990:""00900:")
heart3 = Image("05050:""55555:""77777:""07770:""00700:")
heart4 = Image("03030:""33333:""55555:""05550:""00500:")
heart5 = Image("01010:""11111:""33333:""03330:""00300:")
heart6 = Image("00000:""00000:""00000:""00000:""00000:")
# tehdään lista (animaatio), jossa on kaikki sydänkuvat
animaatio = [heart1, heart2, heart3, heart4, heart5, heart6]
# näytetään animaatio, välissä 200ms tauko ja ikuisesti-luuppi
display.show(animaatio, loop=True, delay=200)