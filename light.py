import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
while True:
        GPIO.output(27,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(27,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.05)
 
