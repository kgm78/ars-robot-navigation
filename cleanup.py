import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#set GPIO Pins for sonic
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#Pins for movement
GPIO_FORWARD = 5
GPIO_RIGHT = 4
GPIO_LEFT = 6
GPIO_STOP = 26

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#Movement stups
GPIO.setup(GPIO_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_RIGHT, GPIO.OUT)
GPIO.setup(GPIO_LEFT, GPIO.OUT)
GPIO.setup(GPIO_STOP, GPIO.OUT)
GPIO.cleanup()