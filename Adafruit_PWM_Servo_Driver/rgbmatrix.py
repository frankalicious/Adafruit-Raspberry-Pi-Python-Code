#!/usr/bin/python

import time
import math
import random
from PIL import Image
from Adafruit_I2C import Adafruit_I2C

# ============================================================================
# Adafruit rgb matrix
# ============================================================================

class MATRIX :
  i2c = None

  def __init__(self, address=0x55, debug=False):
    # self.i2c = Adafruit_I2C(address, debug=True)
    self.i2c = Adafruit_I2C(address, debug=False)
    self.address = address
    self.debug = debug

  def endless_random(self):
    print 'endless random values...'
    # rand_list = [random.randint(0,255) for i in range(33)]
    while True:
      rand_list = [random.randint(0,255) for i in range(33)]
      self.i2c.writeList(rand_list[0],rand_list[1:])
      # time.sleep(0.01)

  def endless_solid(self):
    print 'endless solid color...'
    # color_list = [0xff,0x00,0x00]
    # color_list = [0xa,0xb,0xc]
    # color_list += [0xd,0xe,0xf]
    color_list = [0x00,0x00,0x00]
    # color_list = [0xff,0x00,0x00]
    # color_list += [0xff,0xff,0x00]
    # color_list += [0x00,0xff,0x00]
    # color_list += [0x00,0xff,0xff]
    # color_list += [0x00,0x00,0xff]
    # color_list += [0xff,0x00,0xff]

    while True:
      matrix.i2c.writeList(color_list[0],color_list[1:]) 
      # matrix.i2c.writeList(0xff,[0x00,0x00])
      # matrix.i2c.writeList(0x00,[0xff,0x00])
      # time.sleep(0.01)

  def endless_ascending(self):
    print 'endless ascending values...'
    color=0x000000
    while True:
      red = (color & 0x0000FF)
      green = (color & 0x00FF00) >> 8
      blue = (color & 0xFF0000) >> 16
      matrix.i2c.writeList(red,[green,blue])
      color+=1

  def mario_standing(self):
    pixels = self._pixel_list('./SuperMarioStanding_02.png')
    for pixel in pixels:
      self.i2c.writeList(pixel[0],list(pixel[1:]))

  def mario_walking(self):
    pixels_step1 = self._pixel_list('./SuperMario_step1.png')
    pixels_step2 = self._pixel_list('./SuperMario_step2.png')
    pixels_step3 = self._pixel_list('./SuperMario_step3.png')

    while True:
      for pixel in pixels_step1:
        self.i2c.writeList(pixel[0],list(pixel[1:]))
      # time.sleep(0.1)
      for pixel in pixels_step2:
        self.i2c.writeList(pixel[0],list(pixel[1:]))
      # time.sleep(0.1)
      for pixel in pixels_step3:
        self.i2c.writeList(pixel[0],list(pixel[1:]))
      # time.sleep(0.1)

  def _pixel_list(self, pic):
    # pixelsWide = 32
    # pixelsTall = 16

    im = Image.open(pic)
    im = im.rotate(180)
    #todo: check size. resize if necessary?
    rgb_im = im.convert('RGB')
    print 'size of picture:', rgb_im.size
    pixels = list(rgb_im.getdata())
    return pixels

if __name__ == '__main__':

  # matrix = MATRIX(0x55, debug=True)
  matrix = MATRIX()
  # matrix.endless_random()
  # matrix.endless_solid()
  # matrix.endless_ascending()
  matrix.mario_standing()
  # matrix.mario_walking()
  # matrix.i2c.writeList(0x00, [0xFF,0x00])
  # while True:
    # rand_list = [random.randint(0,255) for i in range(33)]
    # rand_list = [0xff,0xff,0xff]
    # rand_list = [0xff,0xff,0xff]
    # rand_list = [0x00,0xff,0xff]
    # rand_list = [0x00,0xff]
    # matrix.i2c.writeList(rand_list[0],rand_list[1:]) 
  # matrix.i2c.writeList(0x00, 
                       # [0xfe, 0xfe, 0xfe, 0xfe, 0xfe]+
                       # [0x00,0xfe, 0xfe, 0xfe, 0xfe, 0xfe]*4)
  # matrix.i2c.writeList(0x01,[0x01])
  # matrix.i2c.writeList(0x00,[0xff,0x00])
