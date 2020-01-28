import serial 
import struct
arduinoSerialData = serial.Serial('/dev/ttyACM1',9600)
while True:
    print(int(float(arduinoSerialData.readline().decode('utf-8'))))
    #print(struct.unpack('f',arduinoSerialData.readline() ))