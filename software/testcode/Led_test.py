from machine import Pin
from time import sleep

led1 = Pin(23,Pin.OUT)
led2 = Pin(14,Pin.OUT)
led3 = Pin(27,Pin.OUT)
led4 = Pin(26,Pin.OUT)
led5 = Pin(25,Pin.OUT)
led6 = Pin(32,Pin.OUT)
led7 = Pin(33,Pin.OUT)

while True:
    led1.value(not led1.value())
    led2.value(not led2.value())
    led3.value(not led3.value())
    led4.value(not led4.value())
    led5.value(not led5.value())
    led6.value(not led6.value())
    led7.value(not led7.value())
    
    sleep(0.5)
