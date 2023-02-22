
import belay
from belay import Device
import time

#import utime

#how can I make the timer get out of the loops
class phase_2(Device):
    
    @Device.setup
    def phase2_setup():



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



        button_pressed = False
        timer_starts =utime.ticks_ms()


    @Device.task
    def phase2():
#for i in range(100):
        for i in range(2):
            #print('Trial:',str(i+1)+('/100'))            
            
            #if button_food.value()==0: #when the dispense-food button is not pressed
            led.value(1) #food indicator LED is turned on as food is dispensed
            #for now, the 2 NP buttons' leds are turned off
            NP_1.value(0) 
            NP_2.value(0)
            NP_3.value(0)
            NP_4.value(0)


            while button_food.value() == 1: 
                next
            
            #while button_food.value()==0: #when the dispense-food button is pressed, which means the IR-Beam has been broken
            #print("mouse break IR Beam")# ADD TIME
            led.value(0) 
            #utime.sleep(5)
            utime.sleep(1)

            nose_pokes = [NP_1,NP_2,NP_3,NP_4]
            
            np_buttons = [button_1,button_2,button_3,button_4]
            
            #random choice between 0 to length of nose_pokes
            choice = random.randint(0,3)
            
            #print('NP number chosen',choice)
            
            nose_pokes[choice].value(1) #NP turns on but button hasn't yet been activated
            np_buttons[choice].value(0)
            led.value(0) # Foood is off
            
            while np_buttons[choice].value() == 1: #while there is no np button detected, nothing happens
                
                next
            #button has been pressed
            #print("this phase")
            T2_timer= utime.ticks_ms()
            nose_pokes[choice].value(0) #NP LED is turned off
            sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
            maxseq=100
            counter=0
            while counter<maxseq:
                for step in sequence:
                      for j in range(len(pins)):
                        pins[j].value(step[j])
                        sleep(0.001)
                        counter=counter+1
            led.value(1) #Food LED is turned on
            
            #initial food button now needs to be pressed, representing the IR-beam being broken
            while button_food.value() == 1: #waits for IR beam to broken which means food is eaten
                #print("CC")
                next
                
                
            led.value(0) #Food LED is turned off as food has been eaten (IR-beam broken)
            time_food =utime.ticks_ms()
            mouse_to_food = time_food - T2_timer#time still feels wrong 
            #print("mouse ate pallet at " + str(mouse_to_food) + "ms")
            timer_end = utime.ticks_ms()
            task_end = timer_end-timer_starts
            
            utime.sleep(1)
            
            yield([i, "5", choice, mouse_to_food, task_end])
            
           
           
if __name__ == "__main__":

    print(belay.list_devices())
    bh = phase_2('COM9')  #Food training
    bh.phase2_setup() # fm.food_setup
    
    bh.phase2() #this is for the spitting
    i_values = []
    try:
        for i in bh.phase2():
            print(i)
            i_values.append(i)
            print(i_values)
             
            #file naming:      
    except:
        print('this is the exception')
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
        csvwriter.writerow(["trial","ITI","choice","m2f","total"])
        data = i_values
        for i in range(0,len(data),5):
            data.append(data[i:i+5])
        csvwriter.writerows(data)

    bh.close()
    
#Eberything works but the yield onlyprints teh last trial, doesn't spit
    #times in all of the are still wrong
        