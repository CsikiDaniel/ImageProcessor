import socket
from time import sleep
import RPi.GPIO as GPIO

backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.9', 9527))
s.listen(backlog)

# Setup Robot
GPIO.setmode(GPIO.BCM)
delay = 0.000195  # in 16-th step
steps = 150

# Motor 1 - Horizontal motor
Enable_M1 = 16
Direction_M1 = 20
Step_M1 = 21

right = 1
left = 0

GPIO.setup(Enable_M1, GPIO.OUT)
GPIO.setup(Direction_M1, GPIO.OUT)
GPIO.setup(Step_M1, GPIO.OUT)

# Motor 2 - Vertical motor
Enable_M2 = 14
Direction_M2 = 15
Step_M2 = 18

up = 1
down = 0

GPIO.setup(Enable_M2, GPIO.OUT)
GPIO.setup(Direction_M2, GPIO.OUT)
GPIO.setup(Step_M2, GPIO.OUT)

GPIO.output(Enable_M1, GPIO.HIGH)
GPIO.output(Enable_M2, GPIO.HIGH)


def enable_M1():
    GPIO.output(Enable_M1, GPIO.LOW)


def disable_M1():
    GPIO.output(Enable_M1, GPIO.HIGH)


def enable_M2():
    GPIO.output(Enable_M2, GPIO.LOW)


def disable_M2():
    GPIO.output(Enable_M2, GPIO.HIGH)


def move_left():
    enable_M1()
    disable_M2()
    GPIO.output(Direction_M1, left)

    for step in range(steps):
        GPIO.output(Step_M1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M1, GPIO.LOW)
        sleep(delay)


def move_right():
    enable_M1()
    disable_M2()
    GPIO.output(Direction_M1, right)

    for step in range(steps):
        GPIO.output(Step_M1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M1, GPIO.LOW)
        sleep(delay)


def move_up():
    disable_M1()
    enable_M2()
    GPIO.output(Direction_M2, up)

    for step in range(steps):
        GPIO.output(Step_M2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.LOW)
        sleep(delay)


def move_down():
    disable_M1()
    enable_M2()
    GPIO.output(Direction_M2, down)

    for step in range(steps):
        GPIO.output(Step_M2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.LOW)
        sleep(delay)


def move_left_and_down():
    enable_M1()
    enable_M2()
    GPIO.output(Direction_M1, left)
    GPIO.output(Direction_M2, down)

    for step in range(steps):
        GPIO.output(Step_M1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M1, GPIO.LOW)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.LOW)
        sleep(delay)


def move_left_and_up():
    enable_M1()
    enable_M2()
    GPIO.output(Direction_M1, left)
    GPIO.output(Direction_M2, up)

    for step in range(steps):
        GPIO.output(Step_M1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M1, GPIO.LOW)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.LOW)
        sleep(delay)


def move_right_and_up():
    enable_M1()
    enable_M2()
    GPIO.output(Direction_M1, right)
    GPIO.output(Direction_M2, up)

    for step in range(steps):
        GPIO.output(Step_M1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M1, GPIO.LOW)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.LOW)
        sleep(delay)


def move_right_and_down():
    enable_M1()
    enable_M2()
    GPIO.output(Direction_M1, right)
    GPIO.output(Direction_M2, down)

    for step in range(steps):
        GPIO.output(Step_M1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M1, GPIO.LOW)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(Step_M2, GPIO.LOW)
        sleep(delay)


def stay_center():
    disable_M1()
    disable_M2()


try:
    client, address = s.accept()
    while True:
        data = client.recv(size)

        if len(data) == 4:
            decoded = data.decode('utf-8')
            answer = ''
            if decoded == '1000':
                move_left()
                print('Left')
            elif decoded == '0100':
                move_right()
                print('Right')
            elif decoded == '0010':
                move_up()
                print('Up')
            elif decoded == '0001':
                move_down()
                print('Down')
            elif decoded == '1010':
                move_left_and_up()
                print('Left & Up')
            elif decoded == '1001':
                move_left_and_down()
                print('Left & Down')
            elif decoded == '0110':
                move_right_and_up()
                print('Right & Up')
            elif decoded == '0101':
                move_right_and_down()
                print('Right & Down')
            elif decoded == '0000':
                stay_center()
                print('Center')
            client.send(data)
except:
    print("Closing socket")
    client.close()
    s.close()
