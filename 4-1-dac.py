import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
GPIO.setup(dac,GPIO.OUT)
def binarr(a):
    x=[0]*8
    res=[]
    i=0
    for i in range (8):
        x[i]=a%2
        a=a//2
    for i in range (len(x)):
        res.append(x[len(x)-1-i])
    return res

try:
    while(True):
        a=input('Введите число от 0 до 255:')
        if a=='q':
            sys.exit()
        elif not a.isdigit():
            print('Введите, пожалуйста число')
        elif (int(a)>255 or int(a)<0):
            print('Сказано же, от 0 до 255')
            GPIO.output(dac,0)
        else:
            mas=binarr(int(a))
            print('u=',(3.235/(2**8)*int(a)))
            for i in range(8):
                GPIO.output(dac[i],mas[i])

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()  