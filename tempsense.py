#thanks to Afton for some key parts of this code
import board                                    
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface                       #importing libs
from analogio import AnalogIn
from lcd.lcd import CursorMode                             
from time import sleep
from simpleio import map_range
import digitalio

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)              #defining the LCD

raw = AnalogIn(board.A2)                                                        #Analog input for sensor

temp = 0        
tchange = 0                                                                     #defining values

temp_says = ["brrr Too Cold!", "feels great :)", "Too Hot!"]                    #making the array


while True:
    temp = round((raw.value-500)/ 576,1)                                        #temp = map_range(raw.value, 0, 100, 0, 100)
    if tchange != temp:
        lcd.clear()
        lcd.print("T: " + str(temp) +"C  " + str(round((temp * 1.8) + 32,1)) + "F ")  #printing temp in celcius and fahrenheit  
        if temp > 23:                                                           #giving values and telling the lcd what to print
            lcd.print(temp_says[2])
        elif temp < 20:
            lcd.print(temp_says[0])
        else:
            lcd.print(temp_says[1])
        tChange = temp                                                          #resetting values
        print(temp)
    sleep(1) 
 