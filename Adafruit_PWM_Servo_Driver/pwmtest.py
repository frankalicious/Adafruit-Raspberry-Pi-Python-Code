#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import random
# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(1600)                        # Set frequency to 1600 Hz

pwm.setPWM(0, 0, 0)#red
pwm.setPWM(1, 0, 0)#green
pwm.setPWM(2, 0, 0)#blue

while (True):
    for pwmnum in range(3):
        pwm.setPWM(pwmnum, 0, random.randint(0,4095))
    time.sleep(0.1)
    # time.sleep(0.1)
    # pwm.setPWM(0, 0, 0)#red
    # pwm.setPWM(1, 0, 0)#green
    # pwm.setPWM(2, 0, 0)#blue
    # for blinkcount in range(2):
    #     pwm.setPWM(0, 0, 0)
    #     time.sleep(0.1)
    #     pwm.setPWM(0, 0, 4095)
    #     time.sleep(0.1)
