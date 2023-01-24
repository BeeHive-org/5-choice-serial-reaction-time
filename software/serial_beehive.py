# These are imports necessary to use the belay library
import belay
from belay import Device
import time



class SerialBeeHive(Device): #This is the class that contains all the phases 
    
    @Device.setup # Device setup is where the yellow LEDs and sensor LEDs are defined, also imports.
    def setup():

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
                    print (button_dispenser.value())
                    
                    
                    #[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
                        
                    for i in range(80):
                        for step in sequence:
                            for j in range(len(pins)):  #j is a variable defined to range in the length of the pins
                                pins[j].value(step[j]) 
                                sleep(0.001) #this is to avoid overloading, give a small break 
                                if pellet == 1: #if pellet is equal to one then the button.dispenser is 1 therefore the pellet hasn't dropped yet
                                    pellet = button_dispenser.value()
                                #if pellet == 0: #if the pellet equals to 0 then a pellet has dropped, the while loop stops and the code can continue
                                #    print('')
                    utime.sleep(1)
                    #sleep(0.01)
                    sequence.reverse() 

                    for i in range(25):
                        for step in sequence:
                            for j in range(len(pins)):  #j is a variable defined to range in the length of the pins
                                pins[j].value(step[j]) 
                                sleep(0.001) #this is to avoid overloading, give a small break 
                                if pellet == 1: #if pellet is equal to one then the button.dispenser is 1 therefore the pellet hasn't dropped yet
                                    pellet = button_dispenser.value()
                                #if pellet == 0: #if the pellet equals to 0 then a pellet has dropped, the while loop stops and the code can continue

        
        
    @Device.task 
    def food_training(): #this is the function for the food training
        """Food magazine training"""
            
        num_trial =50
        for trial in range (num_trial): #trials meaning trials that can be changed in the brackets
            timer_start= utime.ticks_ms() #this is a timer of the start of the trial    
            led.value(0) #the food magazine LED value starts at 0
           
            #ITIs
            times=[4,8,16,32] 
            
            #times=[1,1.2,1.1]
            times_num = random.choice(times) #random time out of these is chosen
                
            led.value(0)  #During ITI the LED of the food dispenser is off
            utime.sleep(times_num) # Utime.sleeps allows for the machine to pause for teh amount of times teh ITI is
            
            
            led.value(1) #After teh ITI the LED is on
            
            
            #here put stepper motor in action
            reward()
            #direction1=reward(direction=direction1)
            #print(direction1)
            
            
            timer_food = utime.ticks_ms()# timer starts to know when the mouse went for the food
            
            while button_food.value() == 1: #while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reahced frot eh food
                utime.sleep(0.1) #this allows for the timer to not bug
                led.value(1) # while it's 1 the food magazine led remains on
           
            led.value(0)# once the mouse went for the food, the while loop stops and the food magaine yellow LED turns off
            
            
            timer_food2=utime.ticks_ms()
            
            mouse_to_food = timer_food2-timer_food #mouse to food is the amount of time the mouse took to get teh food
            timer_end = utime.ticks_ms()
            
            task_end = timer_end-timer_start #end of the whole task

        
            yield([trial+1, times_num, mouse_to_food, task_end])  #variables that are going to be yielded into the CSV file



    @Device.task
    def phase1():
        
        """Phase 1"""
        
        for trial in range (49):
            
            timer_start=utime.ticks_ms()
            button_pressed = False
            utime.sleep(5)
            
            while button_pressed== False: #this a while loop that allows for the conditions 
    
                #if any of the buttons are interrupted the sensor will go from 1 to 0 showing an interruption
                #Here one of the Nosepokes has been poked
                if button_1.value() == 0 or button_2.value() == 0  or button_3.value() == 0  or button_4.value() == 0 or button_5.value()==0: #if any of the NPs are poked
                      
                    #Lights are tunred off
                    NP_1.value(0) 
                    NP_2.value(0)
                    NP_3.value(0)
                    NP_4.value(0)
                    NP_5.value(0)
                    
                    #Reard is sent
                    led.value(1)
                    
                    reward()
                   
                    food_time = utime.ticks_ms()

                    while button_food.value() == 1:
                        utime.sleep(0.1)
                        led.value(1)
                        
                  
                    timer_food = utime.ticks_ms()
                    mouse_to_food = timer_food -food_time
                    
                    led.value(0)
                
                
                    button_pressed = True #when the button pressed is true then the while loop can stop and the trial can go again
                    timer_end=utime.ticks_ms()
                    trial_end = timer_end-timer_start
                    
                           
                #If no NPs are pressed then nothing happens
                elif button_1.value() == 1 or button_2.value() == 1 or button_3.value() == 1 or button_4.value() == 1 or button_5.value() == 1:#0 meaning the NPs haven't been touched     
                        NP_1.value(1) #THE Lights remain on
                        NP_2.value(1)
                        NP_3.value(1)
                        NP_4.value(1)
                        NP_5.value(1)
                        led.value(0)
                    
                
            yield([trial+1, times_num, mouse_to_food, trial_end])



    @Device.task
    def phase2():
        """Phase 2"""
        
        for trial in range(99):
                        
            timer_starts=utime.ticks_ms()
            
            led.value(1) #food indicator LED is turned on as food is dispenseR   

            
            while button_food.value() == 1: #nothing happens untilthe mouse goes to Nospoke the food magazine
                utime.sleep(0.1)
                next
            
            led.value(0)  #Once pressed Foog magazine yellow LED turns off 
           
            utime.sleep(5) #ITI of 5 seconds
            
            #matching accumulating all the NP and button into lists
            nose_pokes = [NP_1,NP_2,NP_3,NP_4, NP_5]
            np_buttons = [button_1,button_2,button_3,button_4, button_5]
            
            #random choice between NP1 to NP5 (0 to 4)
            choice = random.randint(0,4)
            
            nose_pokes[choice].value(1) #NP turns on but button hasn't yet been activated
            np_buttons[choice].value(0) #NP hasn't been poked yet
            led.value(0) #Food LED is off
            
            while np_buttons[choice].value() == 1: #while the chosen NP hasn't been poked, nothing happens
                utime.sleep(0.1)
                
                next
                
            #button has been pressed
        
            T2_timer= utime.ticks_ms() #timer for mouser to food
            
            nose_pokes[choice].value(0) #chosen NP LED is turned off
            
            #Food dispenser is on
            reward()
              
              
            led.value(1) #Food LED is turned on
            
            
            while button_food.value() == 1: #waits for IR beam to broken which means food is eaten
                utime.sleep(0.1)
                next
                
                
            led.value(0) #Food LED is turned off as food has been eaten (IR-beam broken)
            
            time_food =utime.ticks_ms()
            mouse_to_food = time_food - T2_timer
            timer_end = utime.ticks_ms()
            task_end = timer_end-timer_starts
            
            utime.sleep(20) #consumption interval 20 seconds
            
            yield([trial+1, "5", choice, mouse_to_food, task_end])
            
            
            
        
            
    @Device.task
    def stage_5csrtt_task():
        """5 choice serial task"""
        
        #Need to set the counter to 0 for all the variables that are going to be "calculated"
        correct_responce = 0 #counter for when the mouse has pressed the right button
        omissions = 0 #counter of when no button is pressed
        premature_responce=0 
        incorrect_responce=0
        accuracy_percentage = 0 
        omission_percentage=0
        index_current_SD = 0 #the index of which SD is on within the possible SDs
        omission_counter =0


        #Start of task
        for trial in range(200000): #providing an unlimitted amount of trials

        #variables are placed inside the for loop because they're value needs to reset every trial to not add up
             
            wrong_button_name= None # no wrong buttons pressed at teh moment
            premature_timer=0  
            omissions=0
            
            #ITI/SD AND LH:
            extra = 4000
            ITI= 5000
            
            possible_SDs = [16000,8000,4000,2000,1500,1000]
            #possible_SDs = [1600,800,400,200,1500,1000]  #all teh SDs as the phase progresses
            current_SD= possible_SDs[index_current_SD] #The current SD is teh SD that is being executed if teh criteria has been met
            
            if current_SD==1000: #once it reaches sd of 1 second the whole loop stops and it moves on to the next phase
                break
            
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
                       
                        utime.sleep(20) #eating period
                        
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
                    
                    #In this case there are two omission counters butthis can be edited based on how the person want sto output their data.
                    #Here one of the omissions is used to output "1" every time there is an omission and the other is a counter to measure the omission percentage.  
                    
                
            if time_out == True: #When time out was true then
                led.value(0)
                nose_pokes[choice].value(0)
                
                #for when yielding the data, need to specifiy that mouse_to_food and correct responce are 0
                mouse_to_food = 0
                correct_time=0
                
                utime.sleep(5) #whole system is off for 5 seconds
                
                
            task_end_time= utime.ticks_ms() 
            task_end = task_end_time - start_timer
            print(task_end)
            print('') #linebreak
            
            #Calculating the accuracy percentage and the omissions percentage for the criteria
            
            accuracy_percentage = 100 # Here in order to not divide 1 correct response by 0 in case there is no incorrect response we just say that correct response is 100%

            if incorrect_responce > 0: #unless incorrect response is higher than 0, which then the accuracy percentage can be calculated
                accuracy_percentage = (correct_responce/(correct_responce+incorrect_responce))*100
            
           # print(accuracy_percentage, "within loop")
                
         
            #Same logic here. If omission counter is 0 then the the percentage is 0 unless omission counter is bigger than 0.
            if omission_counter == 0:
                omission_percentage = 0
            elif omission_counter > 0:
                omission_percentage= (omission_counter/ (correct_responce+incorrect_responce+omission_counter))*100
           # print(omission_percentage,"omission")
                
            
           
            #SD will decrease if these conditions are met
            if index_current_SD+1 != len(possible_SDs): #checking that we are not at the end of the list
                if trial >= 50: #If in x trial
                    
                    if accuracy_percentage >= 60 and omission_percentage < 30: #the accuracy is 60 percent or more and omission percentage is less than 30 percent then
                        print('second condition met')
                        index_current_SD += 1 #condition is met then the Stimulus duration decreases according to the list from the begining.
                    elif accuracy_percentage >= 60 and correct_responce == 5:
                        print('third condition met')
                        index_current_SD += 1
                        

       
            yield([trial+1,ITI, current_SD, choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name, omissions, omission_percentage,accuracy_percentage task_end])








  
    @Device.task
    def stage9_task():
        """stage 9"""
    
        num_trials = 1000 #another way to place number of trials
        nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
        np_buttons = [button_1,button_2,button_3,button_4, button_5]
       
        
        
        for trial in range(num_trials):
               
            start_time=utime.ticks_ms()
           
            omissions = 0  #there's no timer for omission therefore every start of the trial omission needs to be set back to 0 so it doens't add up
            wrong_button_name= None #no wrong NPs pressed
            
            
            #ITI/SD AND LH:
            extra = 4000
            ITI= 5000
            SD = 1000
            
                
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

          
            
            # randomly choosing index for nose poke
            choice = random.randint(0,4)
            
            
           # print('NP number chosen',choice)
            nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
            np_buttons = [button_1,button_2,button_3,button_4, button_5]
            
            
            #list of wrong buttons that can be pressed during the game
            np_buttons_wrong = [] 
            for j in range(len(np_buttons)):
                if j != choice:
                    np_buttons_wrong.append(np_buttons[j])
            

            #ITI
            timer_premature=utime.ticks_ms()
            
            while ITI_break == True: #similar to other phase
                
                

                premature_responce_timer = utime.ticks_ms()
                premature_timer= premature_responce_timer - timer_premature
               
                
                 #ITI   
                if premature_timer < ITI: 
                    
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 0:
                        
                        led.value(0)

                        nose_pokes[choice].value(0)
                        

                        premature_responce +=1
                        
                        ITI_break=False
                        time_out = True
                        button_pressed = True
                       
                
                elif premature_timer > ITI:
                   
       
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 1:
                        button_pressed = False
                        ITI_break = False
                        
                
            timer_duration = utime.ticks_ms()
            
            
            #Start of SD
            
            while button_pressed == False:
                task_time= utime.ticks_ms()
                
                nose_pokes[choice].value(1)
                task_duration = task_time-timer_duration
             
                
                if task_duration < SD + extra:   #Within the SD and LH time 
                   #
      
                    if task_duration > SD:
                          nose_pokes[choice].value(0)
                          
                          

                    if np_buttons[choice].value() == 0:                       
                        correct_timer = task_time-timer_duration
                        button_pressed = True
                        
                        #food dispenser is on
                        reward()
                                    
                        led.value(1)
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        
                        timer_fooder= utime.ticks_ms()

                        button_food.value() == 1 
                  
                     
                        while button_food.value() == 1:
                            utime.sleep(0.1)
                            next 
                    
                        led.value(0) 
                        time_food =utime.ticks_ms()
                        mouse_to_food = time_food - timer_fooder 
                        print(mouse_to_food)         
                       
                        
                        correct_responses += 1 #since the mouse has succeeded, we add 1 to our counter of correct_responses
                        utime.sleep(20) 
                        
                       
                        premature_timer=0
                        task_duration=0
                        omissions = 0
                        wrong_button_name=0
                    wrong_button_pressed = None
                    
                    
                    #Wrong button:
                    for button in np_buttons_wrong:
                        if button.value() == 0:
                            
                            wrong_button_pressed = button
                            wrong_button_name = ""
                            
                            for button_variable,np_name in button_correspondance:
                                if button_variable == wrong_button_pressed:
                                 
                                    wrong_button_name = np_name
                                    break
                            

                            led.value(0)
                            nose_pokes[choice].value(0)
                            
                            
                            mouse_to_food = 0
                            correct_time= 0
                            premature_timer = 0
                            omissions=0
                           
                            
                            button_pressed = True
                            time_out = True
                          
                            break
                        
                    
                elif task_duration > SD + extra:
                    
                    button_pressed=True
                    time_out=True
                    
                    task_duration = 0
                    mouse_to_food = 0
                    correct_time= 0
                    premature_timer = 0
                    
                    omissions += 1
                    
                
                    
               #Time out: 
            if time_out == True: 
                led.value(0)
                nose_pokes[choice].value(0)
                mouse_to_food = 0
                correct_time=0
                utime.sleep(5)
                
        
                
            
                
                
            task_end_time= utime.ticks_ms() 
            task_end = task_end_time - start_timer
          
            print('') #linebreak

            end_timer=utime.ticks_ms()
            task_end = end_timer-start_timer
            
            yield([trial, "5", "1", choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name,  omissions, task_end])



    @Device.task
    def stage10_task(num_trials=5):
        """stage 10"""
         #variables and trials:
       

        #SD, ITI AND LH:
        SD=1000
        extra = 4000
       
        nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
        np_buttons = [button_1,button_2,button_3,button_4,button_5]

        #start of trials
        num_trials=500
        for trial in range(num_trials):
            
            wrong_button_name= None
            omissions = 0 
            task_duration=0
            premature_timer=0
            
            #Long code to make sure that the varITIs are equally distributed
            possible_ITIs = [5000,7500,1250] #the possible ITIs
            index_current_ITI = 0 #current ITI

            num_trials = 10 #number of trials
            #counter of the amount of each ITI has been used
            count_trials_five = 0
            count_trials_seven = 0
            count_trials_twelve = 0

            for i in range(num_trials): #counter of the number of trials

                selected_ITI = possible_ITIs[random.randint(0,len(possible_ITIs)-1)] #randomised ITI taken out of the possibilities
                if selected_ITI == 5:
                    count_trials_five += 1 #counter adds +1 every time an ITI has been taken
                elif selected_ITI == 7.5:
                    count_trials_seven +=1
                elif selected_ITI == 12.5:
                    count_trials_twelve +=1
                    
                    #Allows to make sure that it doesn't go over the amount it's supposed to by removing 1
                if 5 in possible_ITIs and count_trials_five == 167:
                    possible_ITIs.remove(5)
                if 7.5 in possible_ITIs and count_trials_seven == 167:
                    possible_ITIs.remove(7.5)
                if 12.5 in possible_ITIs and count_trials_twelve == 167:
                    possible_ITIs.remove(12.5)


    
            
            
            
            start_timer = utime.ticks_ms()
            
            
            #Task starts
            led.value(1) 
            
            while button_food.value() == 1: 
                timer_food = utime.ticks_ms()
                next
                
            led.value(0)
           
            ITI_break = True
            time_out = False
            button_pressed = False
            
            
        #chosing a NP
            choice = random.randint(0,4)
            np_buttons_wrong = [] 
            for j in range(len(np_buttons)):
                if j != choice:
                    np_buttons_wrong.append(np_buttons[j])
            
            
            timer_food=utime.ticks_ms()
            
      #ITI
            while ITI_break == True:
                
                premature_responce_timer = utime.ticks_ms()
                premature_timer= premature_responce_timer - timer_food
                
                if premature_timer < selected_ITI:# 5000:
                    
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 0:
                        
                        led.value(0)
                        
                         

                        nose_pokes[choice].value(0)
                        ITI_break=False
                        time_out = True
                        button_pressed = True
                        
                        mouse_to_food =0
                        correct_time=0
                        task_duration=0
                        omissions = 0
                
                elif premature_timer > selected_ITI: #5000:
                   
                   
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==1 or np_buttons[choice].value() == 1:
                        button_pressed = False
                        ITI_break = False
                        
                
            timer_duration = utime.ticks_ms()
            
           #NP lights up
            while button_pressed == False:
                task_time= utime.ticks_ms()
                
                nose_pokes[choice].value(1)
                task_duration = task_time-timer_duration
                
                if task_duration < SD + extra:      #within SD and LH time                
                  
                    if task_duration > SD:
                          nose_pokes[choice].value(0)
                          
                          

                    if np_buttons[choice].value() == 0:  #Correct choice 
                      
                        correct_time = task_time-timer_duration
                        
                        button_pressed = True
                        
                        #Food disepner 
                        reward()
                                    
            
                                    
                        led.value(1) #food agazine eld turns on
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        
                        timer_fooder= utime.ticks_ms()

                        button_food.value() == 1 
                        
                        while button_food.value() == 1:
                            utime.sleep(0.1)
                            next
                            
                    
                    
                    
                        led.value(0) 
                        time_food =utime.ticks_ms()
                        mouse_to_food = time_food - timer_fooder 
                        #print(mouse_to_food)         
                        #print('eating for 20 seconds')
                        #correct_responses += 1 #since the mouse has succeeded, we add 1 to our counter of correct_responses
                         
                        utime.sleep(20) #should be 20
                        
                        
                        premature_timer=0
                        task_duration=0
                        omissions = 0
                        wrong_button_name=0
                        
                    
                    wrong_button_pressed = None
                    
                    #Wrong NP
                    for button in np_buttons_wrong:
                        if button.value() == 0:
                           
                            wrong_button_pressed = button
                            wrong_button_name = ""
                            
                            for button_variable,np_name in button_correspondance:
                                if button_variable == wrong_button_pressed:
                                  
                                    wrong_button_name = np_name
                                    break
                            
                            led.value(0)
                            nose_pokes[choice].value(0)
                            
                            
                            mouse_to_food = 0
                            correct_time= 0
                            premature_timer = 0
                            omissions=0
                           
                            
                            button_pressed = True
                            time_out = True
                        
                            break
                    
                                       
                elif task_duration > SD + extra: #Omission
                    print("omission")
                    button_pressed=True
                    time_out=True
                    
                    task_duration = 0
                    mouse_to_food = 0
                    correct_time= 0
                    premature_timer = 0
                    
                    omissions += 1
                    
                    
             #Time out   
            if time_out == True: 
                led.value(0)
                nose_pokes[choice].value(0)
                mouse_to_food = 0
                correct_time=0
                utime.sleep(5)
                
                
            
                
            end_timer=utime.ticks_ms()
            task_end = end_timer-start_timer
            
            yield([trial+1, selected_ITI, "1", choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name,  omissions, task_end])

                

 @Device.task
    def stage11_task():
        """stage 9"""
    
        num_trials = 500 #another way to place number of trials
        nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
        np_buttons = [button_1,button_2,button_3,button_4, button_5]
       
        
        
        for trial in range(num_trials):
               
            start_time=utime.ticks_ms()
           
            omissions = 0  #there's no timer for omission therefore every start of the trial omission needs to be set back to 0 so it doens't add up
            wrong_button_name= None #no wrong NPs pressed
            
            
            #ITI/SD AND LH:
            extra = 4000
            ITI= 5000
            SD = 1000
            
                
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

          
            
            # randomly choosing index for nose poke
            choice = random.randint(0,4)
            
            
           # print('NP number chosen',choice)
            nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
            np_buttons = [button_1,button_2,button_3,button_4, button_5]
            
            
            #list of wrong buttons that can be pressed during the game
            np_buttons_wrong = [] 
            for j in range(len(np_buttons)):
                if j != choice:
                    np_buttons_wrong.append(np_buttons[j])
            

            #ITI
            timer_premature=utime.ticks_ms()
            
            while ITI_break == True: #similar to other phase
                
                

                premature_responce_timer = utime.ticks_ms()
                premature_timer= premature_responce_timer - timer_premature
               
                
                 #ITI   
                if premature_timer < ITI: 
                    
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 0:
                        
                        led.value(0)

                        nose_pokes[choice].value(0)
                        

                        premature_responce +=1
                        
                        ITI_break=False
                        time_out = True
                        button_pressed = True
                       
                
                elif premature_timer > ITI:
                   
       
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 1:
                        button_pressed = False
                        ITI_break = False
                        
                
            timer_duration = utime.ticks_ms()
            
            
            #Start of SD
            
            while button_pressed == False:
                task_time= utime.ticks_ms()
                
                nose_pokes[choice].value(1)
                task_duration = task_time-timer_duration
             
                
                if task_duration < SD + extra:   #Within the SD and LH time 
                   #
      
                    if task_duration > SD:
                          nose_pokes[choice].value(0)
                          
                          

                    if np_buttons[choice].value() == 0:                       
                        correct_timer = task_time-timer_duration
                        button_pressed = True
                        
                        #food dispenser is on
                        reward()
                                    
                        led.value(1)
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        
                        timer_fooder= utime.ticks_ms()

                        button_food.value() == 1 
                  
                     
                        while button_food.value() == 1:
                            utime.sleep(0.1)
                            next 
                    
                        led.value(0) 
                        time_food =utime.ticks_ms()
                        mouse_to_food = time_food - timer_fooder 
                        print(mouse_to_food)         
                       
                        
                        correct_responses += 1 #since the mouse has succeeded, we add 1 to our counter of correct_responses
                        utime.sleep(20) 
                        
                       
                        premature_timer=0
                        task_duration=0
                        omissions = 0
                        wrong_button_name=0
                    wrong_button_pressed = None
                    
                    
                    #Wrong button:
                    for button in np_buttons_wrong:
                        if button.value() == 0:
                            
                            wrong_button_pressed = button
                            wrong_button_name = ""
                            
                            for button_variable,np_name in button_correspondance:
                                if button_variable == wrong_button_pressed:
                                 
                                    wrong_button_name = np_name
                                    break
                            

                            led.value(0)
                            nose_pokes[choice].value(0)
                            
                            
                            mouse_to_food = 0
                            correct_time= 0
                            premature_timer = 0
                            omissions=0
                           
                            
                            button_pressed = True
                            time_out = True
                          
                            break
                        
                    
                elif task_duration > SD + extra:
                    
                    button_pressed=True
                    time_out=True
                    
                    task_duration = 0
                    mouse_to_food = 0
                    correct_time= 0
                    premature_timer = 0
                    
                    omissions += 1
                    
                
                    
               #Time out: 
            if time_out == True: 
                led.value(0)
                nose_pokes[choice].value(0)
                mouse_to_food = 0
                correct_time=0
                utime.sleep(5)
                
        
                
            
                
                
            task_end_time= utime.ticks_ms() 
            task_end = task_end_time - start_timer
          
            print('') #linebreak

            end_timer=utime.ticks_ms()
            task_end = end_timer-start_timer
            
            yield([trial, "5", "1", choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name,  omissions, task_end])

    @Device.task
    def stage12_task():
        """Stage 12"""
          
        num_trials = 500
        
        for trial in range(num_trials):
            
             
           
            extra = 4000
            ITI = 5000
           
            nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
            np_buttons = [button_1,button_2,button_3,button_4, button_5]
            
            #variables
            omissions = 0 
            wrong_button_name= None
            task_duration=0
            premature_timer=0
           
        

            #SDs possbility and selectivity
            possible_SDs = [1000,500,200]
            index_current_SD = 0            
            count_trials_five = 0
            count_trials_seven = 0
            count_trials_twelve = 0
            
            #Allows for the SDs to be equally selected/ same as ITI

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
        
        
        
        
            
            start_timer = utime.ticks_ms() #timer for total task

            led.value(1) #starts with food magazine Yellow LED on
            
            while button_food.value() == 1: #this loop waits for the button to be pressed
                timer_food = utime.ticks_ms()
                next
                
            led.value(0)
           
            #conditions for the conditions 
            ITI_break = True
            time_out = False
            button_pressed = False

           
            
            #chosing NP to turn on
            choice = random.randint(0,4)
            print('NP number chosen',choice)
            
            #list of wrong buttons that can be pressed during the game
            np_buttons_wrong = [] 
            for j in range(len(np_buttons)):
                if j != choice:
                    np_buttons_wrong.append(np_buttons[j])
            
            timer_food=utime.ticks_ms() #timer for food
         
            #ITI
            while ITI_break == True:
                
                premature_responce_timer = utime.ticks_ms()
                premature_timer= premature_responce_timer - timer_food
                
                if premature_timer < ITI: #PREMATURE responce
                    
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 0:
                        
                        led.value(0)
                        nose_pokes[choice].value(0)
                        
                        ITI_break=False
                        time_out = True
                        button_pressed = True
                
                elif premature_timer > ITI: #no NPS poked
                   
        
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==1 or np_buttons[choice].value() == 1:
                        button_pressed = False
                        ITI_break = False
                        
                
            timer_duration = utime.ticks_ms()
         
         
         
            while button_pressed == False:
                task_time= utime.ticks_ms()
                
                nose_pokes[choice].value(1) #NP is on
                task_duration = task_time-timer_duration
             
                #Task starts
                if task_duration < selected_SD + extra: #task duration is within the SD and LH
                    
                    if task_duration > selected_SD:
                          nose_pokes[choice].value(0)
                          
                          

                    if np_buttons[choice].value() == 0:  #correct NP poked

                        button_pressed = True
                        correct_time = task_time-timer_duration
                        
                        
                        led.value(1) 
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        
                        time_food= utime.ticks_ms()
                        
                        #food diepsner is on
                        reward()
                                    
                                    
                    
                        button_food.value() == 1 #task stops until the mouse goes towards the food
                        while button_food.value() == 1:
                            utime.sleep(0.1)
                            next 
                    
                    
                        led.value(0) 
                        time_food =utime.ticks_ms()
                        mouse_to_food = time_food - timer_duration 

                        utime.sleep(1) #should be 20 #time out 20 seconds
                        
                        #variables that are 0  
                        premature_timer=0
                        task_duration=0
                        omissions = 0
                        wrong_button_name=0
                    
                    wrong_button_pressed = None
                    
                    
                    for button in np_buttons_wrong: #In case of wrong NP poked
                        if button.value() == 0: 
                           
                            wrong_button_pressed = button
                            wrong_button_name = ""
                            
                            for button_variable,np_name in button_correspondance:
                                if button_variable == wrong_button_pressed:
                                    wrong_button_name = np_name
                                    break
                            
                       
                            led.value(0)
                            nose_pokes[choice].value(0)
                            
                            
                            mouse_to_food = 0
                            correct_time= 0
                            premature_timer = 0
                            omissions=0
                           
                            
                            button_pressed = True
                            time_out = True
                            break
                    
                        
                    
                elif task_duration > selected_SD + extra: #Omission

                    button_pressed=True
                    time_out=True
                     
                    task_duration = 0
                    mouse_to_food = 0
                    correct_time= 0
                    premature_timer = 0
                    omissions += 1
                    
                      
                
            if time_out == True: #Time out
                led.value(0)
                nose_pokes[choice].value(0)
                mouse_to_food= 0
                correct_time=0
                utime.sleep(5)
             
            end_timer = utime.ticks_ms() 
            task_end = end_timer-start_timer
                
            yield([trial+1, selected_SD, "1", choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name,  omissions, task_end])


