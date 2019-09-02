import update_img
import time
import RPi.GPIO as GPIO
import os, sys
import constant
from PIL import Image, ImageFilter
from imageio import imread, mimsave, imsave
from imagemake import *

while(True):
    path = "/home/pi/Downloads/"
    os.chdir(path)
    print('**** Image downloading...****')
    update_img.pic()
    
    print('**** Image processing...****')
    path = "/home/pi/Downloads/Apps/images"
    os.chdir(path)
    imgFiles = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpeg')))
    imageresize(imgFiles, 1024, 512)
    imageblur(imgFiles)
