import Ultrasonic
# import module
while True:
    #Infinite loop
    a=Ultrasonic.sensoring()
    # .sensoring() is function inside the Python Module
    sensorStop=a[0]
    #stop value for zero forward velocity
    #does not stop steering or backwards 
    sensorDict=a[1]
    #data dictionary for GUI on Pi
    if sensorStop == 1:
        print('stop')
    