import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull               #importing all required libraries 

from lcd.lcd import CursorMode                                    #lcd cursor is 1 square, not a line

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

button_a = DigitalInOut(board.D3)
button_a.direction = Direction.INPUT
button_a.pull = Pull.UP

slide_a=DigitalInOut(board.D2)
slide_a.direction=Direction.INPUT                                 #setting up slide switch and button

#lcd tricks!

#lcd.clear()
#lcd.set_cursor_pos(1, 0)

# Make the cursor visible as a line:
#lcd.set_cursor_mode(CursorMode.LINE)

count=0                                                           #setting up count
prev_state = button_a.value                                       #setting up button on push

while True:
    cur_state = button_a.value
    if cur_state != prev_state:                                   #button on push loop
        if not cur_state:                   
            if slide_a.value == True:                             #if the slide value is true, increase number
                count += 1
                if count==0:
                    lcd.set_cursor_pos(0,9)
                    lcd.print(' ')
            else:                                                 #if the slide value is false, decrease number
                count -= 1
                if count==9:
                    lcd.set_cursor_pos(0,9)
                    lcd.print(' ')
            print(count)
            time.sleep(.1)
        prev_state = cur_state
    else:
        lcd.set_cursor_pos(0,0)                                   #telling LCD what to print
        lcd.print('button: ')
        lcd.print(str(count))
        lcd.set_cursor_pos(1,0) 
        lcd.print('switch: ')
        if slide_a.value == False:
           lcd.print('-')
        if slide_a.value == True:
            lcd.print('+')


           

