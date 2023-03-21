import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull               
from lcd.lcd import CursorMode   
import neopixel  
import rotaryio                                                   #importing all required libraries

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP                                             #defining the button on the encoder

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1                                              #defining the neopixel

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16) #defining the LCD

encoder = rotaryio.IncrementalEncoder(board.D4, board.D3)
last_position = None                                               #defining the encoder

stoplight = ["Stop.", "Caution...", "Go!"]                         #making the array

prev_state = button.value                                          #setting up the on push loop

while True:
    cur_state = button.value                                       #setting things equal to what they need to be
    position = encoder.position

    if last_position is None or position != last_position:         #making the roatery encoder work on turn
        print(position)
        if position == 0:
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            lcd.print(stoplight[0])                                #telling the LCD what to print from the array when the encoder turns to a certain value
        elif position == 1:
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            lcd.print(stoplight[1]) 
        elif position == 2:
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            lcd.print(stoplight[2])

    if position == 0 and cur_state != prev_state:                   #push button loop to make the neopixel a certain color depending on the encoder value
        if not cur_state:
            dot.fill((255, 0, 0)) 
    elif position == 1 and cur_state != prev_state:                                   
        if not cur_state:
            dot.fill((255, 255, 0))  
    elif position == 2 and cur_state != prev_state:                                   
        if not cur_state:
            dot.fill((0, 255, 0)) 

    last_position = position                                        #resetting the encoder "value"
    
