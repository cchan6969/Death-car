#!/usr/bin/env python3
import serial 
import json

arduinoDict = {}
arduinoList = []
count=0

# Import Serial Library
if __name__ == '__main__':
# It allows you to execute code when the file runs as a script, but not when it is imported as a module
    ser = serial.Serial('COM4', 9600, timeout=1) 
    # .Serial('Serial Device Name', bandrate on Arduino, timeout timer in seconds)
    ser.reset_input_buffer()
    # It flushes any byte that could already be in the input buffer at that point, 
    # so it will avoid receiving weird data at the beginning of the communication.
    while True:
    # Infinite loop
        while count < 3:
            #line = ser.readline().decode("utf_8").rstrip()
            line = ser.readline().decode( 'ascii' ).rstrip()
            # line = int(line)
            # readline() function will read all bytes until a newline character is detected
            # decode() decodes the incoming byte message from serial
            # utf-8 converts byte to string
            # rstrip() function is specific to strings, it allows you to remove any trailing characters (newline, carriage return)
            #print(line)
            #print(int(line))
            arduinoList.append(line)
            count+=1
        print(arduinoList)
        #arduinoDict['Stop'] = arduinoList[0]
        #arduinoDict['Sensor'] = arduinoList[1]
        #arduinoDict['Dist'] = arduinoList[2]
        
        #print(arduinoDict)
        # Send data to Pi
        sensor1 = arduinoDict.get("Sensor")
        sensor2 = arduinoDict.get("Dist")
        sensor3 = arduinoDict.get("Stop")

        

        # Reset
        arduinoList = []
        count = 0
            #data = json.loads(line)
            #print(data)
            #print(type(data))