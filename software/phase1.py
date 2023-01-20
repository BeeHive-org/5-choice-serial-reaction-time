

import belay
from belay import Device
import time

#import utime

#how can I make the timer get out of the loops
class phase_1(Device):
    
    @Device.setup
    def phase1_setup():
        import machine
        import utime
        import random

        from machine import Pin
        from time import sleep
        IN1 = Pin(14,Pin.OUT)
        IN2 = Pin(27,Pin.OUT)
        IN3 = Pin(25,Pin.OUT)
        IN4 = Pin(26,Pin.OUT)

        pins = [IN1, IN2, IN3, IN4]


        led=machine.Pin(15, machine.Pin.OUT) #LED WORKS
        button_food=machine.Pin(22,machine.Pin.IN)


        NP_1=machine.Pin(17,machine.Pin.OUT)
        NP_2=machine.Pin(16,machine.Pin.OUT)
        NP_3=machine.Pin(19,machine.Pin.OUT)
        NP_4=machine.Pin(21,machine.Pin.OUT)
        NP_5=machine.Pin(2,machine.Pin.OUT)

        button_1 = machine.Pin(23,machine.Pin.IN)
        button_2 = machine.Pin(5,machine.Pin.IN) #pin 4
        button_3 = machine.Pin(18,machine.Pin.IN)
        button_4 = machine.Pin(4,machine.Pin.IN)
        



        NP_1.value(0)
        NP_2.value(0)
        NP_3.value(0)
        NP_4.value(0)
        NP_5.value(0)


#PHASE 1:

      #  count_of_clicks = 0
        timer_starts = utime.ticks_ms()




#for x in range (1, 50):
    @Device.task
    def phase1():
        
        for i in range (4):
            
            button_pressed = False
            #times=[4,8,16,32]
            times=[1,1.1,2,1]
            times_num = random.choice(times)
            
            print(times_num)
            utime.sleep(times_num)
            food_time = utime.ticks_ms()
            while button_pressed== False:
            
        
                if button_1.value() == 0 or button_2.value() == 0  or button_3.value() == 0  or button_4.value() == 0: #if any of the NPs are poked
                     #Lights are tunred off 
                    
                    NP_1.value(0) #THE Lights remain on
                    NP_2.value(0)
                    NP_3.value(0)
                    NP_4.value(0)
                    NP_5.value(0)

                    sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
                    maxseq=100
                    counter=0
                    while counter<maxseq:
                        for step in sequence:
                            for j in range(len(pins)):
                                pins[j].value(step[j])
                                sleep(0.001)
                        counter=counter+1
                   # NP_5.value(0)
                    led.value(1) #LED is on leading to food falling
                    button_food.value(0)
                    #print("Food out")
                    while button_food.value() == 1:
                        led.value(1)
                        
                  #  if button_food.value() == 0:
                    timer_food = utime.ticks_ms()
                    mouse_to_food = timer_food -food_time #it accumulates instead f timing it one by one
                    #print("mouse ate pallet at " + str(mouse_to_food) + "ms")
                    led.value(0)
                
                
                    #times=[4,8,16,32]
                    times=[1]
                    times_num = random.choice(times)
                    #print("The ITI will run for", times_num, "s") 
                    utime.sleep(times_num)
                    
                    button_pressed = True
                    timer_end=utime.ticks_ms()
                    trial_end = timer_end-timer_starts
                    print(trial_end)
                #ITI timer starts again
                           
            
                elif button_1.value() == 1 or button_2.value() == 1 or button_3.value() == 1 or button_4.value() == 1:#0 meaning the NPs haven't been touched     
                        NP_1.value(1) #THE Lights remain on
                        NP_2.value(1)
                        NP_3.value(1)
                        NP_4.value(1)
                        NP_5.value(1)
                        led.value(0)
                    
                
            yield([i, times_num, mouse_to_food, trial_end])
                
                #print("END")
       #Need to figure out how to take it out of the while loop once hte 50th trial is done to go onto phase 2
                        
                        
          
if __name__ == "__main__":
   
   # print(fileName)
    

    print(belay.list_devices())
    bh = phase_1('COM9')  #Food training
    bh.phase1_setup() # fm.food_setup
    a = bh.phase1()
   # print(a)
    
    bh.phase1() #this is for the spitting
    i_values = []
    
    try :   
        for i in bh.phase1():
            print(i)
            i_values.append(i)
            print(i_values)
                 
                #file naming:
               
                
    except:
          #  print("2")
        print(i_values)
            
        
        
        
    #CSV
    animal="mouse1" # name can be changes                    
    from datetime import datetime#Impementing date
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
    date = dt_string
    fileName = animal+"_"+ date+".csv"

    import csv
    with open(fileName,'w') as csvfile: #fid:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["trial","ITI","m2f","total"])
        data = i_values
        for i in range(0,len(data),4):
            data.append(data[i:i+4])
        csvwriter.writerows(data)

    bh.close()
    
                
                
