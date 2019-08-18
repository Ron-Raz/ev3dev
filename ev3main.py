#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

leds=Leds()
ledsGreen()

import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server='192.168.2.1'
port=7777

ts = TouchSensor()
#url="http://192.168.2.1:8080/events"

def top_left_channel_1_action(state):
    print("top left on channel 1: %s" % state)

def bottom_right_channel_4_action(state):
    print("bottom right on channel 4: %s" % state)

def ledsOff():
	leds.all_off()

def ledsGreen():
	leds.set_color('LEFT','GREEN')
	leds.set_color('RIGHT','GREEN')

ir = InfraredSensor()
ir.on_channel1_top_left = top_left_channel_1_action
ir.on_channel4_bottom_right = bottom_right_channel_4_action
#sound = Sound()
#sound.speak('Welcome to the E V 3 dev project!')
msg='foobar'
countdown=10
while countdown>0:
	#ir.process()
	if ts.is_pressed:
		sock.sendto(msg.encode(),(server,port))
		print(countdown,ts.is_pressed)
		countdown-=1
	#time.sleep(0.01)

ledsOff()
