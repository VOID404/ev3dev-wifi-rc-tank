'''
Those "undefined variable" errors are expected. Just ingnore them.
'''

import pygame, sys
from tank_client_lib import *
from pygame.locals import *


# config
DEBUG = False
speed = 100 # TODO: GUI slider or something like that: [<-100->]
rot_speed = 50
host = 'http://192.168.1.109:8080'


def debug(text):
    if DEBUG:
        print('DEBUG:{}'.format(text))

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((200, 100), 0, 32)
pygame.display.set_caption('Tank Client')

WHITE = (255, 255, 255)
windowSurface.fill(WHITE)

state = None
def update():
    global state
    if keys['left']:
        if state != 'left':
            debug('go left')
            state = 'left'
            turn_left(rot_speed)
    elif keys['right']:
        if state != 'right':
            debug('go right')
            state = 'right'
            turn_right(rot_speed)
    elif keys['up']:
        if state != 'up':
            debug('go up')
            state = 'up'
            forward(speed)
    elif keys['down']:
        if state != 'down':
            debug('go down')
            state = 'down'
            forward(-1*speed)
    else:
        if state != 'idle':
            debug('stop')
            state = 'idle'
            stop()

# draw the window onto the screen
pygame.display.update()

keys = {'up':False, 'down':False, 'left':False, 'right':False}
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_q and speed+5 <= 100:
            print("Speed: {0} \nRotation speed: {1}".format(speed, rot_speed))
            speed += 5
        elif event.type == KEYDOWN and event.key == K_a and speed-5 >= 0:
            print("Speed: {0} \nRotation speed: {1}".format(speed, rot_speed))
            speed -= 5

        if event.type == KEYDOWN and event.key == K_w and rot_speed+5 <= 100:
            print("Speed: {0} \nRotation speed: {1}".format(speed, rot_speed))
            rot_speed += 5
        elif event.type == KEYDOWN and event.key == K_s and rot_speed-5 >= 0:
            print("Speed: {0} \nRotation speed: {1}".format(speed, rot_speed))
            rot_speed -= 5

        if pygame.key.get_pressed()[K_UP]:
            keys['up']=True
        else: keys['up']=False
        if pygame.key.get_pressed()[K_DOWN]:
            keys['down']=True
        else: keys['down']=False
        if pygame.key.get_pressed()[K_LEFT]:
            keys['left']=True
        else: keys['left']=False
        if pygame.key.get_pressed()[K_RIGHT]:
            keys['right']=True
        else: keys['right']=False
    update()
