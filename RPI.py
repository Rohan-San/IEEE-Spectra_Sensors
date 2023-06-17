import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
IR_PIN = 18
LIGHT_PIN = 25
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, False)

def readIR(pin):
    GPIO.SETUP(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(0.1)

    GPIO.setup(pin, GPIO.IN)
    i = GPIO.input(pin)
    if i == False:
        print("No Inturuders !", i)
        GPIO.output(LIGHT_PIN, False)
    elif (i == True):
        print("intruder alert !", i)
        GPIO.OUTPUT(LIGHT_PIN, True)
try:
    while True:
        readIR(IR_PIN)
        time.sleep(0.5)
except(KeyboardInterrupt):
    GPIO.cleanup()
    exit()
    
