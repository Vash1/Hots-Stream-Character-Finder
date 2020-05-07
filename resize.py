import os.path
from PIL import Image

inputfolder = './img_fullres/'
#outputfolder = './img_720p/'
path, dirs, files = os.walk('./img_fullres').__next__()

files.sort()
size = 1280, 720

#outputfolder = './img_360/'
#size = 640, 360

for filename in files:
    img = Image.open(inputfolder+filename)
    img.thumbnail(size)
    img.save(filename)

    
    print('./img_fullres/'+filename)
