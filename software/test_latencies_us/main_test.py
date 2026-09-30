import csv #CSV imports to excel
import belay #belay library is used as a library that communicates the data from the ESP32 to excel on teh coomputer
#from belay import Device 
#import time
from serial_beehive import SerialBeeHive #import serial_beehive the file and then the class SerialBeeHive where all the funnctions are
import pandas as pd

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
bh = SerialBeeHive('/dev/ttyUSB1') #SerialBeeHive is now bh
bh.setup() # call the set up function
print("done setup")

#test for toggling an digital port on/off and reading from another digital port
data = bh.delays_benchmarking()
data.to_json("benchmark.json")

# #write the header.
# with open('data_in.csv', 'w', newline='') as csvfile: #within a new excel file
#     csvwriter = csv.writer(csvfile) 
#     csvwriter.writerow(fields) #writes the headers
# 
# trial_s = [str(r) for r in trial]
#     with open(file_name_training, 'a', newline='') as csvfile: #within a new excel file
#         #open the file in append mode
#         csvwriter = csv.writer(csvfile)
#         #write the trial data
#         csvwriter.writerows([trial_s]) #the rows are data1