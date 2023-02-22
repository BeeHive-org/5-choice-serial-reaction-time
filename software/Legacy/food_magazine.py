#PHASE 1 ESP32

#T1 PHASE ESP32 is used currently as a circuit board for the SENSOR of the box:
                #It replaces the bottons 

#THIS WORKS WITH REAL SENSORS AND LEDs.

import belay
from belay import Device
import time
import csv



#LED WORKS

class food_training(Device):

    @Device.setup
    def food_setup():
        
        import machine
        import utime
        import random

        from machine import Pin
        from time import sleep
        
        
        #IN1 = Pin(14, Pin.OUT)
        #IN2 = Pin(27, Pin.OUT)
        #IN3 = Pin(25, Pin.OUT)
        #IN4 = Pin(26, Pin.OUT)

        #pins = [IN1, IN2, IN3, IN4]


        #led = machine.Pin(15, machine.Pin.OUT) #LED WORKS
        
        #button_food=machine.Pin(22,machine.Pin.IN)
        #button_dispenser = machine.Pin(29, machine.Pin.IN)


        #NP_1=machine.Pin(17,machine.Pin.OUT)
        #NP_2=machine.Pin(16,machine.Pin.OUT)
        #NP_3=machine.Pin(19,machine.Pin.OUT)
        #NP_4=machine.Pin(21,machine.Pin.OUT)
        #NP_5=machine.Pin(2,machine.Pin.OUT)

        button_1 = machine.Pin(23,machine.Pin.IN)
        button_2 = machine.Pin(5,machine.Pin.IN) #pin 4
        button_3 = machine.Pin(18,machine.Pin.IN)
        button_4 = machine.Pin(4,machine.Pin.IN)
        button_5 = machine.Pin(28, machine.Pin.IN)
        
        

        button_correspondance = [ (button_1, "NP_1"), (button_2, "NP_2"), (button_3, "NP_3"), (button_4, "NP_4")] #(button_5,"NP_5")]



        NP_1.value(0)
        NP_2.value(0)
        NP_3.value(0)
        NP_4.value(0)
        NP_5.value(0)
        
        #Allows the test go for 50 turns
        #for x in range (1,50):
        
        timer_starts =utime.ticks_ms()
      
    @Device.task
    def food_magazine():
        i = 1
        for i in range (5):
            print(i)
            #ITI
            #times=[4,8,16,32]
            times=[1,1.2,1.1]
            times_num = random.choice(times)
                
            led.value(0)  #During this the LED of the food dispenser is off
            utime.sleep(times_num) # after this, the timer is silent
            
            #here put stepper motor in action
            sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
            maxseq=100
            counter=0
            while counter<maxseq:
                for step in sequence:
                    for j in range(len(pins)):
                        pins[j].value(step[j])
                        sleep(0.001)
                #print(counter)
                counter=counter+1
            while button_dispenser.value()==1:
                led.value(0)
                #print(button_dispenser.value())
                #utime.sleep(0.5)
            
                
               #food came down, led turns on 
            timer_food = utime.ticks_ms()
            led.value(1)           

            # print(button_food.value())

            #print("Food is out") (comment out for data analysis)

            while button_food.value() == 1:
                #print(button_food.value())
                
                led.value(1)
                #print("uues")
           
            led.value(0)
            mouse_to_food = timer_food - timer_start
            timer_end = utime.ticks_ms()
            task_end = timer_end-timer_start
        
            yield([i, times_num, mouse_to_food, task_end])    

        
        
            

print(belay.list_devices())
bh = food_training('COM9')  #Food training
bh.food_setup() # fm.food_setup
bh.food_magazine() #this is for the spitting

data1 = []
               
animal="mouse1" # name can be changes                    
from datetime import datetime#Impementing date
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
date = dt_string
fileName = animal+"_"+ date+".csv"
with open(fileName,'w') as csvfile: #fid:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Trial", "NP touch", "M2f", "total"])


for i in bh.food_magazine():
    print(i)
    data1.append(i)
    print(data1)
    with open(fileName,'a') as csvfile: #fid:
        csvwriter = csv.writer(csvfile)
        #for i in range(0,len(data),10):
    #             clean_data.append(data[i:i+10])
        csvwriter.writerow(data1)
       
        
    
            
            
          #



