from time import sleep                                     #importing all libraries 
import board
from analogio import AnalogIn, AnalogOut
import simpleio 
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import motor

motorpin=AnalogOut(board.A0)                               #telling the arduino which pins do what 
potentiometer=AnalogIn(board.A1)

while True:
    print(potentiometer.value, (int(simpleio.map_range(potentiometer.value,0,65535,0,255)),))  #Mapping and printing potentiometer value
    sleep(.25)
    motorpin.value=potentiometer.value      #setting the motor to the mapped potentiometer value

