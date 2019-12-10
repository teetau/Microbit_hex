# 01_03_noppa.py
from microbit import *
import random
# Arvotaan satunnaisluku välillä 1-6
# muutetaan numero merkeiksi (str)
display.show(str(random.randint(1, 6)))