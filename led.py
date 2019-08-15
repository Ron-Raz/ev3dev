#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

import time
# TODO: Add code here
leds = Leds()

leds.set_color("LEFT", "GREEN")
time.sleep(.500)
leds.set_color("RIGHT", "YELLOW")
time.sleep(.500)
leds.set_color("LEFT", "RED")
time.sleep(.500)
leds.set_color("RIGHT", "GREEN")
time.sleep(.500)
leds.set_color("LEFT", "GREEN")
