import RPi.GPIO as GPIO
import time 
leds=[2,3,4,17,27,22,10,9]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds,GPIO.OUT)
for k in range (3):
    for i in range (0,8,1):
        GPIO.output(leds[i],GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(leds[i],GPIO.LOW)
