 @Device.task
    def phase3():
        """Phase 3"""
        total=time.ticks_ms()
        for trial in range(100):
            
            
            
            #Variables of wrong "moves":
            trial_correct = False
            
            wrong_button_name= None # no wrong buttons pressed at teh moment
            premature_timer=0
            
            
             ITI= 5000
            
                        
            start_trial_time= time.ticks_ms() #this is a timer of the start of the trial    
            food_led.value(1) #the food magazine LED value starts at 0
            
            while button_trial.value() == 1:#while the food magazine sensor LEDs are 1 that means there has been no interruption. This means the mouse hasn't reached for the food
                utime.sleep(0.1)          
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
            
            
            
            while ITI_break == True: #while the ITI is under 5000ms
                

                premature_response_timer = time.ticks_ms()
                premature_timer= premature_response_timer - timer_premature
                #print(premature_timer)
                
                    
                if premature_timer < ITI: #while the premature timer is smaller than the ITI:
                    
                                          # If a button is pressed: 
                    if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0  or np_buttons_wrong[3].value()==0 or  np_buttons[choice].value() == 0 :
                        
                        led.value(0) # the food magazine LED remain off

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


            #Start of SD
            
            while button_pressed == False: #While no nosepoke has been pressed the task keeps going:
                np_buttons[choice].value() == 1
                
                
            task_time= time.ticks_ms()
            task_duration = task_time-timer_duration
                        

                nose_pokes[choice].value(0)
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

                    button_food.value() == 1 #task stops until the mouse goes towards the food
                    
                    
                    while button_food.value() == 1: #food sensor turns on and wait for mouse to get pellet
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
                        
                        led.value(0) #food magazine yellow lED is off
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
            task_end = task_end_time - start_timer
            total_task= task_end_time-total
                
            
            yield([trial+1,times_num,  "5", choice, mouse_to_food, premature_timer, wrong_button_name, task_end,total_task])
        
            
            
            
            
            
            