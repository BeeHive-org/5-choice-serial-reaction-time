import csv #CSV imports to excel
import belay #belay library is used as a library that communicates the data from the ESP32 to excel on teh coomputer
#from belay import Device 
#import time
from serial_beehive import SerialBeeHive #import serial_beehive the file and then the class SerialBeeHive where all the funnctions are

from datetime import datetime #used to implement dates
now = datetime.now()

print("setting up...")
print(belay.list_devices())
"""
COM3 in the line below refers to which COM port Windows is using to comunicate with the ESP32.
this can change depending on the machine, so if a error similar to this appears:
`  File "/home/andre/repositories/5-choice-serial-reaction-time/software/5-csrtt/outside2.py", line 12, in <module>
    bh = SerialBeeHive('COM3') #SerialBeeHive is now bh`

Users will need to find which COM port their device is connected to.
Here is how to find it on Windows machines:
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/establish-serial-connection.html#check-port-on-windows


"""
bh = SerialBeeHive('/dev/ttyUSB0') #SerialBeeHive is now bh
bh.setup() # call the set up function
print("done setup")

#Explanations on food_training are the same with all the other tasks:
#In the case you only want one phase to run you can easily comment out the phases you don't want 
#by selecting the code and pressing ctrl + 3, same thing to uncomment it. 

#Food training
#bh.food_training() # call the function food training in bh
#data1 = [] #data1 is a list where all the data can be extracted to


animal="mouse1" # animal name                    

date = now.strftime("%d_%m_%Y-%H_%M_%S") #date and time


phase = "food_magazine_training"  #phase name
file_name = animal+"_"+phase+"_"+ date+".csv"  #name of the file

#Go through the trials appending to CSV

print("start magazine training")
session = []
fields = ["Trial","ITI","start_trial_time",
          "Mouse_food_latency","trial_duration","total_duration"]

#thonny's backend termination leads to all data from session being lost if each new
#dataline is not saved on the file right away, so the code below does that.

#write the header.
with open(file_name, 'w', newline='') as csvfile: #within a new excel file
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) #writes the headers

#the next line opens the file, writes to it and closes it every trial,
#which is a bit wasteful, but avoids loosing data in case something hapens.
index = 1
for trial in bh.food_training(num_trial=50):
    print("trial: ",index)
    index = index+1z
    #transform all elements in list to strings
    trial_s = [str(r) for r in trial]
    with open(file_name, 'a', newline='') as csvfile: #within a new excel file
        
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerows([trial_s]) #the rows are data1
        
        
        




# #Phase 1: 


# #                
# animal="mouse1" # name can be changed                    
# phase = "Phase1"
# # 
# date = now.strftime("%d_%m_%Y-%H_%M_%S")

# file_name = animal+"_"+phase+"_"+ date+".csv"


# with open(fileName,'w+') as csvfile: #fid:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(["Trial","ITI","Mouse_food_latency","total"])
#     for trial in bh.phase1():
#         csvwriter.writerow(trial)


#Phase2  
# bh.phase2() #this is for the spitting
# 
# data3 = []
#                
# animal="mouse1" # name can be changes                    
# phase = "Phase3"
# 
# date = now.strftime("%d_%m_%Y-%H_%M_%S")
# 
# fileName = animal+"_"+phase+"_"+ date+".csv"
# 
# 

# for trial in bh.phase2():
#     #data3.append(trial)
#     
#     for i in range(0,len(data3),4):
#         clean_data = []
#     try:
#         with open(fileName,'w+') as csvfile: #fid:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(["Trial","ITI","Mouse_food_latency","total"])
#             csvwriter.writerows(data3)
#             
#            
#     except PermissionError:
#         next


#phase 3
# bh.phase3() #this is for the spitting
# print("phase3")
# data4 = []
#                
# animal="mouse1" # name can be changes                    
# phase = "Phase3"
# 
# dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
# date = dt_string
# 
# fileName = animal+"_"+phase+"_"+ date+".csv"
# 
# 
# data4=[]
# for i in bh.phase3():

#     print(i)

#     
#     try:
#         with open(fileName,'w+') as csvfile: #fid:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(["Trial","ITI","NP chosen", "Mouse_food_latency", "premature responce", "wrong button", "task end","total"])
#             csvwriter.writerows(data4)
#                      
#            
#     except PermissionError:
#         next

