# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_Servo](#CircuitPython_Ultrasonic)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Turns the neopixel on and cycles through the colors of the rainbow. 

```python
from time import sleep
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1 

count=0

while True:
    count = count + 1
    dot.fill((255, 0, 0))
    sleep(.15)
    dot.fill((255, 165, 0   ))
    sleep(.15)
    dot.fill((255, 255, 0))
    sleep(.15)
    dot.fill((0, 255, 0))
    sleep(.15)
    dot.fill((0, 0, 255))
    sleep(.15)
    dot.fill((75, 0, 130))
    sleep(.15)
    dot.fill((238, 130, 238))
    sleep(.15)
    print('done with loop', count)
```


### Evidence


![neopixel_rainbow](https://media.giphy.com/media/i878kZAQd2ijZAM1FF/giphy.gif)



### Wiring
None needed

### Reflection
During this assignment, I had to figure out where to import the libraries, where to get the libraries, and which libraries were needed. You should download the UF2 file, then copy paste the correct .mpy into the lib folder of the circuitPython directory. I also had to remember how to do a counter, but it is much easier than I remembered. 


## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence
gif with credit
### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.


## CircuitPython_Ultrasonic

### Description & Code
In the distances meausered by an ultrasonic senseor between 5 and 35 cm, the neopixel will be mapped to fade from red to green.

```python
import time
import board
import neopixel
import adafruit_hcsr04
import simpleio                     #imported lib

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1                #setting up ultrasonic and neopixel

while True:
    try:
        cm=int(sonar.distance)      #defining cm as a variable of what the ultrasonic sensor is reading
        print(cm)
        if cm<5: 
            dot.fill((255, 0, 0))   #if the distance is less than 5 cm, red
            time.sleep(.15)
        elif 5<=cm<20:
            red=simpleio.map_range(sonar.distance,5,20,255,0)
            green=simpleio.map_range(sonar.distance,5,20,0,0)
            blue=simpleio.map_range(sonar.distance,5,20,0,255)
            dot.fill((red,green,blue))                   #smoothly trasition from red to blue as the distance goes from 5 to 20
            time.sleep(.05)
        elif 20<=cm<=35:   
            red=simpleio.map_range(sonar.distance,20,35,0,0)
            green=simpleio.map_range(sonar.distance,20,35,0,255)
            blue=simpleio.map_range(sonar.distance,20,35,255,0)
            dot.fill((red, green, blue))                 #smoothly trasition from blue to green as the distance goes from 20 to 35
            time.sleep(.05)
        elif cm>35:
            dot.fill((0, 255, 0))                        #if the distance is more than 35 cm, green
            time.sleep(.15)
        else:
            dot.fill((0, 0, 0))                          #if there is no reading, off
            time.sleep(.15)
    except RuntimeError:                                 #if there is no value found, tell us
        print("Retrying!")
    time.sleep(0.1)                                      #debounce
    
```

### Evidence

![servo_fade](https://media.giphy.com/media/yXlLEO7xj1HNUstS9G/giphy.gif)

### Wiring
![ciruit diagram ultrasonic](docs/ulrasonic%20circuit.png)
### Reflection
The hardest part of this assignment was figuring out how to map the values from cm of distance into 0-255 LED values. It took me a while to figure out how to do the mapping, but once i did, it all came fast from there. The format for ultrasonic sensors in circuitPython was copy pasted from the circuitPython webpage.



## CircuitPython_LCD

### Description & Code
When the slideswitch is true, every time the button is pressed the counter will go up by 1. When the slideswitch is false, the same thing will happen exept the values will go down. The LCD will print the counter and whether the slideswitch is positive or negative. 

```python
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
```

### Evidence
![lcd_in_action](https://media.giphy.com/media/u54T48FAGXANMkITiG/giphy.gif)

### Wiring
![circuit_diagram_lcd](docs/lcd%20circuit%20diagram.png)
### Reflection
I learnd a lot during this project. The hardest part was getting all the libraries and setting up all the particular circuitPython LCD requirements for it to work. I used the same settup for the switch as I did fot the button, which I had to figure out by myself because there is nothing on the internet for circuitPython slideswitches. I also had to figure out how to use button on push so it didn't count more than 1 time per push.  




## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence
gif with credit
### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.