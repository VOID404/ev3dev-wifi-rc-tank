#!/usr/bin/env python

from bottle import run, get
from time import sleep, clock
from threading import Thread, currentThread
import ev3dev.ev3 as ev3
from sys import exit

left_motor = ev3.LargeMotor('outB')
right_motor = ev3.LargeMotor('outC')
motors = [left_motor, right_motor]

connected = False

def auto_emergency_stop():
    print('Ping recived')
    while True:
        global timestamp
        if clock()-timestamp>3: # Timeout in seconds
            print("NO PING")
            set_speed(0,0)
            set_speed(1,0)
            start_motor(0)
            start_motor(1)
            connected = False
            currentThread().exit()

timestamp = None
@get('/ping')
def ping():
    global connected
    global timestamp
    timestamp = clock()
    if not connected:
        connected=True
        Thread(target=auto_emergency_stop).start()

@get('/STOP')
def emergency_stop():
    set_speed(0,0)
    set_speed(1,0)
    start_motor(0)
    start_motor(1)

@get('/stop/<motor:int>')
def stop_motor(motor):
    motors[motor].stop()

@get('/start/<motor:int>')
def start_motor(motor):
    motors[motor].run_forever()

@get('/speed/<motor:int>/<speed:int>')
def set_speed(motor, speed):
    motors[motor].duty_cycle_sp = speed

@get('/_forward/<speed:int>')
def _forward(speed):
    set_speed(0, speed)
    set_speed(1, speed)
    start_motor(0)
    start_motor(1)

@get('/_turn_left/<speed:int>')
def _turn_left(speed):
    set_speed(0, -1*speed)
    set_speed(1, speed)
    start_motor(0)
    start_motor(1)

@get('/_turn_right/<speed:int>')
def _turn_right(speed):
    set_speed(0, speed)
    set_speed(1, -1*speed)
    start_motor(0)
    start_motor(1)

@get('/_stop')
def _stop():
    _forward(0)

run(host='192.168.1.109', port=8080)
