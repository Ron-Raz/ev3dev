#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

import time
# TODO: Add code here
leds = Leds()

time.sleep(1)
leds.set_color("LEFT", "GREEN")
leds.set_color("RIGHT", "GREEN")
time.sleep(1)
leds.set_color("LEFT", "RED")
leds.set_color("RIGHT", "RED")