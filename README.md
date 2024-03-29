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
* [Temperature_LCD](#Temperature_LCD)
* [Rotary_Encoder](#Rotary_Encoder)
* [Photointerrupter](#Photointerrupter)
* [Certification](#Certification)


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
The goal of this assignment was to move a 180 servo by pushing buttons. One of the buttons would move it clockwise and the other counter-clockwise. If the buttons were not being pressed the servo should not move.
```python
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
```
### Evidence
![servo_gif](docs/ezgif.com-video-to-gif%20(1).gif)
### Wiring
![servo_wiring](docs/servowire.png)
### Reflection
This assignment was very frustrating. I spent almost 2 class periods on it when I finally realized the servo I picked up from the 180 servo bin was actually a continuous servo. The code I had been working on and the wiring was right, I just had the wrong servo. I learned how to use inputs and outputs while doing this assignment. Link to Afton's Github: https://github.com/Avanhoo/CircuitPython 

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
The goal of this assignment was to practice assembling parts in onshape to prepare us for the exam. 
### Evidence
![Assemley_assembled](docs/assemblypic.png)

link: https://cvilleschools.onshape.com/documents/7ce903cc5915923b359f506c/w/e7e3524a56c729e04c37baed/e/c8543076275e207bb2c0158b
### Reflection
This assignment was not too hard, but I did cut a few corners that impacted me later. I didn't order some of the revolute mates correctly, so it moved in an incorrect fasion which made getting the values a bit harder. 

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
We already did this assignment last year and I did multiple projects which included motot control so it was easy to do again. I needed a little help with the code and then the hardest part was figuring out why the motor wouldn't work. It ended up being the order in which the analog pins were declared. The motor pin needs to come before the potentiometer pin. If I were to do this again I would use the "in-between" feature in order to mate more accurately. I would be more careful of the order in which I mate certain things because  mating them incorrectly makes finding the quesiton values harder.



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
### Prototype:

![prototype_pic](/docs/IMG-5075.jpg)


### Circuit with all the servos running:

#### Crank/release servo:

![big_servo_1](/docs/ezgif.com-video-to-gif%20(5).gif)
#### Turntable servo:
![big_servo_2](/docs/ezgif.com-video-to-gif%20(6).gif)
#### Gripper servo:
![small_servo](/docs/ezgif.com-video-to-gif%20(7).gif)


### Assembled CAD (as is):

![CAD](/docs/cadarm.png)

Link: https://cvilleschools.onshape.com/documents/e8cf7f51ade30afad8ba4cc3/w/c00bdf382ea5b91e203aaeed/e/ef81620b3dca0a4067e5af3c
### Wiring
![robotarm](https://github.com/vjones2906/circuitPython/blob/master/docs/robotarm_wiring.png)
### Reflection
This project was a challenge for my group. We didn't end up finishing everything and didn't even laser cut the CAD model. The plan was to split the CAD and code between the group members so that Vinnie did all the code and did the circuit while Will did all the CAD. Vinnie ended up finishing the code early and jonied will in trying to finish the CAD. Beacause of how the dimensions were done in CAD before Vinnie came, he had to define and redo most of the dimensions. This slowed down the proccess significantly. The group spent time making CAD parts before thinking them through to completion, which only led to more work for them later. Will also missed quite a few days during the in-class time to work on the project, and not all the classtime we had was spent in a productive matter. If the group had spent any amount of time on the project after school or if they used the time they had wisely, the project could have been completed. In the end the group had a perfectly functioning circuit and code, a CAD document that was close to completion, and a prototype. All the group had to do to complete their project was finish, cut, and assemble the CAD shell. The project taught us to plan every step carefully before it was attempted. The group spent lot of time finding a solution to the inital problem and ended up with a general idea of how to do it, but failed to plan the smaller steps. We spent several class periods brainstorming techniques. We thought about using a string and a crank to lift the arm up. We thought about a crane-like structure with a gearbox to increase the torque of the servo. We thought about having a really short arm and spinning it just with a motor. Eventually we settled on using a servo to lift a stick and raise the arm. We realized it couln't lift the arm by itself and we needed a notch in the arm in order for the stick to latch in and take it to the desired hight. It also taught us that if we didn't use our time wisely, deadlines will sneak up on us.


## Temperature_LCD

### Description & Code
The goal of this assignment is to read the temperature in the room, print it on an LCD, and then display whether or not the temperature is in a desired range.
```python
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
```
### Evidence
![temp_gif](docs/ezgif.com-video-to-gif%20(2).gif)
### Wiring
![temp_wiring](docs/tempwire.png)
### Reflection
This assignment was difficult to figure out at first. Make sure to find compatable code if you look online becasuse when I was looking for some example code I ended up finding a wrong version and basing my whole V1 off of it. It had many extra value conversions that were meant to read the input correctly. Make sure you know that all the Metro needs to read the values correctly is AnalogIn(board.pin) which saves a lot of code and time. I ended up having afton help me out with the finer details of the code. I figuresd out that you can use an array to print the things you want to say on the LCD easier. Make sure to adjust the contrast using the little screw on the back of the LCD backpack if you want to see the screen! Link to Afton's Github: https://github.com/Avanhoo/CircuitPython  


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
The main challenge of this assingment was trying to do the C++ code in python. The whole assingment was meant for C++ so all the tips and all of the learning was not in python. There are plenty of websites online which provide code for a rotary enoder in python, an example of which is https://learn.adafruit.com/rotary-encoder/circuitpython. I learned about arrays and how an encoder actually works. One of the main problems I had with the code itself was which loop would go before the other. It took a lot of trying and a lot tweaking to find the exact right order. In order to find the right order, I found it helpful to think about the loops as a family and then draw out a family tree and then match which loops goes to which person. If you draw it out like this is helps your brain realize what loop HAS to exist for another to function.  


## Photointerrupter

### Description & Code
The goal of this assignment was to show how many times the photointurrupter was inturrupted in 4 second intervals. 
```python
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
```
### Evidence
![photointurrupter_gif](/docs/ezgif.com-video-to-gif%20(4).gif)   
### Wiring
![Photointurrupter_wiring](/docs/photowiring.png)
### Reflection
This challenges of this assignment were to figure out how monotonic time works and how to best orient the loops. Afton helped me out with some of the code to give me a general idea of where I should be headed. I had a couple issues with my lcd library that took some time to fix and then some issues with the display itself. If you are having trouble with your libraries I found it easiest to delete the existing library from your folder (if it is there) and then copy the .mpy file straight from the circuitpython bundle back to the lib folder. I learned a lot from this assignment and will probably use the monotonic time and the knowledege of loop nesting in the future. Link to Afton's Github: https://github.com/Avanhoo/CircuitPython 


## Certification

### Description 
The goal of this assignment was to get an Onshape Certification. We would take a 4 part test in 3 hours in order to acheive this. The first part was creating a swing arm, the second part was making a multi-part studio, the third part was creating a functioning assembly, and the final part was multiple choice. 
### Evidence
![onshapecertified](https://github.com/vjones2906/circuitPython/blob/master/docs/onshapecertified.png)
### Reflection
This took me 2 attemps to get. A passing score was a 75, and I got a 73 on the first attempt. I figured out a problem with my multi-part studio in the last 2 minutes of the exam and didn't have enough time to fix it. If you want to get faster at something you need to practice it, and that's what I did. I re-did the multi-part studio and assembly many times and each time I got faster. Some helpful shortcuts I figured out was if you type "e" it will set two values equal to eachother. I also learned that you can use the middle click of your mouse to move around in onshape without spinning your view. When I took the test a second time, where the exam was almost the exact same as the first time. When you take this type of test you should be very careful and look for all small details in the drawings before attempting to re-create them. I ended up passing the second time around and getting my onshape certificate. 