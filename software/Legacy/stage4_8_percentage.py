#these imports are necessary for the different phases
import machine
import utime 
import random

#This is for the stepper motor that turns the food dispenser allowing
from machine import Pin  
from time import sleep


#The pins from the stepper motor
IN1 = machine.Pin(27,machine.Pin.OUT)
IN2 = machine.Pin(14,machine.Pin.OUT)
IN3 =machine.Pin(25,machine.Pin.OUT)
IN4 =machine.Pin(26,machine.Pin.OUT)

pins = [IN1, IN2, IN3, IN4]


led=machine.Pin(15, machine.Pin.OUT) #LED = the yellow LED for the food magazine
button_food=machine.Pin(22,Pin.IN) # Seonsr LED fro teh food magazine
button_dispenser = machine.Pin(35, machine.Pin.IN) # Sensor LEDs for the food dispenser to detect when food pellets come down

#All the pins for teh yellow LEDs nose pokes
NP_1=machine.Pin(17,machine.Pin.OUT) 
NP_2=machine.Pin(16,machine.Pin.OUT)
NP_3=machine.Pin(19,machine.Pin.OUT)
NP_4=machine.Pin(21, machine.Pin.OUT)
NP_5=machine.Pin(2,machine.Pin.OUT)

#All the IR. sensors for the different Nose pokes
button_1 = machine.Pin(23,Pin.IN)
button_2 = machine.Pin(5,Pin.IN) 
button_3 = machine.Pin(18,Pin.IN)
button_4 = machine.Pin(4,Pin.IN)
button_5 = machine.Pin(32,machine.Pin.IN)



#This is to associate each button with the Nose poke for the data output on teh excel sheet
button_correspondance = [ (button_1, "NP_1"), (button_2, "NP_2"), (button_3, "NP_3"), (button_4, "NP_4"), (button_5,"NP_5")]


#This sets all the Nosepoked yellow LED values at 0 before the trial starts
NP_1.value(0)
NP_2.value(0)
NP_3.value(0)
NP_4.value(0)
NP_5.value(0)


