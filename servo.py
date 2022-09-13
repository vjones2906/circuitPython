"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

from digitalio import DigitalInOut, Direction, Pull

button_a = DigitalInOut(board.D1)
button_a.direction = Direction.INPUT
button_a.pull = Pull.UP

button_b = DigitalInOut(board.D2)
button_b.direction = Direction.INPUT
button_b.pull = Pull.UP

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    if button_a.value:
        for angle in range(0, 180, 10):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            print("servo counterclockwise")
            time.sleep(0.05)
    elif button_b.value:
        for angle in range(180, 0, -10): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
            print("servo clockwise")
            time.sleep(0.05)
    else:
        print("servo off")
        time.sleep(0.5)