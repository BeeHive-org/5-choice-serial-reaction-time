import csv #CSV imports to excel
import belay #belay library is used as a library that communicates the data from the ESP32 to excel on teh coomputer
#from belay import Device 
#import time
from serial_beehive import SerialBeeHive #import serial_beehive the file and then the class SerialBeeHive where all the funnctions are

from datetime import datetime #used to implement dates
now = datetime.now()

print("mmmdm")
print(belay.list_devices()) 
bh = SerialBeeHive('COM3') #SerialBeeHive is now bh
bh.setup() # call the set up function
print("done setup")

#Explanations on food_training are the same with all the other tasks:
#In teh case you only want one phase to run you can easily comment out the phases you don't want by selecting the code and pressing ctrl + 3, same thing to uncomment it. 

#Food training
bh.food_training() # call the function food training in bh
data1 = [] #data1 is a list where all the data can be extracted to

phase = "Food_magazine_training"  #phase name
animal="mouse1" # animal name                    
# 
# 
dt_string = now.strftime("%d_%m_%Y-%H_%M_%S") #date and time
date = dt_string 
# 
fileName = animal+"_"+phase+"_"+ date+".csv"  #name of the file

#Go through the trials appending to CSV
data1=[]
with open(fileName,'w+') as csvfile: #within a new excel file
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(["Trial","ITI","Mouse_food_latency","total_trial"]) #writes the headers
    for i in bh.food_training():
        data1.append(i)  #append the data that was yielded
        print(i)    
        csvwriter.writerows(data1) #the rows are data1




# #Phase 1: 
# bh.phase1() #this is for the spitting
# # 
# data2 = []
# #                
# animal="mouse1" # name can be changes                    
# phase = "Phase2"
# # 
# dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
# date = dt_string
# # 
# # 
# fileName = animal+"_"+phase+"_"+ date+".csv"
# # 
# data2=[]
# with open(fileName,'w+') as csvfile: #fid:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(["Trial","ITI","Mouse_food_latency","total"])
#     for i in bh.phase1():
#         data2.append(i)
#         print(i)
#         csvwriter.writerows(data2)


#Phase2  
# bh.phase2() #this is for the spitting
# 
# data3 = []
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
# data3=[]
# for i in bh.phase2():
#     data3.append(i)
#     print(i)
#     #data3.append(i)
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
#     data4.append(i)
#     print(i)
#     #data3.append(i)
#     
#     for i in range(0,len(data4),7):
#         clean_data = []
#     try:
#         with open(fileName,'w+') as csvfile: #fid:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(["Trial","ITI","NP chosen", "Mouse_food_latency", "premature responce", "wrong button", "task end","total"])
#             csvwriter.writerows(data4)
#                      
#            
#     except PermissionError:
#         next

bh.stage_5csrtt_task() #this is for the spitting

data4 = []
               
animal="mouse1" # name can be changes                    
phase = "Phase4-8"

dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
date = dt_string


fileName = animal+"_"+phase+"_"+ date+".csv"


data4=[]
for i in bh.stage_5csrtt_task():
    data4.append(i)
    print(i)
    #data4.append(i)
    
    for i in range(0,len(data4),17):
        clean_data = []
    try:
        with open(fileName,'w+') as csvfile: #fid:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["trial","ITI","SD", "NP","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","omission percentage", "Accuracy percentage", "Winindex", "accuracy average", "omission average", "total (ms)", "total_task"])
            csvwriter.writerows(data4)
            
           
    except PermissionError:
        next
    
   
    
    
    

# 
bh.stage9_task() #this is for the spitting

data5 = []
               
animal="mouse1" # name can be changes                    
phase = "phase9"

dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
date = dt_string


fileName = animal+"_"+phase+"_"+ date+".csv"


data5=[]
for i in bh.stage9_task():
    data5.append(i)
    print(i)
    #data1.append(i)
    
    for i in range(0,len(data5),11):
        clean_data = []
    try:
        with open(fileName,'w+') as csvfile: #fid:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
            csvwriter.writerows(data5)
            
           
    except PermissionError:
        next
#     
#     
# 
# 
# 
bh.stage10_task() #this is for the spitting

data6 = []
               
animal="mouse1" # name can be changes                    
phase = "phase10"

dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
date = dt_string
fileName = animal+"_"+phase+"_"+ date+".csv"



data6=[]
for i in bh.stage10_task():
    data6.append(i)
    print(i)
    #data6.append(i)
    
    for i in range(0,len(data6),11):
        clean_data = []
    try:
        with open(fileName,'w+') as csvfile: #fid:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
            csvwriter.writerows(data6)
            
           
    except PermissionError:
        next
#     
    


# 
bh.stage11_task() #this is for the spitting

data7 = []
               
animal="mouse1" # name can be changes                    
phase = "phase11"

dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
date = dt_string
fileName = animal+"_"+phase+"_"+ date+".csv"



data7=[]
for i in bh.food_training():
    data7.append(i)
    print(i)
 
    
    for i in range(0,len(data7),11):
        clean_data = []
    try:
        with open(fileName,'w+') as csvfile: #fid:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
            csvwriter.writerows(data7)
            
           
    except PermissionError:
        next
    
    

bh.stage12_task() #this is for the spitting

data8 = []
               
animal="mouse1" # name can be changes                    
phase = "phase12"

dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
date = dt_string
fileName = animal+"_"+phase+"_"+ date+".csv"


for i in bh.food_training():
    data8.append(i)
    print(i)
    
    
    for i in range(0,len(data8),11):
        clean_data = []
    try:
        with open(fileName,'w+') as csvfile: #fid:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
            csvwriter.writerows(data8)
            
           
    except PermissionError:
        next
    
    
    
bh.stage11_task() #this is for the spitting

data9 = []
               
animal="mouse1" # name can be changes                    
phase = "phase13"

dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
date = dt_string
fileName = animal+"_"+phase+"_"+ date+".csv"



data9=[]
for i in bh.food_training():
    data9.append(i)
    print(i)
    #data7.append(i)
    
    for i in range(0,len(data9),11):
        clean_data = []
    try:
        with open(fileName,'w+') as csvfile: #fid:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["trial","ITI","SD", "Light","premature_responses (ms)",  "correct_responses(ms)","Mouse_food_latency (ms)" , "incorrect responses (ms)", "wrong NP chosen",  "omissions","total (ms)"])
            csvwriter.writerows(data9)
            
           
    except PermissionError:
        next

   
   

bh.close()






