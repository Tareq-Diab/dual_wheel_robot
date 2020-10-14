#!/usr/bin/env python
import time 
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)

ti=0
intial=True
T=0
def frequency_meter(channel):
    global ti , intial , T
    if intial:
        ti=time.time()
        initial =False
    else :
        T=ti-time.time()
        intial =True
        print("the periodic timeis {}".format(T))
gpio.add_event_detect(29, GPIO.RISING, callback=frequency_meter)  

    