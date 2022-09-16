import time
import board
import neopixel
import adafruit_hcsr04
import simpleio
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1 
# neopixel turn red when your object is less than 5cm, blue when between 5 and 20cm, and green when farther than 20cm

while True:
    try:
        cm=int(sonar.distance)
        print(cm)
        if cm<5: 
            dot.fill((255, 0, 0))
            time.sleep(.15)
        elif 5<=cm<20:
        elif 20<=cm<=35:
            
            red=simpleio.map_range(sonar.distance,5,20,255,0)
            blue=simpleio.map_range(sonar.distance,5,20,255,0)
            dot.fill((red, green, blue))
            time.sleep(.15)
        elif cm>35:
            dot.fill((0, 255, 0))
            time.sleep(.15)
        else:
            dot.fill((0, 0, 0))
            time.sleep(.15)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    