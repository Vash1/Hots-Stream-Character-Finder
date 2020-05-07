frame = None

def getNames(): 
    l = (
"abathur",
"alarak",
"alexstrasza",
"ana",
"Anub'arak",
"artanis",
"arthas",
"auriel",
"azmodan",
"brightwing",
            
"The butcher",
"cassia",
"chen",
"cho",
"gall",
"chromie",
"dehaka",
"diablo",
"d.va",
"e.t.c",
            
"falstad",
"garrosh",
"hanzo",
"gazlowe",
"genji",
"greymane",
"gul'dan",
"illidan",
"jaina",
"johanna",
            
"kael'thas",
"junkrat",
"kel'thuzad",
"kerrigan",
"kharazim",
"leoric",
"li li",
"Li-ming",
"the lost vikings",
"Lúcio",
            
"lunara",
"Lt. Morales",
"malfurion",
"malthael",
"medivh",
"muradin",
"murky",
"nazeebo",
"nova",
"probius",
            
"ragnaros",
"raynor",
"rehgar",
"rexxar",
"samuro",
"Sgt. Hammer",
"sonya",
"stitches",
"stukov",
"sylvanas",
            
"tassadar",
"thrall",
"tracer",
"tychus",
"tyrael",
"tyrande",
"uther",
"valeera",
"valla",
"varian",
            
"xul",
"zagara",
"zarya",
"zeratul",
"zul'jin",
"blaze"
)
    l = [el.upper() for el in l]
    return l

'''

load frame
find 10 avatars-position, depending on match type spectator vs playing
compare 10 pictures with avatar sheet and return names
depending on match type:
    spectator - find 0-7 talents at positions
    player - detect tab window
        find 0-7 talent choices
    by using a talent sheet that each character has


'''

from subprocess import Popen, PIPE
import numpy as np
import cv2

width = 640
height = 360

p1 = Popen(["streamlink", "https://www.twitch.tv/glogan13", "360p", "-O"], stdout=PIPE)
p2 = Popen(["ffmpeg",
           "-i", "pipe:0",
           "-filter:v", "fps=2",
           "-loglevel", "quiet",
           "-an",
           "-f", "image2pipe",
           "-pix_fmt", "bgr24",
           # "-pix_fmt", "GRAY8",
           "-vcodec", "rawvideo", "-"],
           stdin = p1.stdout, stdout=PIPE)
#p2 = Popen(["ffmpeg", "-i", "pipe:0", "-f", "rawvideo", "-filter:v", "fps=0.5", "-qscale:v", "1", "-f", "image2pipe", "-"], stdin=p1.stdout, stdout=PIPE, bufsize=10**8)

def getFrame(process):
    raw_image = process.stdout.read(width * height * 3)
    return np.frombuffer(raw_image, dtype=np.uint8).reshape((height, width, 3))
    # raw_image = process.stdout.read(width * height * 1)
    # return np.frombuffer(raw_image, dtype=np.uint8).reshape((height, width, 1))

def bInMatch():
#crop 'versus' from image. its at upper center.
#almost no dynamic background at this position, should work fine
    #textVS = frame[25:25+9, 620:635+11]
    #textVS = frame
    #textVS = frame[25:25+9, 635:635+11]
#check 12x9 pixel from full frame with the template. should almost be equal
    #result = cv2.matchTemplate(vsTemplate, textVS, cv2.TM_CCOEFF_NORMED)
    #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #print(min_val, max_val, " at: ", max_loc)
    #if max_val > 0.88:
    return True
    #return False


full = cv2.imread('smallHeroes.jpg')
# full = cv2.cvtColor(full, cv2.COLOR_BGR2GRAY)
vsTemplate = cv2.imread('ismatchTemplate.png')

ax1, ay1 = [132,2] #at 360p the corner of the most left portrait. first corner
ax2, ay2 = [155,12] #"size" of the bounding box
bx1, by1 = [161,2]
bx2, by2 = [184,12]

zx1 = 367

diffx, diffy = [bx1 - ax1, by1 - ay1]
sizex, sizey = [ax2 - ax1, by2 - by1]
Lcoords=[ (ax1+diffx*i + round(i*2/10), ay1+diffy*i) for i in range(5)]
Rcoords=[ (zx1+diffx*i + round(i*2/10), ay1+diffy*i) for i in range(5)]
h=(sizex, sizey)
Lcoords.reverse()

def positionIn(searchString):
    return folderCompare.index(searchString.upper())

#in the full vertical image, get the position of matching getNames/upperNames
#should return up to 10 results if a match is ongoing
#may not detect portraits with a timer on them (waiting to respawn)

def cv2FindAvatar(i):
    result = cv2.matchTemplate(lAvatar[i], full, cv2.TM_CCOEFF_NORMED)
    #match.append(np.where(result >= thresh))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    matchLoc.append(max_loc)
    matchMax.append(max_val)
    result = cv2.matchTemplate(rAvatar[i], full, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    matchLoc.append(max_loc)
    matchMax.append(max_val)

def getPlayerName():
    for y in matchLoc:
        index = positionIn(upperNames[int(y[1]/10)])
        playingCharacters.append(folderNames[index])
    

upperNames = getNames() 
import os

folderNames = os.listdir("../imgetter.python/scripts/imFolder")
folderCompare = [el.upper() for el in folderNames]

for el in upperNames:
    if folderCompare.count(el) < 1:
        print('not equal:', el)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', full)
'''not in match vs in a match'''
#get frames
#if bInMatch is true 5x in a row, set match true

#match:
#get frames obviously
#if bInMatch is false 5x in a row, set match false

matchLoc = None
matchMax = None
playingCharacters = []

from collections import deque
isMatch = deque([False]*7, maxlen=7)

while True:
    frame = getFrame(p2)

    isMatch.append(bInMatch())
    cv2.imshow("imgs", frame)
    cv2.waitKey(400)

    if isMatch.count(True) > 5:
        matchLoc = []
        matchMax = []

        lAvatar = []
        for a, b in Lcoords:
            lAvatar.append(frame[b:b+h[1], a:a+h[0]])

        rAvatar = []
        for a, b in Rcoords:
            rAvatar.append(frame[b:b+h[1], a:a+h[0]])

        for i in range(5):
            cv2FindAvatar(i)

        #print(matchLoc)
        playingCharacters.clear()
        getPlayerName()
        os.system('clear')
        print("Left Team:", playingCharacters[0:len(playingCharacters):2])
        print("Right Team:", playingCharacters[1:len(playingCharacters):2])



    elif isMatch.count(True)  == 4:
        print("count is 4")
        continue
    elif isMatch.count(True) < 4:
        print("match not found")
        continue
