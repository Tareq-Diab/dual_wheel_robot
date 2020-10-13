import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
mr=[37,35,40]
ml=[33,31,38]
for pin in mr:
    gpio.setup(pin,gpio.OUT)
for pin in ml:
    gpio.setup(pin,gpio.OUT)
pwm_mr=gpio.PWM(40,50)
pwm_ml=gpio.PWM(38,50)
pwm_mr.start(0)
pwm_ml.start(0)
for i in range(4):
    gpio.output(ml[0],1)
    pwm_mr.ChangeDutyCycle(25*i)
    pwm_ml.ChangeDutyCycle(25*i)
    time.sleep(3)

gpio.output(ml[0],0)
pwm_mr.ChangeDutyCycle(0)
pwm_ml.ChangeDutyCycle(0)

    
    