# bh.stage_5csrtt_task() #this is for the spitting

# data4 = []
               
# animal="mouse1" # name can be changes                    
# phase = "Phase4-8"

# date = now.strftime("%d_%m_%Y-%H_%M_%S")



# fileName = animal+"_"+phase+"_"+ date+".csv"


# data4=[]
# for i in bh.stage_5csrtt_task():
#     data4.append(i)
#     print(i)
#     #data4.append(i)
    
#     for i in range(0,len(data4),17):
#         clean_data = []
#     try:
#         with open(fileName,'w+') as csvfile: #fid:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(["trial","ITI","SD", "NP","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","omission percentage", "Accuracy percentage", "Winindex", "accuracy average", "omission average", "total (ms)", "total_task"])
#             csvwriter.writerows(data4)
            
           
#     except PermissionError:
#         next
    

# # 
# bh.stage9_task() #this is for the spitting

# data5 = []
               
# animal="mouse1" # name can be changes                    
# phase = "phase9"

# date = now.strftime("%d_%m_%Y-%H_%M_%S")

# fileName = animal+"_"+phase+"_"+ date+".csv"


# data5=[]
# for i in bh.stage9_task():
#     data5.append(i)
#     print(i)
#     #data1.append(i)
    
#     for i in range(0,len(data5),11):
#         clean_data = []
#     try:
#         with open(fileName,'w+') as csvfile: #fid:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
#             csvwriter.writerows(data5)
            
           
#     except PermissionError:
#         next
# #     

# # 
# bh.stage10_task() #this is for the spitting

# data6 = []
               
# animal="mouse1" # name can be changes                    
# phase = "phase10"

# date = now.strftime("%d_%m_%Y-%H_%M_%S")

# fileName = animal+"_"+phase+"_"+ date+".csv"



# data6=[]
# for i in bh.stage10_task():
#     data6.append(i)
#     print(i)
#     #data6.append(i)
    
#     for i in range(0,len(data6),11):
#         clean_data = []
#     try:
#         with open(fileName,'w+') as csvfile: #fid:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
#             csvwriter.writerows(data6)
            
           
#     except PermissionError:
#         next
# #     
# # 
# bh.stage11_task() #this is for the spitting

# data7 = []
               
# animal="mouse1" # name can be changes                    
# phase = "phase11"

# date = now.strftime("%d_%m_%Y-%H_%M_%S")

# fileName = animal+"_"+phase+"_"+ date+".csv"



# data7=[]
# for i in bh.food_training():
#     data7.append(i)
#     print(i)
 
    
#     for i in range(0,len(data7),11):
#         clean_data = []
#     try:
#         with open(fileName,'w+') as csvfile: #fid:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
#             csvwriter.writerows(data7)
            
           
#     except PermissionError:
#         next
    
    

# bh.stage12_task() #this is for the spitting

# data8 = []
               
# animal="mouse1" # name can be changes                    
# phase = "phase12"

# date = now.strftime("%d_%m_%Y-%H_%M_%S")
# fileName = animal+"_"+phase+"_"+ date+".csv"


# for i in bh.food_training():
#     data8.append(i)
#     print(i)
    
    
#     for i in range(0,len(data8),11):
#         clean_data = []
#     try:
#         with open(fileName,'w+') as csvfile: #fid:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
#             csvwriter.writerows(data8)
            
           
#     except PermissionError:
#         next
    
    
    
# bh.stage11_task() #this is for the spitting

# data9 = []
               
# animal="mouse1" # name can be changes                    
# phase = "phase13"

# date = now.strftime("%d_%m_%Y-%H_%M_%S")

# fileName = animal+"_"+phase+"_"+ date+".csv"



# data9=[]
# for i in bh.food_training():
#     data9.append(i)
#     print(i)
#     #data7.append(i)
    
#     for i in range(0,len(data9),11):
#         clean_data = []
#     try:
#         with open(fileName,'w+') as csvfile: #fid:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
#             csvwriter.writerows(data9)
            
           
#     except PermissionError:
#         next

   
   

# bh.close()






