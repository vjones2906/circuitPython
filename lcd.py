import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

from lcd.lcd import CursorMode

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

button_a = DigitalInOut(board.D3)
button_a.direction = Direction.INPUT
button_a.pull = Pull.UP

slide_a=DigitalInOut(board.D2)
slide_a.direction=Direction.INPUT

#lcd.clear()
#lcd.set_cursor_pos(1, 0)
# Make the cursor visible as a line.
#lcd.set_cursor_mode(CursorMode.LINE)

print(slide_a.value)

count=0
prev_state = button_a.value

while True:
    cur_state = button_a.value
    if cur_state != prev_state:
        if not cur_state:
            if slide_a.value == False:
                count = count + 1
            else:
                lcd.set_cursor_pos(1,12)
                lcd.print(' ')
                count = count - 1
            print(count)
            time.sleep(.3)
        else:
            lcd.set_cursor_pos(0,0) 
            lcd.print('button: ')
            lcd.print(str(count))
            lcd.set_cursor_pos(1,0) 
            lcd.print('switch: ')
            lcd.print(str(slide_a.value))
        prev_state = cur_state