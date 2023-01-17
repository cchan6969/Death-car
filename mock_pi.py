import Ultrasonic
while True:
    #Infinite loop
    a=Ultrasonic.sensoring()
    b=a[0]
    #stop value
    c=a[1]
    #data dictionary
    if b == 1:
        print('stop')
    