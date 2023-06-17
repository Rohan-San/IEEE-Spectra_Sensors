import RPi.GPIO as GPIO
import time
pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
while True:
    try:
        GPIO.output(pin, True)
        time.sleep(0.5)
        GPIO.output(pin, False)
        time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
