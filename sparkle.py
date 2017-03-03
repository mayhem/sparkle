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

def set_color_hsv(strip, index, h, s, v):
    color = colorsys.hsv_to_rgb(h, s, v)
    set_color(strip, index, int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))

def main_loop(strip):
    dots = 10
    color_index = 0.0
    color_inc = .001
    while True:
        clear(strip)
        for i in range(dots):
            index = randint(0, numpixels - 1)
            set_color_hsv(strip, index, color_index, 1, 1) 

        strip.show();
        sleep(.1)
        color_index += color_inc


strip = Adafruit_DotStar(numpixels, order='bgr')

strip.begin()           
strip.setBrightness(70) 
startup(strip)

try:
    main_loop(strip)
except KeyboardInterrupt:
    off(strip)
    sys.exit(0)
