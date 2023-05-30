#thanks to afton for some key parts to the code 
import board                                                                    #importing libs
from time import monotonic, sleep
from digitalio import DigitalInOut, Pull, Direction
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)              #defining the LCD

now = monotonic()                                                               #Time in seconds since power on

photo = DigitalInOut(board.D8)              
photo.direction = Direction.INPUT
photo.pull = Pull.UP                                                            #defining photointurrupter

count = 0
count2 = 0
timeStart = 0                                                                   #defining vars

while True:
    if photo.value:
        count += 1
        while photo.value:
            pass                                                                
    if (float(timeStart + 4) < monotonic()):                                    #setting the 4 second loop
        print("Interrupts: " + str(count))
        lcd.clear()
        lcd.print("In Interval " + str(count2) + ":  Detected " + str(count) + " Times") #printing on LCD
        count2 += 1
        count = 0                                                               #changing counts
        timeStart = monotonic()
