#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins for sonic
GPIO_TRIGGER_FRONT = 18
GPIO_ECHO_FRONT = 24

#Pins for movement
GPIO_FORWARD = 5
GPIO_RIGHT = 4
GPIO_LEFT = 6
GPIO_STOP = 26

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER_FRONT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_FRONT, GPIO.IN)

#Movement stups
GPIO.setup(GPIO_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_RIGHT, GPIO.OUT)
GPIO.setup(GPIO_LEFT, GPIO.OUT)
GPIO.setup(GPIO_STOP, GPIO.OUT)

#Some constants 
#Goal height and width are variables required for the program to stop
#Also they stop the loop for going up and going left
goal_height = 182.88
goal_width = 213.36

#Max width and height are variables outside the wall
#Basically the binding space of the whole arena 
max_height = 213.36
max_width = 213.36

#Value to track approximate robot position
current_height = 0
current_width = 0

#Cspace = space IR sensor will scream
cspace_front = 20.0

#distance vars
distance_front = 0
distance_left = 20
distance_right = 0

#Get distance of an Ultrasonic sensor
#Use case 
# getDistance(GPIO_TRIGGER, GPIO_ECHO)
def getDistance(trigger, echo):
    # set Trigger to HIGH
    GPIO.output(trigger, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

#Performs a right turn for 0.2s
def turnRight():
    print('turning right')
    GPIO.output(GPIO_RIGHT, True)
    time.sleep(0.2)
    GPIO.output(GPIO_RIGHT, False)
    
#Performs a left turn for 0.2s
def turnLeft():
    print('turning left')
    GPIO.output(GPIO_LEFT, True)
    time.sleep(0.2)
    GPIO.output(GPIO_LEFT, False)
    
#moves forward for 0.5s
def moveForward():
    GPIO.output(GPIO_FORWARD, True)
    time.sleep(0.5)
    GPIO.output(GPIO_FORWARD, False)

#checks to see if moving right reveals an open path ahead
def checkRight():
    GPIO.output(GPIO_RIGHT, True)
    time.sleep(0.1)
    GPIO.output(GPIO_RIGHT, False)
    if getDistance(GPIO_TRIGGER_FRONT, GPIO_ECHO_FRONT) > 20:
        return True
    else:
        GPIO.output(GPIO_LEFT, True)
        time.sleep(0.1)
        GPIO.output(GPIO_LEFT, False)
        return False
    
#checks to see if moving left reveals an open path ahead
def checkLeft():
    GPIO.output(GPIO_LEFT, True)
    time.sleep(1)
    GPIO.output(GPIO_LEFT, False)
    if getDistance(GPIO_TRIGGER_FRONT, GPIO_ECHO_FRONT) > 20:
        return True
    else:
        GPIO.output(GPIO_RIGHT, True)
        time.sleep(1)
        GPIO.output(GPIO_RIGHT, False)
        return False    

#move up
while distance_front != -1 and current_height < goal_height:
    distance_front = getDistance(GPIO_TRIGGER_FRONT, GPIO_ECHO_FRONT)
    ##TODO: Add ultrasonic sensor left and right
    #distance_right = getDistance(GPIO_TRIGGER_RIGHT, GPIO_ECHO_RIGHT)
    #distance_right = getDistance(GPIO_TRIGGER_LEFT, GPIO_ECHO_LEFT)
    #distance
    time.sleep(1)
    distance_front = float(distance_front)
    print(distance_front)
    #If obstacle is detected in front
    if(distance_front < 10):
        if (checkRight()):
            print('checking right')
            break
        elif (checkLeft()):
            print('checking left')
            break
    #this covers a specific scenario on the path
    if distance_right < 10 and distance_left < 10:
        moveForward() 
        current_height = current_height + 7.62
    ###############################################
    #
    # NOTE: Timing for turnLeft() and turnRight() may need to be adjusted for more precise turns
    #
    ###############################################
    #if too close to right side
    if distance_right < 10:
        turnLeft()
    #if too close to left side
    if distance_left < 10:
        turnRight()        
    #Normal case move forward
    else:
        print('Current height is ' + str(current_height))
        moveForward()
        current_height = current_height + 7.62

    print(current_height)
print('Goal height reached')

#Move left ~90 degrees
#TODO: Test how long it takes for a sharp right turn here
GPIO.output(GPIO_LEFT, True)
time.sleep(0.2)
GPIO.output(GPIO_LEFT, False)

#move left
while distance_front != -1 and current_width < goal_width:
    distance_front = getDistance(GPIO_TRIGGER_FRONT, GPIO_ECHO_FRONT)
    ##TODO: Add ultrasonic sensor left and right
    #distance_right = getDistance(GPIO_TRIGGER_RIGHT, GPIO_ECHO_RIGHT)
    #distance_right = getDistance(GPIO_TRIGGER_LEFT, GPIO_ECHO_LEFT)
    #distance
    time.sleep(1)
    distance_front = float(distance_front)
    print(distance_front)
    #If obstacle is detected in front
    if(distance_front < 10):
        if (checkRight()):
            print('checking right')
            break
        elif (checkLeft()):
            print('checking left')
            break
    #this covers a specific scenario on the path
    if distance_right < 10 and distance_left < 10:
        moveForward() 
        current_width = current_width + 7.62
    ###############################################
    #
    # NOTE: Timing for turnLeft() and turnRight() may need to be adjusted for more precise turns
    #
    ###############################################
    #if too close to right side
    if distance_right < 10:
        turnLeft()
    #if too close to left side
    if distance_left < 10:
        turnRight()        
    #Normal case move forward
    else:
        print('Current height is ' + str(current_width))
        moveForward()
        current_width = current_width + 7.62
GPIO.cleanup()
print('goal reached')
exit()