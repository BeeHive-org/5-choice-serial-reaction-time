
import belay
from belay import Device
import time

#import utime

#how can I make the timer get out of the loops
class SerialBeeHive(Device):
    
    @Device.setup
    def setup():


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




        start_time=utime.ticks_ms()

        #possible_SDs = [16000,8000,4000,2000,1500,1000]
       
                

    @Device.task
    def stage_5csrtt_task():
        print("Start")
        start_time=utime.ticks_ms()

        
        #variables and trials:
        num_trials = 10
        correct_responses = 0 #counter for when the mouse has pressed the right button
        accuracy = 0 #we only count correct_responses, so if no correct_responses then accuracy is 0
        omissions = 0 #counter of when no button is pressed
        premature_responce=0
        incorrect_responce=0
        
        
        #ITI/SD AND LH:
        extra = 4000
        ITI= 5000
        
        possible_SDs = [1000,2000,4000,2000,1500,1000]

        index_current_SD = 0
        current_SD= possible_SDs[index_current_SD]
        nose_pokes = [NP_1,NP_2, NP_3, NP_4]
    
        np_buttons = [button_1,button_2,button_3,button_4]
        
        
        
        #Start of task
        for i in range(num_trials):
           # print('current SD is at index',str(index_current_SD),'and the value is',str(possible_SDs[index_current_SD]))
            
            start_timer = utime.ticks_ms()

            led.value(1) 
            
            while button_food.value() == 1: #this loop waits for the button to be pressed
                timer_food = utime.ticks_ms()
                next
            #
            led.value(0)
           
           #Variables for the condition to break or continue 
            ITI_break = True
            time_out = False
            button_pressed = True

            #premature responce:
            
            # randomly choosing index for nose poke
            choice = random.randint(0,3)
           # print('NP number chosen',choice)
            #list of wrong buttons that can be pressed during the game
            np_buttons_wrong = [] 
            for j in range(len(np_buttons)):
                if j != choice:
                    np_buttons_wrong.append(np_buttons[j])
            

            #ITI- premature responce
            print("ITI")
            
            #times
            timer_premature=utime.ticks_ms()
            
            while ITI_break == True:
                
                #reason ITI isn't working after first trial = Time adds up thereefore it's always more than ITI--> ask how to fix
                
    
                premature_responce_timer = utime.ticks_ms()
                premature_timer= premature_responce_timer - timer_premature
