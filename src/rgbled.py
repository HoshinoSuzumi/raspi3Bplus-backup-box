import RPi.GPIO as GPIO
import time
import os
class RGBLED():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
        self.redgpio = GPIO.PWM(32,300)
        self.greengpio = GPIO.PWM(33,300)
        self.bluegpio = GPIO.PWM(35,300)
        self.redgpio.start(0)
        self.greengpio.start(0)
        self.bluegpio.start(0)
    def LED(self,red,green,blue):
        self.redgpio.ChangeDutyCycle(int((red*20)/51))
        self.greengpio.ChangeDutyCycle(int((green*20)/51))
        self.bluegpio.ChangeDutyCycle(int((blue*20)/51))
