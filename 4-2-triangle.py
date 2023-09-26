import RPi.GPIO as GPIO
import sys
import time
dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def binarrr(a,n):
    return[int (elem) for elem in bin(a)[2:].zfill(n)]
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
    while (True):
        T=input('Give me youe numbeeeer:')
        if (T=='q'):
            sys.exit()
        elif not T.isdigit():
            print('Введите пожалуйста ЧИСЛО!')
        else:
            while(True):
                for i in range(255):
                    a=i
                    mas=binarr(int(a))
                    for i in range (8):
                        GPIO.output(dac[i],mas[i])
                    time.sleep(int(T)/512)
                for i in range(255):
                    a=255-i
                    mas=binarr(int(a))
                    for i in range (8):
                        GPIO.output(dac[i],mas[i])
                    time.sleep(int(T)/512)
            
finally:
    GPIO.output(dac,1)
    GPIO.cleanup()