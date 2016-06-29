# ev3dev wifi rc tank server
-------------
# Server
Remote controll server with REST API. It's written in python.
It uses [ev3dev](http://www.ev3dev.org/ "ev3dev homepage") (alternative ev3 os).

## dependencies
ev3dev - [ev3dev](http://www.ev3dev.org/ "ev3dev homepage") </br>
Bottle - python http server `pip install bottle`

## robot
It's [Track3r](http://www.lego.com/en-us/mindstorms/build-a-robot/track3r) with phone stand.
![](photos/IMG_0847.png?raw=true "Front")
![](photos/IMG_0848.png?raw=true "Right")
![](photos/IMG_0849.png?raw=true "Back")

## setup
Hardcoded values:
* ip and port (last line)
* list of motors (9th and 10th line)
* emergency stop timeout (19th line, you don't have to use it)

## API doc
Everything is using GET method.

| url | arguments | what it does |
|-----|-----------|--------------|
| `/ping` | none | when you first time send it it activates thread that stops motors if you don't send it |
| `/STOP` | none | stops motors (designed as emergency stop) |
| `/stop/<motor>` | motor - int, read lines 9-10 | stops motor, so it can freely rotate |
| `/start/<motor>` | motor - int, read lines 9-10 | starts motor, remember to set speed |
|`/speed/<motor>/<speed>` | motor - int, same as above, speed - int, percentage | sets speed for motor |
|`/_forward/<speed>` | speed - int, percentage | sets speed for both motors and starts them |
| `/_turn_left/<speed>` | speed - same as above | sets speed for one motor and -speed for second, then starts them |
|`/_turn_right/<speed>` | same as above | same as above |
| `/_stop` | none | sets speed for both motor to 0 and starts them (it prevents rotating freely)

---------
# Client
Client uses 2 files because it's easier to test that way - one
file doesn't require http connection and second one doesn't
require GUI. Here is GUI part: [tank_client.py](client/tank_client.py) and here is http part: [tank_client_lib.py](client/tank_client_lib.py)

## setup
Hardcoded values:
* ip and port (6th line)
* delay between pings (24th line)

## dependencies
I've used python3. It MAY be compatible with 2.7, but I'm not sure. I will make it compatible.

Pygame - python game engine
Requests - http requests library `pip3 install requests`

## usage  
