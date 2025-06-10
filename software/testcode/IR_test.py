from machine import Pin
from machine import ADC
from time import sleep

# Ir1 = Pin(15,Pin.IN)#
# Ir2 = Pin(16,Pin.IN,Pin.PULL_DOWN)#
# Ir3 = Pin(2,Pin.IN) #np 2 from right
# Ir4 = Pin(17,Pin.IN,Pin.PULL_DOWN)#
# Ir5 = Pin(19,Pin.IN)#
# Ir6 = Pin(21,Pin.IN)#
# Ir7 = Pin(22,Pin.IN)#np most right
Ir8 = Pin(12,Pin.IN)#
#Ir8 = ADC(12)

while True:
#     print("Rx1",Ir1.value())
#     print("Rx2",Ir2.value())
#     print("Rx3",Ir3.value())
#     print("Rx4",Ir4.value())
#     print("Rx5",Ir5.value())
#     print("Rx6",Ir6.value())
#     print("Rx7",Ir7.value())
    print("Rx8",Ir8.value())
    #print("Rx8",Ir8.read_u16())
    sleep(1)