import Ultrasonic
while True:
    #Infinite loop
    a=Ultrasonic.sensoring()
    sensorStop=a[0]
    #stop value for zero forward velocity
    #does not stop steering or backwards 
    sensorDict=a[1]
    #data dictionary for GUI on Pi
    if b == 1:
        print('stop')
    