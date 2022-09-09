from time import sleep
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((0, 0, 255))
    sleep(1)
    dot.fill((0, 0, 0))
    sleep(1)
    dot.fill((255, 0, 0))
    sleep(1)
    dot.fill((0, 0, 0))
    sleep(1)
    dot.fill((0, 255, 0))
    sleep(1)
    dot.fill((0, 0, 0))
    sleep(1)