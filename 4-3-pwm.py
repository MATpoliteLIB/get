import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
GPIO.setup(24,GPIO.OUT)
GPIO.setup(dac,GPIO.OUT)

pwm=GPIO.PWM(24,1000)
pwm.start(0)
try:
    while True:
        DutyCicle=int(input())
        pwm.ChangeDutyCycle(DutyCicle)
        print("{:.2f}".format(DutyCicle*3.3/100))
finally:
    GPIO.output(24,0)
    GPIO.output(dac,0)
    GPIO.cleanup()