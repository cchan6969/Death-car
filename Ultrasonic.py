import serial 

# serial.Serial('Serial Device Name', bandrate on Arduino, timeout timer in seconds)
ser = serial.Serial('COM4', 9600, timeout=1, stopbits=1) 

# It allows you to execute code when the file runs as a script, but not when it is imported as a module
def sensoring():
    # It flushes any byte that could already be in the input buffer at that point, 
    # so it will avoid receiving weird data at the beginning of the communication.
    ser.reset_input_buffer()

    arduinoDict = {}
    line = 0

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

        line += 1

    return arduinoDict
