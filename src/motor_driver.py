import RPi.GPIO as gpio
import time
import pygame
from pygame.locals import *

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 

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


pwm_mr.ChangeDutyCycle(50)
pwm_ml.ChangeDutyCycle(50)

pygame.init()
screen = pygame.display.set_mode((240, 240))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(1)



def key_listener():
    global message
    pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)
    rospy.init_node("key_listenser_node")

    while not rospy.is_shutdown():
        events = pygame.event.get()
        twist=Twist()
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key ==  pygame.K_LEFT:
                    twist.angular.z=z
                    message='left'
                    print(message)
                    pub.publish(twist)
                    gpio.output(mr[0],1)
                    gpio.output(ml[1],1)                  
                if event.key == pygame.K_RIGHT:
                    twist.angular.z=-z
                    message='right'
                    print(message)
                    pub.publish(twist)
                    gpio.output(mr[1],1)
                    gpio.output(ml[0],1)      
                if event.key == pygame.K_UP:
                    twist.linear.x=v
                    message='up'
                    print(message)
                    pub.publish(twist)
                    gpio.output(ml[0],1)
                    gpio.output(mr[0],1)

                                        
                if event.key == pygame.K_DOWN:
                    twist.linear.x=-v
                    message='DOWN'
                    print(message)
                    pub.publish(twist)
                    gpio.output(ml[1],1)
                    gpio.output(mr[1],1)
            if event.type == pygame.KEYUP:
                twist.angular.z=0.0
                twist.linear.x=0.0
                message='key-up'
                print(message)
                pub.publish(twist)
                pio.output(ml[0],0)
                gpio.output(mr[0],0)
                gpio.output(ml[1],0)
                gpio.output(mr[1],0)
if __name__=="__main__":
    key_listener()
"""
for i in range(4):
    gpio.output(ml[0],1)
    pwm_mr.ChangeDutyCycle(25*i)
    pwm_ml.ChangeDutyCycle(25*i)
    time.sleep(3)

gpio.output(ml[0],0)
pwm_mr.ChangeDutyCycle(0)
pwm_ml.ChangeDutyCycle(0)

    
 """   
