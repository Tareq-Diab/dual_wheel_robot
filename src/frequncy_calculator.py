#!/usr/bin/env python
import time 
import RPi.GPIO as GPIO
from read_PWM import reader
import pigpio


GPIO.setmode(GPIO.BOARD)
pi = pigpio.pi()
ml=reader(pi,5)
while 1 :
    print(ml.frequency(),ml.duty_cycle())



