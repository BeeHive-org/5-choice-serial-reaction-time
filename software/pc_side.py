import Serial_communication as SB


b=SB.Board()
print(b.serial_ports())

b.connect('/dev/ttyUSB0')
b.runFile("food_magazine.py")
b.record(till=True,gather=10)
data,speed = b.readData(channels=[])

print(data)
#print(data1)