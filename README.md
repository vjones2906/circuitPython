# CircuitPython
## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython Servo](#CircuitPython_Servo)
* [CircuitPython_Ultrasonic](#CircuitPython_Ultrasonic)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Pull_Coptor](#Pull_Copter)
* [Swing_Arm](#Swing_Arm)
* [Multi-Part_Studio](#Multi-Part_Studio)
* [Onshape Assembly](#Onshape_Assembly)
* [Motor_Control](#Motor_control)
* [Bowling_Ball_Arm](#Bowling_Ball_Arm)
* [Temperature_LED](#Temperature_LED)
* [Rotary_Encoder](#Rotary_Encoder)
* [Photointerrupter](#Photointerrupter)
* [Certification](#Certification)
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
### Reflection
During this assignment, I had to figure out where to import the libraries, where to get the libraries, and which libraries were needed. You should download the UF2 file, then copy paste the correct .mpy into the lib folder of the circuitPython directory. I also had to remember how to do a counter, but it is much easier than I remembered. 


## CircuitPython_Servo

### Description & Code
```python

```
### Evidence
![___](__)
### Wiring
![___](__)

### Reflection


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
![lcd_in_action](https://github.com/vjones2906/circuitPython/blob/master/docs/ezgif.com-video-to-gif.gif)
### Wiring
![circuit_diagram_lcd](docs/lcd%20circuit%20diagram.png)
### Reflection
I learnd a lot during this project. The hardest part was getting all the libraries and setting up all the particular circuitPython LCD requirements for it to work. I used the same settup for the switch as I did fot the button, which I had to figure out by myself because there is nothing on the internet for circuitPython slideswitches. I also had to figure out how to use button on push so it didn't count more than 1 time per push.  


## Pull_Copter 

### Description 
This goal of this assignment was to teach us how to collaborate in a single CAD document using branches and versions. We created a pull copter with realistic physics and then 3D printed it. There were two students with different rolls, student A and student B.
### Evidence
![pull copter](https://user-images.githubusercontent.com/112962101/197562548-5c4571a7-1cc3-4c0e-9814-c7d1b1db0804.png)

link: https://cvilleschools.onshape.com/documents/28913ae2144b614eeb24c495/w/07076b2bb0e8b82fca19e7b7/e/f1940db3c9019138372953fc
### Reflection
This project went longer than intended because I got sick and my partner, River, had to wait for me to finish. This was challenging to figure out what parts needed to be completed in branches and what parts needed to be collaberated on. It was also hard to figure out how to do some of the geometry, but overall was just a review of last year. 


## Swing_Arm

### Description 
This goal of this assignment was to use drawings, geometry, and variables to create an exact replica of a part and then be able to make different versions of it. 
### Evidence
![Swing Arm](https://user-images.githubusercontent.com/112962101/197563924-61553a7c-4b80-4dc1-924e-1fd85104f3ef.png)

link: https://cvilleschools.onshape.com/documents/73ad9d41ee7d879dcb33ed27/w/569388fec521f1599875ce0a/e/f1f88169fac4697a44e93ff0
### Reflection
It was difficult getting started on this assignment beacuse I didn't know how to use onshape's geometry at first. There were a few parts of my sketch that I did the wrong way and then had to go back and fix. It taught me to sketch and dimension off of other sketches so if you change something, they all agree. It was also hard interpreting the drawings at first. I learned that cross-sections are very useful. 


## Multi-Part_Studio

### Description 
The goal of this assignment was to use design intent to create the parts so that something can be changed, and everything else will have the same relation to that change. All of the parts in this project were made in the same "studio". 
### Evidence
![Question 1](https://user-images.githubusercontent.com/112962101/197566214-2729eea8-57a2-49bd-9361-19d433e30aaa.png)
![Question 2](https://user-images.githubusercontent.com/112962101/197566233-ca3269b0-2589-4f52-8b08-cb4786a4b6e6.png)
![Question 3](https://user-images.githubusercontent.com/112962101/197566238-da6182d3-b9af-4e5e-90a2-0195e896c2cd.png)
![Question 4](https://user-images.githubusercontent.com/112962101/197566291-0f656ed5-cf45-4a5c-b412-bbc959fef8f6.png)

link: https://cvilleschools.onshape.com/documents/ec01c6bd7bee84627b463f60/w/1764f5923d829c1db0ec3661/e/9ce24ba94ecc458e08fa5093
### Reflection
This project was hardest in the first 2 questions. In the first one you simply had to create everything, and in the second one you saw how poorly you designed most of your sketches and extrudes. The 3rd question had a couple things go wrong, but were easy to fix and the fourth went perfectly. Doing this project really showed me how important design intent is when creating something that is meant to be changed. The more variables or "moving parts" the more precise and well planned all your work has to be. I used cross sections a lot and got some help from Dylan and Jinho.


## Onshape_Assembly

### Description 

### Evidence
![___](__)
### Wiring
![___](__)
### Reflection


## Motor_Control 

### Description & Code
The goal of this assignment was to control a  motor with a potentiometer. If the potentiometer is turned up, the motor rotates faster. 
```python
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
```

### Evidence
![motor](https://github.com/vjones2906/circuitPython/blob/master/docs/ezgif.com-crop.gif)
### Wiring
![motorcontrol](https://github.com/vjones2906/circuitPython/blob/master/docs/motorcontrol.png)
### Reflection
We already did this assignment last year and I did multiple projects which included motot control so it was easy to do again. I needed a little help with the code and then the hardest part was figuring out why the motor wouldn't work. It ended up being the order in which the analog pins were declared. The motor pin needs to come before the potentiometer pin. 



## Bowling_Ball_Arm 

### Description & Code
The purpose of this assignment was to create a specialized robot arm. The arm we created was a gravity-run mini bowling ball arm. The box was on a turn table, and then the arm itself was on an ball bearing axel. There was a servo with an arm above it that would spin and lock in the arm and then keep spinning to raise it. Then when it reached a certain angle the crank arm would slide out. After it would slide out then the arm would be free to swing down on the axel. Then a button would be pressed and the clamps would release the ball and it would fly forward hitting the targets. In total there would be 4 buttons and a potentiometer. The buttons would control the servo to lift up the arm and the release of the claw. The potentiometer would control the heading of the turntable. 
```python
import time
import board
import pwmio
import simpleio 
from adafruit_motor import servo
from analogio import AnalogIn 
from digitalio import DigitalInOut, Direction, Pull

button_a = DigitalInOut(board.D1)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

button_b = DigitalInOut(board.D2)
button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN

button_c = DigitalInOut(board.D3)
button_c.direction = Direction.INPUT
button_c.pull = Pull.DOWN

button_d = DigitalInOut(board.D4)
button_d.direction = Direction.INPUT
button_d.pull = Pull.DOWN

pot = AnalogIn(board.A1)   

# create a PWMOut object on Pin A2.
pwm_servo = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
pwm_servo1 = pwmio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
pwm_servo2 = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)


# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm_servo, min_pulse=1000, max_pulse=2000)  # tune pulse for specific servo
my_servo1 = servo.Servo(pwm_servo1)
my_servo2 = servo.Servo(pwm_servo2)

while True:
    if button_a.value:
        my_servo.throttle  = 1
        print("servo counterclockwise")
        time.sleep(0.1)
    elif button_b.value:
        my_servo.throttle = -.05
        print("servo clockwise")
        time.sleep(0.1)

    elif button_c.value:
        my_servo1.angle = 0
        print("servo 1 counterclockwise")
        time.sleep(0.1)
    elif button_d.value:
        my_servo1.angle = 180
        print("servo 1 clockwise")
        time.sleep(0.1)

    else:
        print((int(simpleio.map_range(pot.value,0,65535,0,180)) ))
        newpot = int(simpleio.map_range(pot.value,0,65535,0,180))
        my_servo2.angle = newpot

        my_servo.throttle = 0
        print("servo off")
        time.sleep(0.1)
```
### Evidence
gif with credit
### Wiring
![robotarm](https://github.com/vjones2906/circuitPython/blob/master/docs/robotarm_wiring.png)
### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.


## Temperature_LED

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


## Rotary_Encoder 

### Description & Code
The end goal for this project is to have an LCD, rotary encoder, and a neopixel all work together. When the rotary encoder would change values from 0-2 the LCD would display Stop, Caution, or Go depending on the value. Then when one of those is selected, the button on the encoder could be pushed and the neopixel would light up to the corresponding color (red-stop, green-go, yellow-caution).
```python
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull               
from lcd.lcd import CursorMode   
import neopixel  
import rotaryio                                                    #importing all required libraries

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP                                              #defining the button on the encoder

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1                                               #defining the neopixel

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
```
### Evidence
![rotary_encoder](https://media.giphy.com/media/g78CPxbHUdv7Wm6lpZ/giphy.gif)
### Wiring
![encoderwiring](https://github.com/vjones2906/circuitPython/blob/master/docs/encoderwiring.png) 
### Reflection
The main challenge of this assingment was trying to do the C++ code in python. The whole assingment was meant for C++ so all the tips and all of the learning was not in python. I learned to use certain websites online to aid me in the learning, and I had to imporvise quite a few times. I learned about arrays and how an encoder actually works. One of the main problems I had with the code itself was which loop would go before the other. It took a lot of trying and a lot tweaking to find the exact right order. 


## Photointerrupter

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


## Certification

### Description 
The goal of this assignment was to get an Onshape Certification. We would take a 4 part test in 3 hours in order to acheive this. The first part was creating a swing arm, the second part was making a multi-part studio, the third part was creating a functioning assembly, and the final part was multiple choice. 
### Evidence
![___](_____)
### Reflection
This took me 2 attemps to get. A passing score was a 75, and I got a 73 on the first attempt. I figured out a problem with my multi-part studio in the last 2 minutes of the exam and didn't have enough time to fix it. I went home and practicecd the multi-part studio and assembly many times in order to get faster at it. I then took the test a second time, where the exam was almost the exact same as the first time.  


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

