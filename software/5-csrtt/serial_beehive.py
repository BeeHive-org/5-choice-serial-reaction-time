# These are imports necessary to use the belay library
import belay
from belay import Device
import time
#import utime




class SerialBeeHive(Device): #This is the class that contains all the phases 
    
    @Device.setup # Device setup is where the yellow LEDs and sensor LEDs are defined, also imports.
    def setup():

        #these imports are necessary for the different phases
        import machine
        import time 
        import random
        import utime

        #This is for the stepper motor that turns the food dispenser allowing
        #from machine import Pin
        #from machine import PWM
        from machine import ADC
        


        
        #The pins for the servo motor on the pellet dispenser
        dispenser_motor = machine.PWM(Pin(18),freq =50)


        #pins = [IN1, IN2, IN3, IN4]
        magazine_sensor_pin = 15
        dispenser_sensor_pin = 39
        button_trial_pin = 2
        
        

        magazine_sensor = machine.Pin(magazine_sensor_pin,machine.Pin.IN) # Sensor LED for the food magazine
        dispenser_sensor = machine.Pin(dispenser_sensor_pin, machine.Pin.IN) # Sensor LEDs for the food dispenser to detect when food pellets come down
        button_trial = machine.Pin(button_trial_pin, machine.Pin.IN) # Sensor for trial start light
        
        
        food_led = machine.Pin(33, machine.Pin.OUT) #LED = the yellow LED for the food magazine
        
        #All the pins for teh yellow LEDs nose pokes
        NP_1 = machine.Pin(14,machine.Pin.OUT) 
        NP_2 = machine.Pin(27,machine.Pin.OUT)
        NP_3 = machine.Pin(25,machine.Pin.OUT)
        NP_4 = machine.Pin(26, machine.Pin.OUT)
        NP_5 = machine.Pin(32,machine.Pin.OUT)

        #All the IR. sensors for the different Nose pokes
        button_1 = machine.Pin(16,Pin.IN)
        button_2 = machine.Pin(17,Pin.IN) 
        button_3 = machine.Pin(19,Pin.IN)
        button_4 = machine.Pin(21,Pin.IN)
        button_5 = machine.Pin(22,machine.Pin.IN)
        

        
        #This is to associate each button with the Nose poke for the data output on the excel sheet
        button_correspondence = [ (button_1, "NP_1"), (button_2, "NP_2"), (button_3, "NP_3"), (button_4, "NP_4"), (button_5,"NP_5")]


        #This sets all the Nosepoked yellow LED values at 0 before the trial starts
        NP_1.value(0)
        NP_2.value(0)
        NP_3.value(0)
        NP_4.value(0)
        NP_5.value(0)
        
        def count_time(interval):
            timer1 = time.ticks_ms()
            timer2 = time.ticks_ms()
            while timer2-timer1<=interval:
                timer2=time.ticks_ms()
            
            return timer2-timer1
            
        #This is the function for the food dispenser giving the reward:
        
        def reward():
            pellet_dropped = 0 #Pellet is one which allows for the food dispensing to start through the while loop underneath
            reward_servo_mov_time = 800;
            

            while pellet_dropped==0:
                dispenser_motor.duty(50)
                timer1 = time.ticks_ms()
                timer2 = time.ticks_ms()
                while(timer2-timer1<reward_servo_mov_time):
                    pellet = dispenser_sensor.value()
                    #print(pellet)
                    timer2 = time.ticks_ms()
                    if pellet == 0:
                        pellet_dropped = 1
                        break
                
                if pellet_dropped == 0:
                    dispenser_motor.duty(23)
                    timer1 = time.ticks_ms()
                    timer2 = time.ticks_ms()
                    while(timer2-timer1<reward_servo_mov_time):
                        timer2 = time.ticks_ms()
                        pellet = dispenser_sensor.value()     
                        if pellet == 0:
                            pellet_dropped = 1
                            break
        
    @Device.task 
    def food_training(num_trial=50): #this is the function for the food training
        """Food magazine training"""
        
        total=time.ticks_ms()
       


        for trial in range (num_trial): #trials meaning trials that can be changed in the brackets
          
            start_trial_time= time.ticks_ms() #this is a timer of the start of the trial -> gives number in miliseconds not actual time   


            food_led.value(1) #the food magazine LED value starts at 0
            reward() 
            #food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off

            
            timer_food = time.ticks_ms()# timer starts to know when the mouse went for the food
            timer_food2 = time.ticks_ms()
            #print(magazine_sensor.value())
            while magazine_sensor.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                utime.sleep(0.1)
                timer_food2=time.ticks_ms() # as soon as the magazine_sensor.value(1), it starts counting          
            food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off
            
            #ITIs
            times=[4,8,16,32] 
            
            times_num = random.choice(times) #one random time out of these is chosen
            #times_num = times_num*1000 #convert seconds to milliseconds
            count_time(times_num) # time.sleeps allows for the machine to pause for the amount of times the ITI is
            
            
            mouse_to_food = timer_food2-timer_food #mouse to food is the amount of time the mouse took to get the food
            end_trial_time = time.ticks_ms()
            
            trial_duration = end_trial_time-start_trial_time #end of the whole task
            
            timer_end = utime.ticks_ms()
            total_time=timer_end-total # end of the whole task
            
    
            
            yield([trial+1, times_num, start_trial_time, mouse_to_food, trial_duration, total_time])  #variables that are going to be yielded into the CSV file

    @Device.task
    def phase1():
        
        """Phase 1"""
        
        total=time.ticks_ms()
        
        for trial in range (50):
            
            start_trial_time= time.ticks_ms() #this is a timer of the start of the trial -> gives number in miliseconds not actual time   
            food_led.value(1) #the food magazine LED value starts at 0
            
            while button_trial.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                print(button_trial.value())
                utime.sleep(0.5)
               
            food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off
            reward()
            
            timer_food = time.ticks_ms()# timer starts to know when the mouse went for the food
            
            while magazine_sensor.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                
                utime.sleep(0.1)
                timer_food2=time.ticks_ms() # as soon as the magazine_sensor.value(1), it starts counting  
            food_led.value(0) #the food magazine LED value starts at 0 
            
            mouse_to_food = timer_food2-timer_food #mouse to food is the amount of time the mouse took to get teh food
            end_trial_time = time.ticks_ms()

            trial_duration = end_trial_time-start_trial_time #end of the whole task

            timer_end = utime.ticks_ms()
            total_time=timer_end-total # end of the whole task

            yield([trial+1,start_trial_time, mouse_to_food, trial_duration, total_time])  #variables that are going to be yielded into the CSV file

    @Device.task
    def phase2():
        
        """Phase 2"""
        total=time.ticks_ms()
        
        for trial in range (50):
            
            start_trial_time= time.ticks_ms() #this is a timer of the start of the trial    
            food_led.value(1) #the food magazine LED value starts at 0
            
            while button_trial.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                print(button_trial.value())
                utime.sleep(0.5)          
            food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off
            
            button_pressed = False
            
            while button_pressed== False: #this a while loop that allows for the conditions 
    
                #if any of the buttons are interrupted the sensor will go from 1 to 0 showing an interruption
                #Here one of the Nosepokes has been poked
                if button_1.value() == 0 or button_2.value() == 0  or button_3.value() == 0  or button_4.value() == 0 or button_5.value()==0: #if any of the NPs are poked
                      
                    #Lights are turned off
                    NP_1.value(0) 
                    NP_2.value(0)
                    NP_3.value(0)
                    NP_4.value(0)
                    NP_5.value(0)
                    
                    #Reward is sent
                    reward()
                    
                    timer_food = time.ticks_ms()

                    while magazine_sensor.value() == 1:
                        timer_food2 = time.ticks_ms()
                        
                    mouse_to_food = timer_food2-timer_food
                    
                    button_pressed = True #when the button pressed is true then the while loop can stop and the trial can go again
                    
                    trial_end = time.ticks_ms()
                    trial_duration = trial_end-start_trial_time
                           
                #If no NPs are pressed then nothing happens
                elif button_1.value() == 1 or button_2.value() == 1 or button_3.value() == 1 or button_4.value() == 1 or button_5.value() == 1:#0 meaning the NPs haven't been touched     
                        NP_1.value(1) #THE Lights remain on
                        NP_2.value(1)
                        NP_3.value(1)
                        NP_4.value(1)
                        NP_5.value(1)
                        food_led.value(0)
                        
            timer_end = utime.ticks_ms()
            total_time=timer_end-total # end of the whole task
            
            #yield([trial+1, mouse_to_food, start_trial_time,trial_duration])   
            yield([trial+1, start_trial_time, mouse_to_food, trial_duration, total_time])



    @Device.task
    def phase3():
        """Phase 3"""
       
        total=time.ticks_ms()
        for trial in range(100):
            
            
            premature_response=0
            mouse_to_food =0
            correct_time=0
            task_duration=0
            
            #Variables of wrong "moves":
            trial_correct = False
            
            wrong_button_name= None # no wrong buttons pressed at teh moment
            premature_timer=0
            
            premature_response=0
            mouse_to_food =0
            correct_time=0
            task_duration=0
           
            
            ITI= 5000
            
                        
            start_trial_time= time.ticks_ms() #this is a timer of the start of the trial    
            food_led.value(1) #the food magazine LED value starts at 0
            
            while button_trial.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                print(button_trial.value())
                utime.sleep(0.5)          
            food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off
    
            #matching accumulating all the NP and button into lists
            nose_pokes = [NP_1,NP_2,NP_3,NP_4, NP_5]
            np_buttons = [button_1,button_2,button_3,button_4, button_5]
            
            #random choice between NP1 to NP5 (0 to 4)
            choice = random.randint(0,4)
            
          #ITI:
            ITI_break = True
            time_out = False
            button_pressed = True
            
            choice = random.randint(0,4)
          
            #list of wrong buttons that can be pressed during the game
            np_buttons_wrong = [] 
            for f in range(len(np_buttons)):
                if f != choice:
                    np_buttons_wrong.append(np_buttons[f]) #it creates a list of all the NPs apart from NP choice which will be the correct one
            
            
            timer_premature=time.ticks_ms() #timer for premature responses
            while ITI_break == True: #while the ITI is under 5000ms
                

                premature_response_timer = time.ticks_ms()
                premature_timer= premature_response_timer - timer_premature
                
                
                #print(premature_timer)
                
                    
                if premature_timer < ITI: #while the premature timer is smaller than the ITI:
                    
                                          # If a button is pressed: 
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0  or np_buttons_wrong[3].value()==0 or  np_buttons[choice].value() == 0 :
                        
                        food_led.value(0) # the food magazine LED remain off

                        nose_pokes[choice].value(0) #the correct NP is turned off
                        

                        #premature response is added to criteria calculator
                        #time.sleep(5)
                        ITI_break=False #the ITI_break loop ends
                        time_out = True #The mouse goes trhough a time out
                        button_pressed = True #A nose poke has been poked
                       # print("premature")
                        
                        #All variables that remain at 0 (not +1)
                        mouse_to_food =0
                        correct_time=0
                        task_duration=0
                        omissions = 0
                        premature_response +=1
                        
                
                elif premature_timer > ITI: #If no button has been pressed
                   
                
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==1 or np_buttons[choice].value() == 1:
                        button_pressed = False #no Nosepoke has been poked 
                        ITI_break = False #the ITI break is over
                        
            
            timer_duration = time.ticks_ms()

            
            #Start of SD
            
            while button_pressed == False: #While no nosepoke has been pressed the task keeps going:
                
                while np_buttons[choice].value() == 1:
                    nose_pokes[choice].value(1)
                
                
                task_time= time.ticks_ms()
                task_duration = task_time-timer_duration
                            

                if np_buttons[choice].value() == 0:   #this means the correct button has been pressed  
                    
                    correct_time = task_time-timer_duration  #timer for when the mouse got the correct response                     
                    button_pressed = True #A NP has been poked
                    
                    NP_1.value(0)
                    NP_2.value(0)
                    NP_3.value(0)
                    NP_4.value(0)
                    NP_5.value(0)
                    #food dispenser is on
                    reward()
                        
                    timer_fooder= time.ticks_ms() #timer mouse to food

                    magazine_sensor.value() == 1 #task stops until the mouse goes towards the food
                    
                    
                    while magazine_sensor.value() == 1: #food sensor turns on and wait for mouse to get pellet
                        time.sleep(0.1)
                        next
                        
                
                
                    time_food =time.ticks_ms()
                
                    mouse_to_food = time_food - timer_fooder #mouse to food timer
                    
                    #correct_response += 1 #since the mouse has succeeded, we add 1 to our counter of correct_response
        
                    premature_timer = 0
                    wrong_button_name = 0
                    
                
                wrong_button_pressed = None #no wrong NP has been poked
                
                for button in np_buttons_wrong:  #Within the NP in the list of wrong NPs
                    
                    
                    if button.value() == 0: #If a wrong NP has been pressed
                       
                        wrong_button_pressed = button
                        wrong_button_name = ""
                        
                        #code to know which wrong NP has been pressed in the case of an incorrect NP has been poked and relate it back to the NP through the button_correspondence
                        for button_variable,np_name in button_correspondence:
                            if button_variable == wrong_button_pressed:
                                wrong_button_name = np_name #teh wrong NP = to the NP_name (it's associating the sensor to the correct NP)
                                break
                        
                        food_led.value(0) #food magazine yellow lED is off
                        nose_pokes[choice].value(0) #Correct NP light turns off
                        
                        #incorrect_response +=1
                        
                        
                        mouse_to_food = 0
                        correct_time= 0
                        premature_timer = 0
                        #button has been pressed but since it was incorrect then time out is also true
                        button_pressed = True
                        time_out = True
            
                        break
                
        
        
        
            if time_out == True: #When time out was true then
                
                food_led.value(0)
                nose_pokes[choice].value(0)
                
                #for when yielding the data, need to specifiy that mouse_to_food and correct response are 0
                mouse_to_food = 0
                correct_time = 0
                
                #time out needs to be that the trial starts again
                trial_correct= False #Should go back up to the beginning where the trial_correct variable started by being false?
            
            task_end_time= time.ticks_ms() 
            task_end = task_end_time - start_trial_time
            total_task= task_end_time-total
                
            
            yield([trial+1, "5", choice, mouse_to_food, premature_timer, wrong_button_name, task_end,total_task])
        
    
            
    @Device.task
    def stage_5csrtt_task():
        """5 choice serial task"""
        
        #Need to set the counter to 0 for all the variables that are going to be "calculated"
        correct_response = 0 #counter for when the mouse has pressed the right button
        omissions = 0 #counter of when no button is pressed
        premature_response=0 
        incorrect_response=0
        accuracy_percentage = 0 
        omission_percentage=0
        index_current_SD = 0 #the index of which SD is on within the possible SDs
        omission_counter =0
        
        
        
        winSize = 20 # window size for the moving average
        winIndex = 0 # index of the moving average window
        accMvgAverage = [0]*winSize # list with number of elements equal to the moving average window size
        omMvgAverage = [0]*winSize # list with number of elements equal to the moving average window size



        total=time.ticks_ms()
        #Start of task

        for trial in range(100000): #providing an unlimitted amount of trials

        #variables are placed inside the for loop because they're value needs to reset every trial to not add up
             
            wrong_button_name= None # no wrong buttons pressed at teh moment
            premature_timer=0  
            omissions=0
            
            #ITI/SD AND LH:
            extra = 4000
            ITI= 5000
            
        
            possible_SDs = [16000,8000,4000,2000,1500]#,1000]  #all teh SDs as the phase progresses
            current_SD= possible_SDs[index_current_SD] #The current SD is teh SD that is being executed if teh criteria has been met
            
            if current_SD==1000: #once it reaches sd of 1 second the whole loop stops and it moves on to the next phase
                break
            
            nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
            np_buttons = [button_1,button_2,button_3,button_4, button_5,button_trial]
                    
            start_timer = time.ticks_ms()
            
            #start of the trial
               
            food_led.value(1) #the food magazine LED value starts at 0
            
            while button_trial.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
               print(button_trial.value())
               utime.sleep(0.5)          
            food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off
            
           
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
            

            print("Start of ITI")
            timer_premature=time.ticks_ms() #timer for premature response
            
            while ITI_break == True: #while the ITI is under 5000ms
                

                premature_response_timer = time.ticks_ms()
                premature_timer= premature_response_timer - timer_premature
                #print(premature_timer)
                
                    
                if premature_timer < ITI: #while the premature timer is smaller than the ITI:
                    
                                          # If a button is pressed: 
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0  or np_buttons_wrong[3].value()==0 or  np_buttons[choice].value() == 0 :
                        
                        food_led.value(0) # the food magazine LED remain off

                        nose_pokes[choice].value(0) #the correct NP is turned off
                        

                        premature_response +=1 #premature response is added to criteria calculator
                        #time.sleep(5)
                        ITI_break=False #the ITI_break loop ends
                        time_out = True #The mouse goes trhough a time out
                        button_pressed = True #A nose poke has been poked
                       # print("premature")
                        
                        #All variables that remain at 0 (not +1)
                        mouse_to_food =0
                        correct_time=0
                        task_duration=0
                        omissions = 0
                
                elif premature_timer > ITI: #If no button has been pressed
                   
                
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==1 or np_buttons[choice].value() == 1:
                        button_pressed = False #no Nosepoke has been poked 
                        ITI_break = False #the ITI break is over
                        
            
            timer_duration = time.ticks_ms()

            print("start of SD")
            #Start of SD
            nose_pokes[choice].value(1)
            while button_pressed == False: #While no nosepoke has been pressed the task keeps going:
                task_time= time.ticks_ms()
                
               # nose_pokes[choice].value(1)
                task_duration = task_time-timer_duration
             
                
                if task_duration < current_SD + extra:   #this makes it so that the buttons are still active for 4 seconds after the led value is turned off
                    
            
                    if task_duration > current_SD:
                          nose_pokes[choice].value(0) #After the SD time has passed the yellow LED turns off but there is still the LH
                          
                          

                    if np_buttons[choice].value() == 0:   #this means the correct button has been pressed  
                        
                        correct_time = task_time-timer_duration  #timer for when the mouse got the correct response                     
                        button_pressed = True #A NP has been poked
                        
                        
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        #food dispenser is on
                        reward()
                            
                        timer_fooder= time.ticks_ms() #timer mouse to food

                        magazine_sensor.value() == 1 #task stops until the mouse goes towards the food
                        
                        
                        while magazine_sensor.value() == 1: #food sensor turns on and wait for mouse to get pellet
                            print(magazine_sensor.value())
                            time.sleep(0.5)
                            next
                            
                    
                    
                        time_food =time.ticks_ms()
                     
                        
                        mouse_to_food = time_food - timer_fooder #mouse to food timer
                        
                        correct_response += 1 #since the mouse has succeeded, we add 1 to our counter of correct_response
                       
                        #time.sleep(20) #eating period
                        
                        premature_timer=0
                        task_duration=0
                        omissions = 0
                        wrong_button_name=0
                        
                    
                    wrong_button_pressed = None #no wrong NP has been poked
                    
                    for button in np_buttons_wrong:  #Within the NP in the list of wrong NPs
                        
                        
                        if button.value() == 0: #If a wrong NP has been pressed
                           
                            wrong_button_pressed = button
                            wrong_button_name = ""
                            
                            #code to know which wrong NP has been pressed in the case of an incorrect NP has been poked and relate it back to the NP through the button_correspondence
                            for button_variable,np_name in button_correspondence:
                                if button_variable == wrong_button_pressed:
                                    wrong_button_name = np_name #teh wrong NP = to the NP_name (it's associating the sensor to the correct NP)
                                    break
                            
                            food_led.value(0) #food magazine yellow lED is off
                            nose_pokes[choice].value(0) #Correct NP light turns off
                            
                            incorrect_response +=1
                            
                            
                            mouse_to_food = 0
                            correct_time= 0
                            premature_timer = 0
                            omissions=0
                           
                            #button has been pressed but since it was incorrect then time out is also true
                            button_pressed = True
                            time_out = True
                
                            break
                        
                    
                elif task_duration > current_SD + extra:# if the task duration is higher than the SD and the LH then that means omission
                  
                    button_pressed=True
                    time_out=True
                    
                    omissions += 1
                    task_duration = 0
                    mouse_to_food = 0
                    correct_time= 0
                    premature_timer = 0
                    
                    omission_counter +=1
                    
                    #In this case there are two omission counters but this can be edited based on how the person wants to output their data.
                    #Here one of the omissions is used to output "1" every time there is an omission and the other is a counter to measure the omission percentage.  
                    
                
            if time_out == True: #When time out was true then
                food_led.value(0)
                nose_pokes[choice].value(0)
                
                #for when yielding the data, need to specifiy that mouse_to_food and correct response are 0
                mouse_to_food = 0
                correct_time=0
                
                time.sleep(5) #whole system is off for 5 seconds
                
                
            task_end_time= time.ticks_ms() 
            task_end = task_end_time - start_timer
            total_task= task_end_time-total
            print(task_end)
            print('') #linebreak
            
            #Calculating the accuracy percentage and the omissions percentage for the criteria
            
            accuracy_percentage = 100 # Here in order to not divide 1 correct response by 0 in case there is no incorrect response we just say that correct response is 100%

            if incorrect_response > 0: #unless incorrect response is higher than 0, which then the accuracy percentage can be calculated
                accuracy_percentage = (correct_response/(correct_response+incorrect_response))*100
            accMvgAverage[winIndex] = accuracy_percentage
            
            #Same logic here. If omission counter is 0 then the the percentage is 0 unless omission counter is bigger than 0.
            if omission_counter == 0:
                omission_percentage = 0
            elif omission_counter > 0:
                omission_percentage= (omission_counter/ (correct_response+incorrect_response+omission_counter))*100
           # print(omission_percentage,"omission")

            omMvgAverage[winIndex] = omission_percentage

            winIndex = winIndex+1
            print(winIndex, "windex")
            if winIndex == winSize:
                winIndex = 0
            
            if trial>=winSize:
                accuracy_average = sum(accMvgAverage)/winSize
                omission_average = sum(omMvgAverage)/winSize
            else:
                accuracy_average = 1
                omission_average = 1
                
                
                
            
            print(accuracy_average, "accuracy ")
            print(omission_average, "omissions")
                
         
            

           
            #SD will decrease if these conditions are met
            if trial > 50 and accuracy_average >= 60:
                if omission_average <= 30 or correct_response >= 200:  #the accuracy is 60 percent or more and omission percentage is less than 30 percent then        
                    index_current_SD += 1 #condition is met then the Stimulus duration decreases according to the list from the beginning.
                    print("SD criteia moved up")
      
       
            yield([trial+1,ITI, current_SD, choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name, omissions,omission_percentage ,accuracy_percentage, windIndex, accuracy_average, omission_average,  task_end,total_task])
            
            if index_current_SD == len(possible_SDs): #checking that we are not at the end of the list
                print("animal has reached lowest SD criteria. Exiting phase...")
                return




  
    @Device.task
    def stage9_task():
        """stage 9"""
        button_correspondence = [ (button_1, "NP_1"), (button_2, "NP_2"), (button_3, "NP_3"), (button_4, "NP_4"), (button_5,"NP_5")]
        correct_response = 0 #counter for when the mouse has pressed the right button
        omissions = 0 #counter of when no button is pressed
        premature_response=0 
        incorrect_response=0
        total=time.ticks_ms()
        #Start of task
        for trial in range(1000): #providing an unlimited amount of trials

        #variables are placed inside the for loop because they're value needs to reset every trial to not add up
             
            wrong_button_name= None # no wrong buttons pressed at teh moment
            premature_timer=0  
            omissions=0
            
            #ITI/SD AND LH:
            extra = 4000
            ITI= 5000
            SD = 1000
            
            nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
            np_buttons = [button_1,button_2,button_3,button_4, button_5]
                    
            start_timer = time.ticks_ms()
            
            #start of the trial
            food_led.value(1) #Food magazine yellow LED turns on to start the trial
            
            while button_trial.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                utime.sleep(0.1)          
            food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off
            
           
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
            

            
            timer_premature=time.ticks_ms() #timer for premature response
            
            while ITI_break == True: #while the ITI is under 5000ms
                

                premature_response_timer = time.ticks_ms()
                premature_timer= premature_response_timer - timer_premature
                #print(premature_timer)
                
                    
                if premature_timer < ITI: #while the premature timer is smaller than the ITI:
                    
                                          # If a button is pressed: 
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0  or np_buttons_wrong[3].value()==0 or  np_buttons[choice].value() == 0:
                        
                        food_led.value(0) # the food magazine LED remain off

                        nose_pokes[choice].value(0) #the correct NP is turned off
                        

                        premature_response +=1 #premature response is added to criteria calculator
                        #time.sleep(5)
                        ITI_break=False #the ITI_break loop ends
                        time_out = True #The mouse goes through a time out
                        button_pressed = True #A nose poke has been poked
                       # print("premature")
                        
                        #All variables that remain at 0 (not +1)
                        mouse_to_food =0
                        correct_time=0
                        task_duration=0
                        omissions = 0
                
                elif premature_timer > ITI: #If no button has been pressed              
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==1 or np_buttons[choice].value() == 1:
                        button_pressed = False #no Nosepoke has been poked 
                        ITI_break = False #the ITI break is over

            timer_duration = time.ticks_ms()

            #Start of SD
            nose_pokes[choice].value(1)
            while button_pressed == False: #While no nosepoke has been pressed the task keeps going:
                
                task_time= time.ticks_ms()
                task_duration = task_time-timer_duration
                
                
                if task_duration < SD + extra:   #this makes it so that the buttons are still active for 4 seconds after the led value is turned off
                  
                    #if task_duration <= SD:
                        
                        
                    if task_duration > SD:
                        nose_pokes[choice].value(0)
                            

                    #nose_pokes[choice].value(0)
                    if np_buttons[choice].value() == 0:   #this means the correct button has been pressed  
                        
                        correct_time = task_time-timer_duration  #timer for when the mouse got the correct response                     
                        button_pressed = True #A NP has been poked
                        
                        
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        #food dispenser is on
                        reward()
                            
                        timer_fooder= time.ticks_ms() #timer mouse to food

                        #magazine_sensor.value() == 1 #task stops until the mouse goes towards the food
                        
                        
                        while magazine_sensor.value() == 1: #food sensor turns on and wait for mouse to get pellet
                            time.sleep(0.1)
                            #next
                            
                    
                    
                        time_food =time.ticks_ms()
                        
                        mouse_to_food = time_food - timer_fooder #mouse to food timer
                        
                        #correct_response += 1 #since the mouse has succeeded, we add 1 to our counter of correct_response
                       
                        time.sleep(20) #eating period
                        
                        premature_timer = 0
                        task_duration = 0
                        omissions = 0
                        wrong_button_name = 0
                        
                    
                    wrong_button_pressed = None #no wrong NP has been poked
                    
                    for button in np_buttons_wrong:  #Within the NP in the list of wrong NPs
                        
                        
                        if button.value() == 0: #If a wrong NP has been pressed
                           
                            wrong_button_pressed = button
                            wrong_button_name = ""
                            
                            #code to know which wrong NP has been pressed in the case of an incorrect NP has been poked and relate it back to the NP through the button_correspondence
                            for button_variable,np_name in button_correspondence:
                                if button_variable == wrong_button_pressed:
                                    wrong_button_name = np_name #teh wrong NP = to the NP_name (it's associating the sensor to the correct NP)
                                    break
                            
                            food_led.value(0) #food magazine yellow lED is off
                            nose_pokes[choice].value(0) #Correct NP light turns off
                            
                            #incorrect_response +=1
                            
                            
                            mouse_to_food = 0
                            correct_time= 0
                            premature_timer = 0
                            omissions=0
                           
                            #button has been pressed but since it was incorrect then time out is also true
                            button_pressed = True
                            time_out = True
                
                            break
                        
                    
                elif task_duration > SD + extra:# if the task duration is higher thna the SD and the LH then that means omission
                  
                    button_pressed=True
                    time_out=True
                    
                    omissions = 1
                    #total_omissions += 1
                    task_duration = 0
                    mouse_to_food = 0
                    correct_time= 0
                    premature_timer = 0
                    
                
                    #In this case there are two omission counters but this can be edited based on how the person wants to output their data.
                    #Here one of the omissions is used to output "1" every time there is an omission and the other is a counter to measure the omission percentage.  
                    
                
            if time_out == True: #When time out was true then
                
                food_led.value(0)
                nose_pokes[choice].value(0)
                
                #for when yielding the data, need to specifiy that mouse_to_food and correct response are 0
                mouse_to_food = 0
                correct_time = 0
                
                time.sleep(5) #whole system is off for 5 seconds
                
            #print(task_duration)
            #print(wrong_button_name)
            task_end_time= time.ticks_ms() 
            task_end = task_end_time - start_timer
            total_task= task_end_time-total
            #print(task_end)
            print('') #linebreak
            
           
       
            yield([trial+1,ITI, SD, choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name, omissions, task_end,total_task])



    @Device.task
    def stage10_task():
        """stage 10"""
         #variables and trials:
       

        #SD, ITI AND LH:
        SD=1000
        extra = 4000
       
        nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
        np_buttons = [button_1,button_2,button_3,button_4,button_5]
        total=time.ticks_ms()

        #start of trials
        num_trials=500
        for trial in range(num_trials):
            
            wrong_button_name= None
            omissions = 0 
            task_duration=0
            premature_timer=0
            
            #Long code to make sure that the varITIs are equally distributed
            possible_ITIs = [5000,7500,12500] #the possible ITIs
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
                if 5000 in possible_ITIs and count_trials_five == 167:
                    possible_ITIs.remove(5000)
                if 7500 in possible_ITIs and count_trials_seven == 167:
                    possible_ITIs.remove(7500)
                if 12500 in possible_ITIs and count_trials_twelve == 167:
                    possible_ITIs.remove(12500)


            
            start_timer = time.ticks_ms()
            
            
            #Task starts
            food_led.value(1) #Food magazine yellow LED turns on to start the trial
            
            while button_trial.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                utime.sleep(0.1)          
            food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off
            
           
            ITI_break = True
            time_out = False
            button_pressed = False
            
            
        #chosing a NP
            choice = random.randint(0,4)
            np_buttons_wrong = [] 
            for j in range(len(np_buttons)):
                if j != choice:
                    np_buttons_wrong.append(np_buttons[j])
            
            
            timer_food=time.ticks_ms()
            
      #ITI
            while ITI_break == True:
                
                premature_response_timer = time.ticks_ms()
                premature_timer= premature_response_timer - timer_food
                
                if premature_timer < selected_ITI:# 5000:
                    
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 0:
                        
                       
                         

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
                        
                
            timer_duration = time.ticks_ms()
            
           
           #Start of SD
            nose_pokes[choice].value(1)
            while button_pressed == False: #While no nosepoke has been pressed the task keeps going:
                
                task_time= time.ticks_ms()
                task_duration = task_time-timer_duration
                
                
                if task_duration < SD + extra:   #this makes it so that the buttons are still active for 4 seconds after the led value is turned off
                        
                    if task_duration > SD:
                        nose_pokes[choice].value(0)
                            

                    #nose_pokes[choice].value(0)
                    if np_buttons[choice].value() == 0:   #this means the correct button has been pressed  
                        
                        correct_time = task_time-timer_duration  #timer for when the mouse got the correct response                     
                        button_pressed = True #A NP has been poked
                        
                        
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        #food dispenser is on
                        reward()
                        
                        timer_fooder= time.ticks_ms() #timer mouse to food

                        magazine_sensor.value() == 1 #task stops until the mouse goes towards the food
                        
                        
                        while magazine_sensor.value() == 1: #food sensor turns on and wait for mouse to get pellet
                            time.sleep(0.1)
                            next
                            
                    
                    
                        time_food =time.ticks_ms()
                        
                        
                        mouse_to_food = time_food - timer_fooder #mouse to food timer
                        
                        #correct_response += 1 #since the mouse has succeeded, we add 1 to our counter of correct_response
                       
                        time.sleep(20) #eating period
                        
                        premature_timer = 0
                        task_duration = 0
                        omissions = 0
                        wrong_button_name = 0
                        
                        
                    
                    wrong_button_pressed = None
                    
                    #Wrong NP
                    for button in np_buttons_wrong:
                        if button.value() == 0:
                           
                            wrong_button_pressed = button
                            wrong_button_name = ""
                            
                            for button_variable,np_name in button_correspondence:
                                if button_variable == wrong_button_pressed:
                                  
                                    wrong_button_name = np_name
                                    break
                            
                
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
                food_led.value(0)
                nose_pokes[choice].value(0)
                mouse_to_food = 0
                correct_time=0
                time.sleep(5)
                
                
            
            print(wrong_button_name)
            print(task_duration)
            end_timer=time.ticks_ms()
            task_end = end_timer-start_timer
            total_task= end_timer-total
            
            yield([trial+1, selected_ITI, "1", choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name,  omissions, task_end,total_task])

                

    @Device.task
    def stage11_task():
        """stage 11"""
    
        num_trials = 500 #another way to place number of trials
        nose_pokes = [NP_1,NP_2, NP_3, NP_4, NP_5]
        np_buttons = [button_1,button_2,button_3,button_4, button_5]
       
        
        total = time.ticks_ms()
        for trial in range(num_trials):
               
            start_time=time.ticks_ms()
           
            omissions = 0  #there's no timer for omission therefore every start of the trial omission needs to be set back to 0 so it doens't add up
            wrong_button_name= None #no wrong NPs pressed
            
            
            #ITI/SD AND LH:
            extra = 4000
            ITI= 5000
            SD = 1000
            
                
            start_timer = time.ticks_ms()

            food_led.value(1) #Food magazine yellow LED turns on to start the trial
            
            while button_trial.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                utime.sleep(0.1)          
            food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off
           
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
            timer_premature=time.ticks_ms()
            
            while ITI_break == True: #similar to other phase
                
                

                premature_response_timer = time.ticks_ms()
                premature_timer= premature_response_timer - timer_premature
               
                
                 #ITI   
                if premature_timer < ITI: 
                    
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 0:
                        
                        food_led.value(0)

                        nose_pokes[choice].value(0)
                        

                        premature_response +=1
                        
                        ITI_break=False
                        time_out = True
                        button_pressed = True
                       
                
                elif premature_timer > ITI:
                   
       
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 1:
                        button_pressed = False
                        ITI_break = False
                        
                
            timer_duration = time.ticks_ms()
            
            
           #Start of SD
            nose_pokes[choice].value(1)
            while button_pressed == False: #While no nosepoke has been pressed the task keeps going:
                
                task_time= time.ticks_ms()
                task_duration = task_time-timer_duration
                
                
                if task_duration < SD + extra:   #this makes it so that the buttons are still active for 4 seconds after the led value is turned off
                  
                    #if task_duration < SD:
                       
                        
                        if task_duration > SD:
                            nose_pokes[choice].value(0)
                            

                    #nose_pokes[choice].value(0)
                        if np_buttons[choice].value() == 0:   #this means the correct button has been pressed  
                        
                            correct_time = task_time-timer_duration  #timer for when the mouse got the correct response                     
                            button_pressed = True #A NP has been poked
                        
                       
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        #food dispenser is on
                        reward()
                        
                        timer_fooder= time.ticks_ms() #timer mouse to food

                        magazine_sensor.value() == 1 #task stops until the mouse goes towards the food
                        
                        
                        while magazine_sensor.value() == 1: #food sensor turns on and wait for mouse to get pellet
                            time.sleep(0.1)
                            next
                            
                    
                    
                        time_food =time.ticks_ms()
                       
                        mouse_to_food = time_food - timer_fooder #mouse to food timer
                        
                        #correct_response += 1 #since the mouse has succeeded, we add 1 to our counter of correct_response
                       
                        time.sleep(20) #eating period
                        
                        premature_timer = 0
                        task_duration = 0
                        omissions = 0
                        wrong_button_name = 0
                        
                        
                wrong_button_pressed = None
                    
                    
                    #Wrong button:
                for button in np_buttons_wrong:
                    if button.value() == 0:
                            
                        wrong_button_pressed = button
                        wrong_button_name = ""
                            
                        for button_variable,np_name in button_correspondence:
                            if button_variable == wrong_button_pressed:
                                 
                                wrong_button_name = np_name
                                break
                            

                        nose_pokes[choice].value(0)
                            
                        mouse_to_food = 0
                        correct_time= 0
                        premature_timer = 0
                        omissions=0
                           
                            
                        button_pressed = True
                        time_out = True
                          
                        break
                        
                    
                    if task_duration > SD + extra:
                    
                        button_pressed=True
                        time_out=True
                    
                        task_duration = 0
                        mouse_to_food = 0
                        correct_time= 0
                        premature_timer = 0
                    
                        omissions += 1


               #Time out: 
            if time_out == True: 
               
                nose_pokes[choice].value(0)
                mouse_to_food = 0
                correct_time=0
                time.sleep(5)
                
        

          
            print('') #linebreak

            end_timer=time.ticks_ms()
            task_end = end_timer-start_timer
            total_time = end_timer - total
            
            yield([trial, "5", "1", choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name,  omissions, task_end,total_time])

    @Device.task
    def stage12_task():
        """Stage 12"""
        
        num_trials = 500
        total = time.ticks_ms()
        
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
            count_trials_one = 0
            count_trials_five = 0
            count_trials_two = 0
            
            #Allows for the SDs to be equally selected/ same as ITI

            for i in range(num_trials):
                selected_SD = possible_SDs[random.randint(0,len(possible_SDs)-1)]
                if selected_SD == 1000:
                    count_trials_one += 1
                elif selected_SD == 500:
                    count_trials_five +=1
                elif selected_SD == 200:
                    count_trials_two +=1
                    
                if 1000 in possible_SDs and count_trials_one == 167:
                    possible_SDs.remove(1000)
                if 500 in possible_SDs and count_trials_five == 167:
                    possible_SDs.remove(500)
                if 200 in possible_SDs and count_trials_two == 167:
                    possible_SDs.remove(200)
        
        
        
        
            
            start_timer = time.ticks_ms() #timer for total task

            food_led.value(1) #Food magazine yellow LED turns on to start the trial
            
            while button_trial.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                utime.sleep(0.1)          
            food_led.value(0)# once the mouse went for the food, the while loop stops and the food magazine yellow LED turns off
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
            
            timer_food=time.ticks_ms() #timer for food
         
            #ITI
            while ITI_break == True:
                
                premature_response_timer = time.ticks_ms()
                premature_timer= premature_response_timer - timer_food
                
                if premature_timer < ITI: #PREMATURE response
                    
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons_wrong[3].value()==0 or np_buttons[choice].value() == 0:
                        
                       
                        nose_pokes[choice].value(0)
                        
                        ITI_break=False
                        time_out = True
                        button_pressed = True
                
                elif premature_timer > ITI: #no NPS poked
                   
        
                    if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons_wrong[3].value()==1 or np_buttons[choice].value() == 1:
                        button_pressed = False
                        ITI_break = False
                        
                
            timer_duration = time.ticks_ms()
         
         
           #Start of SD
            nose_pokes[choice].value(1)
            while button_pressed == False: #While no nosepoke has been pressed the task keeps going:
                
                task_time= time.ticks_ms()
                task_duration = task_time-timer_duration
                
                
                if task_duration < selected_SD + extra:   #this makes it so that the buttons are still active for 4 seconds after the led value is turned off
                  
                    #if task_duration < SD:
                        
                        
                        if task_duration > selected_SD:
                            nose_pokes[choice].value(0)
                            

                    #nose_pokes[choice].value(0)
                if np_buttons[choice].value() == 0:   #this means the correct button has been pressed  
                        
                        correct_time = task_time-timer_duration  #timer for when the mouse got the correct response                     
                        button_pressed = True #A NP has been poked
                        
                      
                        NP_1.value(0)
                        NP_2.value(0)
                        NP_3.value(0)
                        NP_4.value(0)
                        NP_5.value(0)
                        #food dispenser is on
                        reward()
                                    
                        timer_fooder= time.ticks_ms() #timer mouse to food

                        magazine_sensor.value() == 1 #task stops until the mouse goes towards the food
                        
                        
                        while magazine_sensor.value() == 1: #food sensor turns on and wait for mouse to get pellet
                            time.sleep(0.1)
                            next
                            
                    
                    
                        time_food =time.ticks_ms()
                       
                        
                        mouse_to_food = time_food - timer_fooder #mouse to food timer
                        
                        #correct_response += 1 #since the mouse has succeeded, we add 1 to our counter of correct_response
                       
                        time.sleep(20) #eating period
                        
                        premature_timer = 0
                        task_duration = 0
                        omissions = 0
                        wrong_button_name = 0
                        
                wrong_button_pressed = None
                    
                    
                for button in np_buttons_wrong: #In case of wrong NP poked
                    if button.value() == 0: 
                           
                        wrong_button_pressed = button
                        wrong_button_name = ""
                            
                        for button_variable,np_name in button_correspondence:
                            if button_variable == wrong_button_pressed:
                                wrong_button_name = np_name
                                break
                            
                       
                           
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
               
                nose_pokes[choice].value(0)
                mouse_to_food= 0
                correct_time=0
                time.sleep(5)
             
            end_timer = time.ticks_ms() 
            task_end = end_timer-start_timer
            total_time = end_timer-total
                
            yield([trial+1,'5', selected_SD, choice+1, premature_timer, correct_time, mouse_to_food, task_duration, wrong_button_name,  omissions, task_end,total_time])


