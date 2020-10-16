#!/usr/bin/env python
import time 
import RPi.GPIO as GPIO
from read_PWM import reader
import pigpio


class motorspeed(self,pin,resolution):
    def __init__(self,l,r):
        self.pi=pigpio.pi()
        self.motor=reader(pi,pin)
    def RPS(self):
        self.F=self.motor.frequency()
        self.motor._high=None
        self.motor._high_tick=None
        self.motor._period=None

        self.rps=self.F/resolution
        return self.rps
    def RPM(self):
        self.rpm=self.RPS()*60
        return self.rpm
right_motor=motorspeed(5,20)
while 1:
    time.sleep(0.1)
    print(right_motor.RPS())
"""
GPIO.setmode(GPIO.BOARD)
pi = pigpio.pi()
ml=reader(pi,5)

while 1 :
    try:
        time.sleep(0.1)
        print(ml.frequency())
        ml._high=None
        ml._high_tick=None
        ml._period=None
    except:
        print("error occured")
        pass
"""