#                 print("time itit", premature_timer)
                
                    
                if premature_timer < ITI: 
                    
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons[choice].value() == 0:
                        
                        led.value(0)

                        nose_pokes[choice].value(0)
                        

                        premature_responce +=1
                        #utime.sleep(5)
                        print("button pressed")
                        ITI_break=False
                        time_out = True
                        button_pressed = True
                
                elif premature_timer > ITI: #5000:
                   
                   #print('elif is played')
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons[choice].value() == 1:
                        button_pressed = False
                        ITI_break = False
                        
                
            timer_duration = utime.ticks_ms()
            
            
            #Start of SD
            print("Task starts")
            while button_pressed == False:
                task_time= utime.ticks_ms()
                
                nose_pokes[choice].value(1)
                task_duration = task_time-timer_duration
             
                
                if task_duration < current_SD + extra:   #this makes it so that the buttons are still active for 4 seconds after the led value is turned off
                   #
                   #this is for LED off but keep everything active for 4 more seconds
                    if task_duration > current_SD:
                          nose_pokes[choice].value(0)
                          
                          

                    if np_buttons[choice].value() == 0:   #wHEN correct button is pressed then the button pressed is true and corect button is true 
                        #print(task_duration, "3")
                        print("correct")
                        #print('Mouse chose the right button at', timess, "ms")
                        button_pressed = True
                        
                        #food dispenser is on
                        sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
                        maxseq=500
                        counter=0
                        while counter<maxseq:
                            for step in sequence:
                                  for x in range(len(pins)):
                                    pins[x].value(step[x])
                                    sleep(0.001)
                                    counter=counter+1
                                    
                        led.value(1) #food agazine eld turns on
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        
                        time_food= utime.ticks_ms()

                        button_food.value() == 1 #task stops until the mouse goes towards the food
                        #food sensor turns on and wait for mouse to get pellet
                        print("food")
                        while button_food.value() == 1:
                            next 
                    
                        led.value(0) 
                        time_food =utime.ticks_ms()
                        mouse_to_food = time_food - timer_duration 
                        print(mouse_to_food)         
                       
                        
                        correct_responses += 1 #since the mouse has succeeded, we add 1 to our counter of correct_responses
                        accuracy = correct_responses / (i+1) * 100 #timed by 100 so this is accuracy percentage 
                        print('current accuracy with',str(i+1),'trials is',str(accuracy)+'%')
                        utime.sleep(3) #should be 20
                        
                        
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0: #if the wrong button is pressed then time out utime sleep 5
                      #  print('Mouse chose the wrong button at', task_duration, "ms")
                        print("wrong")
                        led.value(0)
                        nose_pokes[choice].value(0)
                        
                        
                        accuracy = correct_responses / (i+1) * 100 #timed by 100 so this is accuracy percentage 
                        #print('current accuracy with',str(i+1),'trials is',str(accuracy)+'%')
                        
                        
                        incorrect_responce +=1
                        button_pressed = True
                        time_out = True
                        
                    
                elif task_duration > current_SD + extra:
                    print("omission")
                    button_pressed=True
                    time_out=True
                    omissions += 1
                
                    
                
            if time_out == True: #and button_pressed=True:
                led.value(0)
                nose_pokes[choice].value(0)
                print("5 second time out")
                utime.sleep(3)
                
                
            task_end_time= utime.ticks_ms() 
            task_end = task_end_time - start_time
            print(task_end)
            print('') #linebreak
            
            
            
            #SD will decrease if these conditions are met
            if index_current_SD+1 != len(possible_SDs): #checking that we are not at the end of the list
                if i >= 5:
                    #print('first condition met')
                    if accuracy >= 60 and omissions < 30:
                        print('second condition met')
                        index_current_SD += 1
                    elif accuracy >= 60 and correct_responses == 5:
                        print('third condition met')
                        index_current_SD += 1
                

      #  print('number of trials',num_trials)
       # print('number of correct responses',correct_responses)
        #print('accuracy',accuracy)
       
        #print(num_trials)
        #print(ITI)
        #print(possible_SDs[index_current_SD] )
        #print(nose_pokes[choice])
        #print(premature_responce)
        #print(correct_responses)
        #print(omissions)
        #print(incorrect_response)
        #print(mouse_to_food)

       # if omissions or premature_responce or incorrect_responce== num_trials:
           
        #yield([num_trials, ITI, possible_SDs[index_current_SD],choice, premature_responce, correct_responses, omissions, incorrect_responce, task_end])
        #else:
        yield ([i, ITI, possible_SDs[index_current_SD], choice,premature_responce, correct_responses, omissions, incorrect_responce, mouse_to_food, task_end])

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








if __name__ == "__main__":

    print(belay.list_devices())
    bh = SerialBeeHive('COM9')  #Food training
    bh.setup() # fm.food_setup

    bh.stage_5csrtt_task() #this is for the spitting
    i_values = []
    #try:
    #print(bh.stage_5csrtt_task())
    for i in bh.stage_5csrtt_task():
        print(i)
        i_values.append(i)
        print(i_values)
             
            #file naming:      
   # except:
    #    print('this is the exception')
     #   print(i_values) 
    #     yield ([i, ITI, possible_SDs[index_current_SD], nose_pokes[choice],premature_responce, correct_responces, omissions, incorrect responce, mouse_to_food, task_end])   
   
   
   
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

#variables needed on CSV:
    #Trial
    # Current SD
    # NP chosen
    # ITI
    #accuracy
    #correct responces
    #M2F
    #Total

#could look into having teh chosen NP to be in the output but need to see the difficulty to do it
#The only issue is that the light won't fully turn off