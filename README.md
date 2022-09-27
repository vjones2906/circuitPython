# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
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
![tinkercad.com](https://www.tinkercad.com/things/6xWfe0dYyqb-glorious-fulffy/editel?tenant=circuits)
### Reflection
The hardest part of this assignment was figuring out how to map the values from cm of distance into 0-255 LED values. It took me a while to figure out how to do the mapping, but once i did, it all came fast from there. The format for ultrasonic sensors in circuitPython was copy pasted from the circuitPython webpage.



## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





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