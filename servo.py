#thanks to afton for code guidelines 
import board                                                           #importing libraries
from time import sleep
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction
angle = 90


pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)         #connecting to servo

                                                                
my_servo = servo.Servo(pwm)                                            #Create a servo object
 
button = DigitalInOut(board.D1)                                        #telling what pins to input from the buttons
button.direction = Direction.INPUT
button2 = DigitalInOut(board.D2)
button2.direction = Direction.INPUT


while True:
    if button.value and angle < 180:                                  #telling the servo to move by 5 if the button is pressed
        angle += 5
    if button2.value and angle > 0:
        angle -=5
    print(angle)
    my_servo.angle = angle
    sleep(0.01)  