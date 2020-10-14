#!/usr/bin/env python3
import time 
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(29,gpio.IN,pull_up_down=gpio.PUD_DOWN)
ti=0
intial=True
T=0
def frequency_meter(channel):
    global ti , intial , T
    if intial:
        ti=time.time()
        intial =False
        print("rising1 at")
        print(ti)
        
    if not intial :
        tf=time.time()
        T=tf-ti
        intial =True
        print("rising2 at")
        print(tf)
        print("T={} , F={}".format(T,(1/T)))
        
gpio.add_event_detect(29, gpio.RISING)
gpio.add_event_callback(29, callback=frequency_meter)  
prevT=0
while True:
    if False:
        print("T={} , F={}".format(T,(1/T)))
    prevT=T
    


    
