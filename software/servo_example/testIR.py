
import time 
import random
import utime
from machine import Pin, PWM
from servo import Servo

servo1 = PWM(Pin(12, mode=Pin.OUT))
sg90.freq(50)

button_food=Pin(2,Pin.IN)
button_food1=Pin(15,Pin.IN)
cycles=10000


counter1=0
while counter1<cycles:
    pellet = button_food.value()
    pellet1 = button_food1.value()
    print(pellet)
    print(pellet1)
    time.sleep(0.010)
    counter1=counter1+1