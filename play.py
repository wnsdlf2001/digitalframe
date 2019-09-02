# -*- coding: utf-8 -*-
"""play.py

This module's name is 'play'.
Please use this module for playing image files.
You must install the fbi(framebuffer imageviewer).
 - how to install fbi: apt-get install fbi

"""
import RPi.GPIO as GPIO
import time
import os, sys
import constant
from PIL import Image, ImageFilter
from imageio import imread, mimsave, imsave
from imagemake import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

# main function
if __name__ == "__main__":
    count =0
    GPIO.setmode(GPIO.BCM)
    PIR_PIN = 7

    GPIO.setup(PIR_PIN, GPIO.IN)

    # kill a previous fbi process.
    os.system('sudo pkill fbi')
    
    while count < 5:
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.25)
        count +=1

    os.system('sudo fbi -a -T 5 -t 5 -1 -noverbose `find /home/pi/Downloads/Apps/images/ -iname "*.jpg"`')
    time.sleep(5)
    os.system('sudo pkill fbi')
    os.system('sudo fbi -a -T 5 -t 5 -noverbose `find /home/pi/Downloads/Apps/blured1/ -iname "*.jpg"`')
    time.sleep(5)
    os.system('sudo pkill fbi')
    os.system('sudo fbi -a -T 5 -t 5 -noverbose `find /home/pi/Downloads/Apps/blured2/ -iname "*.jpg"`')
    time.sleep(5)
    os.system('sudo pkill fbi')
    
    while(True):
        if os.listdir('/home/pi/Downloads/Apps/Automatic Call Recorder/Records'):
            os.system('sudo fbi -a -T 5 -t 5 -1 -noverbose `find /home/pi/Downloads/Apps/images/ -iname "*.jpg"`')
            time.sleep(5)
            os.system('sudo pkill fbi')
        else:
            os.system('sudo fbi -a -T 5 -t 5 -1 -noverbose `find /home/pi/Downloads/Apps/blured3/ -iname "*.jpg"`')
            time.sleep(5) 
            os.system('sudo pkill fbi')
        
        
      #os.system('sudo gpicview `find /home/pi/Downloads/Apps/images/ -iname "*.jpg"`')
    
        
    
