import os.path
from operator import itemgetter
from PIL import Image

import time

folder = './img_360/'
#folder = './img_720/'
path, dirs, files = os.walk(folder).__next__()

files = sorted(files, key=lambda i: int(os.path.splitext(os.path.basename(i))[0]))
i=0

#coordinates:
#360
ax1, ay1 = [132,2] #at 360p the corner of the most left portrait. first corner
ax2, ay2 = [155,12] #"size" of the bounding box
bx1, by1 = [161,2]
bx2, by2 = [184,12]

zx1 = 367

diffx, diffy = [bx1 - ax1, by1 - ay1]
sizex, sizey = [ax2 - ax1, by2 - by1]
Lcoords=[ (ax1+diffx*i + round(i*2/10), ay1+diffy*i) for i in range(5)]
Rcoords=[ (zx1+diffx*i + round(i*2/10), ay1+diffy*i) for i in range(5)]
height=(sizex, sizey)

Lcoords.reverse()

for filename in files:
    img = Image.open(folder+filename)
    for a, b in zip(Lcoords,Rcoords):
        areaL = (a[0],a[1],a[0]+sizex,a[1]+sizey)
        Limg = img.crop(areaL)
        Limg.save("./avatars360p/"+str(i)+"_blue.png")
        areaR = (b[0],b[1],b[0]+sizex,b[1]+sizey)
        Rimg = img.crop(areaR)
        Rimg.save("./avatars360p/"+str(i)+"_red.png")
        i+=1

        print("working on:"+filename)


'''
#720
#Lcoords=[(263,308),(322,367),(381,426),(440,485),(499,544)]
#Rcoords=[(735,780),(794,839),(853,898),(912,957),(971,1016)]
#height=(6,20)

Lcoords.reverse()

for filename in files:
    img = Image.open(folder+filename)
    for a, b in zip(Lcoords,Rcoords):
        areaL = (a[0],height[0],a[1],height[1])
        Limg = img.crop(areaL)
        Limg.save("./avatars/"+str(i)+"_blue.png")
        areaR = (b[0],height[0],b[1],height[1])
        Rimg = img.crop(areaR)
        Rimg.save("./avatars/"+str(i)+"_red.png")
        i+=1

        print("working on:"+filename)
        #print((avatar[0],height[0],avatar[1],height[1]))
'''