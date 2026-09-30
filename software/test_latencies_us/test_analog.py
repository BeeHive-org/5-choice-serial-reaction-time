import time
import belay

device = belay.Device("/dev/ttyUSB0")



@device.setup
def setup(pin_numbers=[33,36]):
    from machine import Pin
    from machine import ADC
    
    all_sensors = dict()
    for port in pin_numbers:
        all_sensors[str(port)] = ADC(port)
        all_sensors[str(port)].atten(ADC.ATTN_11DB)#full 3.3v range
    print(all_sensors)


setup(pin_numbers=[33,36])

@device.task
def read_sensor():
    for key in all_sensors.keys():
        sensor = all_sensors[key]
        print("reading port: "+ key)
        for i in range(10):
            print(sensor.read())
        
            time.sleep(0.2)
    #return read_value
    
read_sensor()