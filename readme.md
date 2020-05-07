Disclaimer: This was a learning project from 2017. I decided to upload it, it might help someone. Developed on Linux.
 

## Installing
Clone the repository and create and start a python virtual environment 
Install the requirements.txt (opencv, numpy, ffmpeg, streamlink) 
run it with "python 360match.py"

Im not sure about windows but you will need to also install ffmpeg


## How it works
- frame: reads the stream by piping it and converting it to numbers
- reference: converts a reference image to numbers, there is a script to create it
- opencv compares 10 specific areas in the frame to the reference
- the result (divided by the height of the avatar) is a line number, and that converts to a name from the list

After some tuning, the reference got only 14 kb in size and it works absolutley good.