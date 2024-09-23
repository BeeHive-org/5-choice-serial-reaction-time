''' This progran tests the servo motor to run the full range 180. 
Its a simple implimentation when the exact angle is not required.
From the datasheet servo motor processes instruction at a speed of
20ms which is 50Hz.
If the instruction is ON for 0.5ms it moves to the least angle 45
and at 2ms it moves to angle 225. this is a range of 180 degrees'''

from machine import Pin,PWM
import time

sg90 = PWM(Pin(18),freq =50)

# 0.5ms/20ms = 0.025 = 2.5% duty cycle
# 2.4ms/20ms = 0.12 = 12% duty cycle

# 0.025*1024=25.6
# 0.12*1024=122.88
x = 0;
while x<1:
    sg90.duty(23)
    time.sleep(1)
    sg90.duty(123)
    time.sleep(1)
    x+=1