import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import analogio
import digitalio
from lcd.lcd import CursorMode                             #importing libs
import time

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16) #defining the LCD

temp = ["brrr Too Cold!", "feels great :)", "Too Hot!"]    #making the array

TMP36_PIN = board.A1                                       # Analog input connected to TMP36 output.

def tmp36_temperature_C(analogin):                         # Function to simplify the math of reading the temperature.
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10

tmp36 = analogio.AnalogIn(TMP36_PIN)                       # Create TMP36 analog input.

lcdPower = digitalio.DigitalInOut(board.D8)                # turn on lcd power switch pin
lcdPower.direction = digitalio.Direction.INPUT
lcdPower.pull = digitalio.Pull.DOWN

while lcdPower.value is False:                             
    print("still sleeping")
    time.sleep(0.1)

# Time to start up the LCD!
time.sleep(1)
print(lcdPower.value)
print("running")

while True:
    temp_C = tmp36_temperature_C(tmp36)                    # Read the temperature in Celsius.
    temp_F = (temp_C * 9/5) + 32                           # Convert to Fahrenheit.
    print("Temperature: {}C {}F".format(temp_C, temp_F))   # Print out the value 
    time.sleep(0.5)    
    if temp_F < 75:                                        #setting ranges for values
        lcd.clear()
        lcd.print(temp[0])                                 #printing desired output
    elif 75 < temp_F < 95:
        lcd.print(temp[1])
    elif temp_F > 95:
        lcd.clear()
        lcd.print(temp[2])
    lcd.set_cursor_pos(0,0)
 