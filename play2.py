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
    count = 0
    GPIO.setmode(GPIO.BCM)
    PIR_PIN = 7

    GPIO.setup(PIR_PIN, GPIO.IN)

    path = "/home/pi/Downloads/gifimages/"
    os.chdir(path)
    imgFiles = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
    images = []
    imageresize(imgFiles, 1024, 512)
    image2gif(imgFiles, 10)
    
    # kill a previous fbi process.
    os.system('sudo pkill gpicview')
    while count < 10:
        GPIO.output(27,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(27,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.05)
        count +=1
    # execute the fbi.
    #os.system('sudo fbi -a -T 2 -t 30 -noverbose `find /home/pi/Downloads/gifimages/ -iname "*.gif"`')
    os.system('sudo gpicview `find /home/pi/Downloads/gifimages/ -iname "*.gif"`')
    count = 0
    while count < 10:
        GPIO.output(27,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(27,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.05)
        count +=1  

       

