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


![spinningMetro_Optimized](https://media.giphy.com/media/i878kZAQd2ijZAM1FF/giphy.gif)



### Wiring
none needed

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection




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

### Wiring

### Reflection