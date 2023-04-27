import csv #CSV imports to excel
import belay #belay library is used as a library that communicates the data from the ESP32 to excel on teh computer
#from belay import Device 
#import time
from serial_beehive import SerialBeeHive #import serial_beehive the file and then the class SerialBeeHive where all the functions are

from datetime import datetime #used to implement dates
now = datetime.now()

print(belay.list_devices()) 
bh = SerialBeeHive('COM5') #SerialBeeHive is now bh
bh.setup() # call the set up function



phases = ["food_training","phase1","phase2", "phase3","stage_5csrtt_task","phase9","phase10","phase11","phase12"]
headers = [ ["Trial","ITI","Start_time","Mouse_food_latency","Trial_duration","total_trial"],
            ["Trial","Start_time","Mouse_food_latency","Trial_duration","total_trial"],
            ["Trial","Start_time","Mouse_food_latency","Trial_duration","total_trial"],
            ["Trial", "ITI", "NP", "Mouse_food_latency", "premature_timer", "wrong NP chosen", "Trial_duration","total_trial"],
            ["Trial","ITI","SD", "NP", "premature_timer", "correct_time", "Mouse_food_latency", "task_duration", "wrong NP chosen",
                                 "omissions","omission_percentage" ,"accuracy_percentage", "windIndex", "accuracy_average",
                                 "omission_average",  "Trial_duration","total_trial"]
            ["Trial","ITI","SD", "NP", "premature_timer", "correct_time", "Mouse_food_latency", "task_duration", "wrong NP chosen",
                                 "omissions", "Trial_duration","total_trial"]
            ["Trial","ITI","SD", "NP", "premature_timer", "correct_time", "Mouse_food_latency", "task_duration", "wrong NP chosen",
                                 "omissions", "Trial_duration","total_trial"]
            ["Trial","ITI","SD", "NP", "premature_timer", "correct_time", "Mouse_food_latency", "task_duration", "wrong NP chosen",
                                 "omissions", "Trial_duration","total_trial"]
            ["Trial","ITI","SD", "NP", "premature_timer", "correct_time", "Mouse_food_latency", "task_duration", "wrong NP chosen",
                                 "omissions", "Trial_duration","total_trial"]                 
]

functions = [bh.phase1(), 
             bh.phase2(),
             bh.phase3(),
             bh.stage_5csrtt_task(),
             bh.stage9_task(),
             bh.stage10_task(),
             bh.stage11_task(),
             bh.stage12_task()]
animal="mouse1" # animal name 
dt_string = now.strftime("%d_%m_%Y-%H_%M_%S") #date and time
date = dt_string 


#Explanations on food_training are the same with all the other tasks:
#In teh case you only want one phase to run you can easily comment out the phases you don't want by selecting the code and pressing ctrl + 3, same thing to uncomment it. 

#Food training

#bh.food_training() # call the function food training in bh

#data1 = [] #data1 is a list where all the data can be extracted to

phase = "Food_magazine_training"  #phase name
                   
for index,phase in enumerate(phases):
    fileName = animal+"_"+phase+"_"+ date+".csv"  #name of the file
    tempData = []
    with open(fileName,'w+') as csvfile: #within a new excel file
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(headers[index])
        if phase=="food_training":
            
            for i in functions[index]:
                datum = i
                tempData.append(i)  #append the data that was yielded
                print(i)    
                csvwriter.writerows(data1) #the rows are data1
#add phase 3, chnange yielded variables, 
        
