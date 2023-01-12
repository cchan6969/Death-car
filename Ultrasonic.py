#!/usr/bin/env python3
import serial 
# Import Serial Library
if __name__ == '__main__':
# It allows you to execute code when the file runs as a script, but not when it is imported as a module
    ser = serial.Serial('COM3', 9600, timeout=1) 
    # .Serial('Serial Device Name', bandrate on Arduino, timeout timer in seconds)
    ser.reset_input_buffer()
    # It flushes any byte that could already be in the input buffer at that point, 
    # so it will avoid receiving weird data at the beginning of the communication.
    while True:
    # Infinite loop
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            # readline() function will read all bytes until a newline character is detected
            # decode() decodes the incoming byte message from serial
            # utf-8 converts byte to string
            # rstrip() function is specific to strings, it allows you to remove any trailing characters (newline, carriage return)
            print(line)