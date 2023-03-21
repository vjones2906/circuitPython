import time
import board
import pwmio
import simpleio 
from adafruit_motor import servo
from analogio import AnalogIn 
from digitalio import DigitalInOut, Direction, Pull

button_a = DigitalInOut(board.D1)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

button_b = DigitalInOut(board.D2)
button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN

button_c = DigitalInOut(board.D3)
button_c.direction = Direction.INPUT
button_c.pull = Pull.DOWN

button_d = DigitalInOut(board.D4)
button_d.direction = Direction.INPUT
button_d.pull = Pull.DOWN

pot = AnalogIn(board.A1)   

# create a PWMOut object on Pin A2.
pwm_servo = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
pwm_servo1 = pwmio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
pwm_servo2 = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)


# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm_servo, min_pulse=1000, max_pulse=2000)  # tune pulse for specific servo
my_servo1 = servo.Servo(pwm_servo1)
my_servo2 = servo.Servo(pwm_servo2)

while True:
    if button_a.value:
        my_servo.throttle  = 1
        print("servo counterclockwise")
        time.sleep(0.1)
    elif button_b.value:
        my_servo.throttle = -.05
        print("servo clockwise")
        time.sleep(0.1)

    elif button_c.value:
        my_servo1.angle = 0
        print("servo 1 counterclockwise")
        time.sleep(0.1)
    elif button_d.value:
        my_servo1.angle = 180
        print("servo 1 clockwise")
        time.sleep(0.1)

    else:
        print((int(simpleio.map_range(pot.value,0,65535,0,180)) ))
        newpot = int(simpleio.map_range(pot.value,0,65535,0,180))
        my_servo2.angle = newpot

        my_servo.throttle = 0
        print("servo off")
        time.sleep(0.1)
