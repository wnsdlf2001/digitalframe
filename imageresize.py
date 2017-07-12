import os, sys
from PIL import Image
from imageio import imread, mimsave, imsave
i = 0
size =(128, 128)
images =[]
path = "E:/images/"
os.chdir(path)
imgFiles = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))

for filename in imgFiles:
    outfile = imgFiles[i]
    im = Image.open(outfile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile)
    i+=1
