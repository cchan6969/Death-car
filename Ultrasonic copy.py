#!/usr/bin/env python3
import serial 
# Import Serial Library
import json
# Import Python JSON library
count = 0
#inistialising a count
arduinoDict = {}
# initialising a Python Dictionary
arduinoList = []
#Initialising a Python List

def import_dict(count,arduinoDict,arduinoList):
    while count < 3:
        line = ser.readline().decode( 'ascii' ).rstrip()
        # line = int(line)
        # readline() function will read all bytes until a newline character is detected
        # decode() decodes the incoming byte message from serial
        # utf-8/ascii  converts byte to string
        # rstrip() function is specific to strings, it allows you to remove any trailing characters (newline, carriage return)
        arduinoList.append(line)
        count+=1
    arduinoDict['Dist'] = arduinoList[0]
    arduinoDict['Stop'] = arduinoList[1]
    arduinoDict['Sensor'] = arduinoList[2]
    #print(arduinoDict)
    #print(arduinoList)
    # Reset
    arduinoList = []
    count = 0
    return(arduinoDict)
    

if __name__ == '__main__':
    ser = serial.Serial('COM4', 9600, timeout=1) 
    # .Serial('Serial Device Name', bandrate on Arduino, timeout timer in seconds)
    ser.reset_input_buffer()
    # It flushes any byte that could already be in the input buffer at that point, 
    # so it will avoid receiving weird data at the beginning of the communication.
    while 1:
        import_dict(count,arduinoDict,arduinoList)
        print(arduinoDict)
    
    # Send data to Pi
    #sensor = arduinoDict.get("Sensor")
    #dist = arduinoDict.get("Dist")
    #stop = arduinoDict.get("Stop")
# It allows you to execute code when the file runs as a script, but not when it is imported as a module
