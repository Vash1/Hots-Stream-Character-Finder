from subprocess import Popen, PIPE
import numpy as np



silentLevel = (
    'quiet'  ,
    'panic'  ,
    'fatal'  ,
    'error'  ,
    'warning',
    'info'   ,
    'verbose',
    'debug'  )

#'p1'
class VideoStream:
    #-holds ffmpeg and streamlink locations and settings
    #-starts matchtrackers because each link will hold a unique frame

    def __init__(self, twitchUsr, res='720p',
        fps=2, loglevel='quiet', number=0):
        
        #p1
        self.twitchURL = 'https://www.twitch.tv/'+twitchUsr
        self.res = res
        self.stdOUT = '-O'
        
        #p2
        self.fps = str(fps)
        self.loglevel = loglevel

        if number is -1:
            self.width = 640
            self.height = 360
        else:
            self.width = 1280
            self.height = 720

        self.number = number

        if number >= 0:
            self.p3info = VideoStream(twitchUsr, res="360p", loglevel=silentLevel[0], number=-1)
    def startListening(self):
        #self.p1 = Popen(["streamlink", self.twitchURL, self.res, "-O"], stdout=PIPE)
        #self.p2 = Popen(["ffmpeg",
        '''    "-i", "pipe:0",
            "-filter:v", "fps="+self.fps,
            "-loglevel", self.loglevel,
            "-an",
            "-f", "image2pipe",
            "-pix_fmt", "bgr24",
            "-vcodec", "rawvideo", "-"],
            bufsize=1,
            stdin = self.p1.stdout, stdout=PIPE)'''

    def startP3(self):
        print(self.p3info.width)
        self.p3info.p1 = Popen(["streamlink", self.p3info.twitchURL, self.p3info.res, "-O"], stdout=PIPE)
        self.p3info.p2 = Popen(["ffmpeg",
            "-i", "pipe:0",
            "-filter:v", "fps="+self.p3info.fps,
            "-loglevel", self.p3info.loglevel,
            "-an",
            "-f", "image2pipe",
            "-pix_fmt", "GRAY8",
            "-vcodec", "rawvideo", "-"],
            stdin = self.p3info.p1.stdout, stdout=PIPE)

    def getFrame(self):
        raw_image = self.p2.stdout.read(self.width * self.height//16*1 * 3)
        self.p2.stdout.read(self.width * self.height//16*15 * 3)
        return np.frombuffer(raw_image, dtype=np.uint8).reshape((self.height//16*1, self.width, 3))

    def getFrame2(self):
        raw_image = self.p3info.p2.stdout.read(self.p3info.width * self.p3info.height * 1)
        #self.p2.stdout.read(self.p3info.width * self.p3info.height * 3)
        return np.frombuffer(raw_image, dtype=np.uint8).reshape((self.p3info.height, self.p3info.width, 1))

    def __repr__(self):
        return "<.VideoStream object - URL:'%s' Resolution:'%s'\n -VideoStream object - LogLevel:'%s'>" % (self.twitchURL, self.res, self.loglevel)


#each instance of streamlink/ffmpeg
'''
is also using a matchtracker object. altho it can use two instances or more
most of them should be on sleep.
need to save references to those matchtrackers somewhere
'''
class MatchTracker():
    pass

instances = []

for i in range(1):
    VideoInstance = VideoStream('bobross', loglevel=silentLevel[0], number=i)
    VideoInstance.startListening()
    VideoInstance.startP3()
    instances.append(VideoInstance)

import time

start = 0
end = time.time()
counter = 0
average = 0

from collections import deque
isMatch = deque([0.0]*30, maxlen=30)

import cv2

while True:
    for vstream in instances:
        #frame = vstream.getFrame()
        frame2 = vstream.getFrame2()

        if vstream.number == 0:
            #cv2.imshow("frame", frame)
            cv2.imshow("frame lowres", frame2)
            cv2.waitKey(1)
            

            start= end
            end = time.time()
            #average = average + end - start

            isMatch.append(end-start)

            avrg = 0
            for el in isMatch:
                avrg += el
            print(avrg/30)




#print(VideoInstance)


'''
width = 1280
height = 720
p1 = Popen(["streamlink", "http://twitch.tv/mewnfare", "720p", "-O"], stdout=PIPE)
p2 = Popen(["ffmpeg",
           "-i", "pipe:0",
           "-filter:v", "fps=0.5",
           "-loglevel", "quiet",
           "-an",
           "-f", "image2pipe",
           "-pix_fmt", "bgr24",
           "-vcodec", "rawvideo", "-"],
           stdin = p1.stdout, stdout=PIPE)

def getFrame(process):
    raw_image = process.stdout.read(width * height * 3)
    return np.frombuffer(raw_image, dtype=np.uint8).reshape((height, width, 3))

while True:
    print("works")
    fullimg = getFrame(p2)
'''