from requests import get
from threading import Thread
from time import sleep
from queue import Queue

host = 'http://192.168.1.109:8080'

requests = Queue(16)
def httpGet(url):
    get(url)
    #requests.put(url)

def httpGet2():
    while True:
        if not requests.empty():
            url = requests.get()
            #print(url)
            get(url)

Thread(target=httpGet2).start()
def ping():
    while True:
        Thread(target=get, args=(host + '/ping', )).start()
        sleep(2)
Thread(target=ping).start()

def set_speed(speed):
    speed = str(speed)
    httpGet(host + '/speed/0/' +str(speed))
    httpGet(host + '/speed/1/' +str(speed))

def start():
    httpGet(host + '/start/0')
    httpGet(host + '/start/1')

def forward(speed):
    '''
    set_speed(speed)
    start()'''
    requests.put(host+'/_forward/'+str(speed))

def stop():
    #forward(0) # There could also be 'host/stop/motor', but it would 'disconnect' motor. It would keep rotating limply.
    requests.put(host+'/_stop')

def turn_left(speed):
    '''
    httpGet("{0}/speed/1/{1}".format(host, speed))
    httpGet("{0}/speed/0/-{1}".format(host, speed))
    start()'''
    requests.put(host+'/_turn_left/'+str(speed))

def turn_right(speed):
    '''
    httpGet("{0}/speed/0/{1}".format(host, speed))
    httpGet("{0}/speed/1/-{1}".format(host, speed))
    start()'''
    requests.put(host+'/_turn_right/'+str(speed))
