import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
def poweroff():
    GPIO.setup(3, GPIO.IN)
    while True:
        if GPIO.input(3) != True:
            print("input is Ture")
            channel = GPIO.wait_for_edge(3, GPIO.RISING, timeout=5000)
            if channel is None:
                print('Poweroff...')
                os.system('poweroff')
            else:
                print("cancel")
        time.sleep(0.1)
