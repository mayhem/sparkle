#!/usr/bin/env python
import sys
import os
import colorsys
from random import randint
from time import sleep, time
from dotstar import Adafruit_DotStar

numpixels = 144 # Number of LEDs in strip

def clear(strip):
    for row in xrange(numpixels):
        strip.setPixelColor(row, 0)

def off(strip):
    clear(strip)
    strip.show()

def startup(strip):

    for repeat in xrange(5):
        for row in xrange(10 / 4):
            strip.setPixelColor(row * 4, 0xFFAA00)
            strip.setPixelColor(row * 4 + 1, 0xFFAA00)
            strip.setPixelColor(row * 4 + 2, 0xFF00FF)
            strip.setPixelColor(row * 4 + 3, 0xFF00FF)

        strip.show();
        sleep(.1)

        for row in xrange(10 / 4):
            strip.setPixelColor(row * 4, 0xFF00FF)
            strip.setPixelColor(row * 4 + 1, 0xFF00FF)
            strip.setPixelColor(row * 4 + 2, 0xFFAA00)
            strip.setPixelColor(row * 4 + 3, 0xFFAA00)

        strip.show();
        sleep(.1)

    clear(strip)

def set_color(strip, index, r, g, b):
    strip.setPixelColor(index, r << 16 | g << 8 | b)

palette = { 0x6B0848, 0xA40A3C, 0x#EC610A, 0x#FFC300 }

def main_loop(strip):
    leds = []
    for i in range(numpixels):
        leds.append([0,0,0])

    dots = 10
    while True:
        clear(strip)
        for i in range(dots):
            index = randint(0, len(palette) - 1)
            leds[index][0] = palette[index] >> 16
            leds[index][1] = (palette[index] >> 8) & 0xFF
            leds[index][2] = palette[index] & 0xFF
            for j, l in enumerate(leds):
                set_color(strip, j, leds[j][0], leds[j][1], leds[j][2])

        strip.show();
        sleep(.05)


strip = Adafruit_DotStar(numpixels, order='bgr')

strip.begin()           
strip.setBrightness(70) 
startup(strip)

try:
    main_loop(strip)
except KeyboardInterrupt:
    off(strip)
    sys.exit(0)
