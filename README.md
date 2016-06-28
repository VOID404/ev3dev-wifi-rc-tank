# ev3dev wifi rc tank server
Remote controll server with REST API. It's written in python.
It uses [ev3dev](http://www.ev3dev.org/ "ev3dev homepage") (alternative ev3 os).

# Server

## dependencies
ev3dev - [ev3dev](http://www.ev3dev.org/ "ev3dev homepage") </br>
Bottle - python http server `pip install bottle`

## robot

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

# Client

## setup

## dependencies
ev3dev - [ev3dev](http://www.ev3dev.org/ "ev3dev homepage") </br>
Bottle - python http server `pip install bottle`

## usage