#This is the function for the food dispenser giving the reward:
def reward():
    pellet = 1 #Pellet is one which allows for the food dispensing to start through the while loop underneath
    #sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] #This is the order of each pin which leads to it's sequence to turn
    #maxseq=10 
    #direction=0
    sequence= [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    while pellet==1:
        
        #[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
            
        for i in range(150):
            for step in sequence:
                for j in range(len(pins)):  #j is a variable defined to range in the length of the pins
                    pins[j].value(step[j]) 
                    sleep(0.001) #this is to avoid overloading, give a small break 
                    if pellet == 1: #if pellet is equal to one then the button.dispenser is 1 therefore the pellet hasn't dropped yet
                        pellet = button_dispenser.value()
                    #if pellet == 0: #if the pellet equals to 0 then a pellet has dropped, the while loop stops and the code can continue
                    #    print('')
        
        #sleep(0.01)
        sequence.reverse() 

        for i in range(100):
            for step in sequence:
                for j in range(len(pins)):  #j is a variable defined to range in the length of the pins
                    pins[j].value(step[j]) 
                    sleep(0.001) #this is to avoid overloading, give a small break 
                    if pellet == 1: #if pellet is equal to one then the button.dispenser is 1 therefore the pellet hasn't dropped yet
                        pellet = button_dispenser.value()
                    #if pellet == 0: #if the pellet equals to 0 then a pellet has dropped, the while loop stops and the code can continue




correct_responce = 0 #counter for when the mouse has pressed the right button
accuracy = 0 #we only count correct_responce, so if no correct_responce then accuracy is 0
omissions = 0 #counter of when no button is pressed
premature_responce=0 
incorrect_responce=0
accuracy_percentage = 0
omission_percentage=0
index_current_SD = 0 #the index of which SD is on within the possible SDs
omission_counter =0


num_trials = 15 #another way to set up and change the trials



#Start of task
for trial in range(num_trials):

#variables
     
    wrong_button_name= None # no wrong buttons pressed at teh moment
    premature_timer=0 
    omissions=0
    
    #ITI/SD AND LH:
    extra = 4000
    ITI= 5000
    
    #possible_SDs = [16000,8000,4000,2000,1500,1000]
    possible_SDs = [1600,800,400,200,1500]  #all teh SDs as the phase progresses
    current_SD= possible_SDs[index_current_SD] #The current SD is teh SD that is being executed if teh criteria has been met
    
    nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
    np_buttons = [button_1,button_2,button_3,button_4, button_5]
            
    start_timer = utime.ticks_ms()
    
    #start of the trial
    led.value(1) #Food magazine yellow LED turns on to start the trial
    
    while button_food.value() == 1: #this loop waits for the food magazine button to be pressed
        timer_food = utime.ticks_ms()
        next
    
    led.value(0) #button pressedn LED is 0
   
   #Variables for the condition to break or continue 
    ITI_break = True
    time_out = False
    button_pressed = True


    
    # randomly choosing index for nose pokes to turn on
    choice = random.randint(0,4)
  
    #list of wrong buttons that can be pressed during the game
    np_buttons_wrong = [] 
    for f in range(len(np_buttons)):
        if f != choice:
            np_buttons_wrong.append(np_buttons[f]) #it creates a list of all the NPs apart from NP choice which will be the correct one
    

    
    timer_premature=utime.ticks_ms() #timer for premature response
    
    while ITI_break == True: #while the ITI is under 5000ms
        

        premature_responce_timer = utime.ticks_ms()
        premature_timer= premature_responce_timer - timer_premature
        #print(premature_timer)
        
            
        if premature_timer < ITI: #while the premature timer is smaller than the ITI:
            
                                  # If a button is pressed: 
            if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0  or np_buttons_wrong[3].value()==0 or  np_buttons[choice].value() == 0 :
                
                led.value(0) # the food magazine LED remain off

                nose_pokes[choice].value(0) #the correct NP is turned off
                

                premature_responce +=1 #premature responce is added to criteria calculator
                #utime.sleep(5)
                ITI_break=False #the ITI_break loop ends
                time_out = True #The mouse goes trhough a time out
                button_pressed = True #A nose poke has been poked
               # print("premature")
                
                #All variables that remain at 0 (not +1)
                mouse_to_food =0
                correct_time=0
                task_duration=0
                omissions = 0
        
        elif premature_timer > ITI: #If no buton has been pressed
           
        
            if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==1 or np_buttons[choice].value() == 1:
                button_pressed = False #no Nosepoke has been poked 
                ITI_break = False #the ITI break is over
                
    
    timer_duration = utime.ticks_ms()


    #Start of SD
    
    while button_pressed == False: #While no nosepoke has been pressed the task keeps going:
        task_time= utime.ticks_ms()
        
        nose_pokes[choice].value(1)
        task_duration = task_time-timer_duration
     
        
        if task_duration < current_SD + extra:   #this makes it so that the buttons are still active for 4 seconds after the led value is turned off
           
    
            if task_duration > current_SD:
                  nose_pokes[choice].value(0) #After the SD time has passed the yellow LED turns off but there is still the LH
                  
                  

            if np_buttons[choice].value() == 0:   #this means the crrect button has been pressed  
                
                correct_time = task_time-timer_duration  #timer for when the mouse got the correct responce                     
                button_pressed = True #A NP has been poked
                
                #food dispenser is on
                reward()
            
                            
                led.value(1) #food agazine LED turns on
                NP_1.value(0)
                NP_2.value(0)
                NP_3.value(0)
                NP_4.value(0)
                NP_5.value(0)
                
                timer_fooder= utime.ticks_ms() #timer mouse to food

                button_food.value() == 1 #task stops until the mouse goes towards the food
                
                
                while button_food.value() == 1: #food sensor turns on and wait for mouse to get pellet
                    utime.sleep(0.1)
                    next
                    
            
            
                time_food =utime.ticks_ms()
                led.value(0) 
                
                mouse_to_food = time_food - timer_fooder #mouse to food timer
                
                correct_responce += 1 #since the mouse has succeeded, we add 1 to our counter of correct_responce
                #accuracy = correct_responce / (trial+1) * 100 #timed by 100 so this is accuracy percentage 
                utime.sleep(1) #should be 20
                
                premature_timer=0
                task_duration=0
                omissions = 0
                wrong_button_name=0
                
            
            wrong_button_pressed = None #no wrong NP has been poked
            
            for button in np_buttons_wrong:  #Within the NP in the list of wrong NPs
                
                
                if button.value() == 0: #If a wrong NP has been pressed
                   
                    wrong_button_pressed = button
                    wrong_button_name = ""
                    
                    #code to know which wrong NP has been pressed in the case of an incorrect NP has been poked and relate it back to the NP through the button_correspondance
                    for button_variable,np_name in button_correspondance:
                        if button_variable == wrong_button_pressed:
                            wrong_button_name = np_name #teh wrong NP = to the NP_name (it's associating the sensor to the correct NP)
                            break
                    
                    led.value(0) #food magazine yellow lED is off
                    nose_pokes[choice].value(0) #Correct NP light turns off
                    
                    incorrect_responce +=1
                    
                    
                    mouse_to_food = 0
                    correct_time= 0
                    premature_timer = 0
                    omissions=0
                   
                    #button has been pressed but since it was incorrect then time out is also true
                    button_pressed = True
                    time_out = True
        
                    break
                
            
        elif task_duration > current_SD + extra:# if the task duration is higher thna the SD and the LH then that means omission
          
            button_pressed=True
            time_out=True
            
            omissions += 1
            task_duration = 0
            mouse_to_food = 0
            correct_time= 0
            premature_timer = 0
            
            omission_counter +=1
            
            
           
        
            
        
    if time_out == True: #When time out was true then
        led.value(0)
        nose_pokes[choice].value(0)
        
        #for when yielding the data, need to specifiy that mouse_to_food and correct responce are 0
        mouse_to_food = 0
        correct_time=0
        
        utime.sleep(1) #whole system is off for 5 seconds
        
        
    task_end_time= utime.ticks_ms() 
    task_end = task_end_time - start_timer
    print(task_end)
    print('') #linebreak
    
    accuracy_percentage = 100

    if incorrect_responce > 0:
        accuracy_percentage = (correct_responce/(correct_responce+incorrect_responce))*100
    
    print(accuracy_percentage, "within loop")
        
 
    
    if omission_counter == 0:
        omissing_percentage = 0
    elif omission_counter > 0:
        omission_percentage= (omission_counter/ (correct_responce+incorrect_responce+omission_counter))*100
    print(omission_percentage,"omission")
        
    
   
    #SD will decrease if these conditions are met
    if index_current_SD+1 != len(possible_SDs): #checking that we are not at the end of the list
        if trial >= 6:
            #print('first condition met')
            if accuracy_percentage >= 60 and omission_percentage < 30:
                print('second condition met')
                index_current_SD += 1
            elif accuracy_percentage >= 60 and correct_responce == 5:
                print('third condition met')
                index_current_SD += 1
        


   # yield([trial+1,ITI, current_SD, choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name,  omissions, task_end])




