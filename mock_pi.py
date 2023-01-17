import Ultrasonic
while True:
    #Infinite loop
    a=Ultrasonic.sensoring()
    b=a[0]
    c=a[1]
    print(c)
    print(type(c))