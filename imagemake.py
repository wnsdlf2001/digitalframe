import os
from PIL import Image, ImageFilter, ImageEnhance
from imageio import imread, mimsave, imsave
images = []

# Recursively list image files and store them in a variable
'''
path = "Apps/images/"
os.chdir(path)
imgFiles = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
'''
def image2gif(imgFiles, frame):
    for filename in imgFiles:
        images.append(imread(filename))
    mimsave('/home/pi/Downloads/Apps/gifimages/movie.gif', images, fps = frame)


def imageblur(imgFiles):
    for filename in imgFiles:
        img = Image.open(filename)
        bleeding2 = img.filter(ImageFilter.GaussianBlur(radius=5))
        bleeding2= ImageEnhance.Color(bleeding2)
        bleeding2=bleeding2.enhance(0.3)
        bleeding2.save('/home/pi/Downloads/Apps/blured1/'+filename[0:-4]+'_blured2.jpg')
        bleeding3 = img.filter(ImageFilter.GaussianBlur(radius=10))
        bleeding3= ImageEnhance.Color(bleeding3)
        bleeding3=bleeding3.enhance(0.2)
        bleeding3.save('/home/pi/Downloads/Apps/blured2/'+filename[0:-4]+'_blured3.jpg')
        bleeding4 = img.filter(ImageFilter.GaussianBlur(radius=15))
        bleeding4= ImageEnhance.Color(bleeding4)
        bleeding4=bleeding4.enhance(0.1)
        bleeding4.save('/home/pi/Downloads/Apps/blured3/'+filename[0:-4]+'_blured4.jpg')
    
def imageresize(imgFiles, sizevert, sizehori):
    i = 0
    size = (sizevert, sizehori)
    for filename in imgFiles:
        outfile = imgFiles[i]
        im = Image.open(outfile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile)
        i += 1
