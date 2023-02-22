#Stage 10:


#SAME as stage 4 to 5:
#just SD varies
#SD and Extra time = 1 and 4


import belay
from belay import Device
import time

#import utime

#how can I make the timer get out of the loops
class stage_12(Device):
    
    @Device.setup
    def stage12_setup():
               
        #imports
        import machine
        import utime
        import random
        from machine import Pin
        from time import sleep
        
        #pins
        IN1 = Pin(14,machine.Pin.OUT)
        IN2 = Pin(27,machine.Pin.OUT)
        IN3 = Pin(25,machine.Pin.OUT)
        IN4 = Pin(26,machine.Pin.OUT)

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


 #SD, ITI AND LH:
        

    
    @Device.task
    def stage12_task():
        
        SD=1000
        extra = 4000
        ITI = 5000
       
        nose_pokes = [NP_1,NP_2, NP_3, NP_4]
        np_buttons = [button_1,button_2,button_3,button_4]
          
        num_trials = 10
        for trial in range(num_trials):
            
                
            correct_responses = 0 #counter for when the mouse has pressed the right button
            accuracy = 0 #we only count correct_responses, so if no correct_responses then accuracy is 0
            omissions = 0 #counter of when no button is pressed
            premature_responce=0
            incorrect_responce=0
        

            possible_SDs = [1000,500,200]
            index_current_SD = 0


            
            count_trials_five = 0
            count_trials_seven = 0
            count_trials_twelve = 0



            for i in range(num_trials):
                selected_SD = possible_SDs[random.randint(0,len(possible_SDs)-1)]
                if selected_SD == 5:
                    count_trials_five += 1
                elif selected_SD == 7.5:
                    count_trials_seven +=1
                elif selected_SD == 12.5:
                    count_trials_twelve +=1
                    
                if 5 in possible_SDs and count_trials_five == 167:
                    possible_SDs.remove(5)
                if 7.5 in possible_SDs and count_trials_seven == 167:
                    possible_SDs.remove(7.5)
                if 12.5 in possible_SDs and count_trials_twelve == 167:
                    possible_SDs.remove(12.5)
        
        
        
        
            
            start_timer = utime.ticks_ms()

            led.value(1) 
            
            while button_food.value() == 1: #this loop waits for the button to be pressed
                timer_food = utime.ticks_ms()
                next
                
            led.value(0)
           
            #conditions for the conditions 
            ITI_break = True
            time_out = False
            button_pressed = False

            #premature responce:
            
            # randomly choosing index for nose poke
            choice = random.randint(0,3)
            print('NP number chosen',choice)
            #list of wrong buttons that can be pressed during the game
            np_buttons_wrong = [] 
            for j in range(len(np_buttons)):
                if j != choice:
                    np_buttons_wrong.append(np_buttons[j])
            
            timer_food=utime.ticks_ms()
            print("ITI")
            
            while ITI_break == True:
                
                premature_responce_timer = utime.ticks_ms()
                premature_timer= premature_responce_timer - timer_food
                
                if premature_timer < ITI:# 5000:
                    
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons[choice].value() == 0:
                        
                        led.value(0)
                        print("premature responce at ", premature_timer, "ms")

                        

                        nose_pokes[choice].value(0)
                        #utime.sleep(5)
                        ITI_break=False
                        time_out = True
                        button_pressed = True
                
                elif premature_timer > ITI: #5000:
                   
                   #print('elif is played')
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons[choice].value() == 1:
                        button_pressed = False
                        ITI_break = False
                        
                
            timer_duration = utime.ticks_ms()
            
            print("Task starts")
            while button_pressed == False:
                task_time= utime.ticks_ms()
                
                nose_pokes[choice].value(1)
                task_duration = task_time-timer_duration
             
                
                if task_duration < selected_SD + extra:   #this makes it so that the buttons are still active for 4 seconds after the led value is turned off
                   #
                   #this is for LED off but keep everything active for 4 more seconds
                    if task_duration > selected_SD:
                          nose_pokes[choice].value(0)
                          
                          

                    if np_buttons[choice].value() == 0:   #wHEN correct button is pressed then the button pressed is true and corect button is true 
                        #print(task_duration, "3")

                        #print('Mouse chose the right button at', timess, "ms")
                        button_pressed = True 
                        led.value(1) #food agazine eld turns on
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        
                        time_food= utime.ticks_ms()

                        button_food.value() == 1 #task stops until the mouse goes towards the food
                        #food sensor turns on and wait for mouse to get pellet
                        while button_food.value() == 1:
                            next 
                    
                        led.value(0) 
                        time_food =utime.ticks_ms()
                        mouse_to_food = time_food - timer_duration 
                        print(mouse_to_food)         
                        print('eating for 20 seconds')
                        correct_responses += 1 #since the mouse has succeeded, we add 1 to our counter of correct_responses
                        
                        utime.sleep(1) #should be 20
                        
                        
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0: #if the wrong button is pressed then time out utime sleep 5
                        print('Mouse chose the wrong button at', task_duration, "ms")
                        led.value(0)
                        nose_pokes[choice].value(0)
                        
                        
                        
                        button_pressed = True
                        time_out = True
                        
                    
                elif task_duration > selected_SD + extra:
                    print("omission")
                    button_pressed=True
                    time_out=True
                    omissions += 1
                
                    
                
            if time_out == True: #and button_pressed=True:
                led.value(0)
                nose_pokes[choice].value(0)
                print("5 second time out")
                utime.sleep(1)





if __name__ == "__main__":

    print(belay.list_devices())
    bh = stage_12('COM9')  #Food training
    bh.stage12_setup() # fm.food_setup

    bh.stage12_task() #this is for the spitting
    i_values = []
    #try:
    #print(bh.stage_5csrtt_task())
    for i in bh.stage12_task():
        print(i)
        i_values.append(i)
        print(i_values)
             
            #file naming:      
   # except:
    #    print('this is the exception')
     #   print(i_values) 

   
   
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
        csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses", "correct_responses", "omissions", "incorrect responses","m2f","total"])
        data = i_values
        for i in range(0,len(data),10):
            data.append(data[i:i+10])
        csvwriter.writerows(data)

    bh.close()



        #The only issue is that the light won't fully turn off


