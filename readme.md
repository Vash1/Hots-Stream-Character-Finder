Disclaimer: This was a learning project from 2017. I decided to upload it, it might help someone.
The files/classes/methods are not cleand up, as this was a prototype to test performance and server-load. My next iteration was in work by that time 
I would have loved to continue the project and implement it with a proper Web/UI client but the publisher cancelled all tournaments (and most of the development) for the game (Heroes of the Storm) 
 

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
