#PHASE 1 ESP32

#T1 PHASE ESP32 is used currently as a circuit board for the SENSOR of the box:
                #It replaces the bottons 

#THIS WORKS WITH REAL SENSORS AND LEDs.
import machine
import utime
import random
from board_serial import *

#T1 PHASE:
    #1. Use 3 lights and 3 buttons to mark the NP
    #2 When 1/3 button is pressed --> All lights turn off and food dispenser is on
    #Mouse collects food
    #Again but with the time interval



def food_training():
    led=machine.Pin(14, machine.Pin.OUT) #LED WORKS
    button_food=machine.Pin(15,machine.Pin.IN)


    timer_starts =utime.ticks_ms()
    #now=button_food.value(1)


    NP_1=machine.Pin(26,machine.Pin.OUT)
    NP_2=machine.Pin(25,machine.Pin.OUT)
    NP_3=machine.Pin(22,machine.Pin.OUT)
    NP_4=machine.Pin(23,machine.Pin.OUT)
    NP_5=machine.Pin(18,machine.Pin.OUT)

    button_1 = machine.Pin(2,machine.Pin.IN)
    button_2 = machine.Pin(16,machine.Pin.IN) #pin 4
    button_3 = machine.Pin(17,machine.Pin.IN)
    #button_4 = machine.Pin(4,machine.Pin.IN)



    NP_1.value(0)
    NP_2.value(0)
    NP_3.value(0)
    NP_4.value(0)
    NP_5.value(0)


    #button_pressed = False


    #print(button_food.value())

    #FOOD MAGAZINE:

    #Allows the test go for 50 turns
    #for x in range (1,50):
    for x in range (1,4):
        
        timer_start= utime.ticks_ms()
        #ITI
        #times=[4,8,16,32]
        times=[1,1.2,1.1]
        times_num = random.choice(times)
        
        #print (bytes("ITI "+str(times_num),'utf-8'))
        #print("ITI ", times_num) #All the times num are for the randomisation fo the lights   
        led.value(0)  #During this the LED of the food dispenser is off
        utime.sleep(times_num) # after this, the timer is silent
        led.value(1)
        # print(button_food.value())

        #print("Food is out") (comment out for data analysis)

        while button_food.value() == 1:
            #print(button_food.value())
            timer_food = utime.ticks_ms()
            #led.value(1)
            #print("uues")

        led.value(0)
        mouse_to_food = timer_food - timer_start
        
        addToData(datainput="Trial "+str(x))
        addToData(datainput="ITI "+str(times_num))
        addToData(datainput="M2F "+str(mouse_to_food))
        #print ("M2F "+str(mouse_to_food),'utf-8')
        #print("M2F ", mouse_to_food, "ms")
    print("END")
    addToData(M=0, datainput="END")

    



food_training()

