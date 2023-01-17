import serial
# Import serial library
ser = serial.Serial('COM4', 9600, timeout=1, stopbits=1) 
# serial.Serial('Serial Device Name', bandrate on Arduino, timeout timer in seconds)
def sensoring():
    ser.reset_input_buffer()
    # It flushes any byte that could already be in the input buffer at that point, 
    # so it will avoid receiving weird data at the beginning of the communication.
    arduinoDict = {}
    #initialise Dictionary to store string data by serial
    line = 0
    #initialise line count for dictionary
    checkStop=0
    while line < 3:
        string = ser.readline().decode( 'utf-8' ).rstrip()
        stringList = string.split(',')

        # Skips Empty readlines
        if len(stringList) <= 1:
            continue

        id = int(stringList[0])
        dist = int(stringList[1])
        stop = int(stringList[2])
        arduinoDict.update({f'carltrasonic-sensor{id}': [dist, stop]})
        
        if stop == 1:
            checkStop = 1
        line += 1

    return checkStop, arduinoDict
