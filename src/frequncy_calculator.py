#!/usr/bin/env python
import time 
import RPi.GPIO as GPIO
from read_PWM import reader
import pigpio


GPIO.setmode(GPIO.BOARD)
pi = pigpio.pi()
ml=reader(pi,5)
while 1 :
    try:
        time.sleep(0.1)
        print(ml.frequency(),ml.duty_cycle())
        ml._high=None
        ml._high_tick=None
        ml._period=None
    except:
        print("error occured")
        pass



