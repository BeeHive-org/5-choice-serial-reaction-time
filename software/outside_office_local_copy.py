import csv #CSV imports to excel
import belay #belay library is used as a library that communicates the data from the ESP32 to excel on teh coomputer
#from belay import Device 
#import time
from serial_beehive import SerialBeeHive #import serial_beehive the file and then the class SerialBeeHive where all the funnctions are

from datetime import datetime #used to implement dates




now = datetime.now()
date = now.strftime("%d_%m_%Y-%H_%M_%S") #date and time
animal="mouse1" # animal name  



print("setting up")
print(belay.list_devices()) 
bh = SerialBeeHive('COM3') #SerialBeeHive is now bh
bh.setup() # call the set up function
print("done setup")

#Explanations on food_training are the same with all the other tasks:
#In teh case you only want one phase to run you can easily comment out the phases you don't want by selecting the code and pressing ctrl + 3, same thing to uncomment it. 


#Food training


phase = "Food_magazine_training"  #phase name
                  


 
fileName = animal+"_"+phase+"_"+ date+".csv"  #name of the file

with open(fileName,'w+') as csvfile: #within a new excel file
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(["Trial","ITI","Mouse_food_latency","total_trial"]) #writes the headers
    for trial in bh.food_training():
        print(trial)    
        csvwriter.writerow(trial) #the rows are data1


animal="mouse1" # name can be changes                    
phase = "Phase1"
date = now.strftime("%d_%m_%Y-%H_%M_%S")
fileName = animal+"_"+phase+"_"+ date+".csv"

with open(fileName,'w+') as csvfile: #fid:
     csvwriter = csv.writer(csvfile)
     csvwriter.writerow(["Trial","Start_time","Mouse_food_latency","Trial_duration","total_trial"],)
     for trial in bh.phase1():
        print(trial)
        csvwriter.writerow(trial)


##PHASE2

                 
phase = "Phase2"
# 

# 
fileName = animal+"_"+phase+"_"+ date+".csv"
# 
# 
with open(fileName,'w+') as csvfile: #fid:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Trial","ITI","Mouse_food_latency","total"])
    for trial in bh.phase2():
        print(trial)
        csv.writerow(trial)

##PHASE3
             
phase = "Phase3"


# 
fileName = animal+"_"+phase+"_"+ date+".csv"
with open(fileName,'w+') as csvfile: #fid:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Trial","ITI","NP chosen", "Mouse_food_latency", "premature responce", "wrong button", "task end","total"])
    for trial in bh.phase3():
        print(trial)
        csvwriter.writerow(trial)     

##PHASES 4-8
               

phase = "Phase4-8"




fileName = animal+"_"+phase+"_"+ date+".csv"

with open(fileName,'w+') as csvfile: #fid:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["trial","ITI","SD", "NP","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","omission percentage", "Accuracy percentage", "Winindex", "accuracy average", "omission average", "total (ms)", "total_task"])
    for trial in bh.stage_5csrtt_task():
        print(trial)
        csvwriter.writerow(trial)
    
##PHASE 9 
           
                    
phase = "phase9"


fileName = animal+"_"+phase+"_"+ date+".csv"

with open(fileName,'w+') as csvfile: #fid:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
    for trial in bh.stage9_task():
        print(trial)
        csvwriter.writerow(trial)
    
    
##PHASE 10
               
                  
phase = "phase10"


fileName = animal+"_"+phase+"_"+ date+".csv"

with open(fileName,'w+') as csvfile: #fid:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
    for trial in bh.stage10_task():
        print(trial)
        csvwriter.writerows(trial)
    
##PHASE 11

                  
phase = "phase11"


fileName = animal+"_"+phase+"_"+ date+".csv"

with open(fileName,'w+') as csvfile: #fid:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
    for trial in bh.stage11_task():
        print(trial)
        csvwriter.writerow(trial)
    
  
##PHASE 12
               
                   
phase = "phase12"
fileName = animal+"_"+phase+"_"+ date+".csv"

with open(fileName,'w+') as csvfile: #fid:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])

    for trial in bh.stage12_task():
        print(trial)
        csvwriter.writerow(trial)
   
           
    

bh.close()