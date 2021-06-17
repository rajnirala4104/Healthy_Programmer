import its_functons as itFunc
from time import time

init_water = time()
init_Eyes = time()
init_Exercise = time()
waterSec = 30*60
eyeSec = 40*60
exerSec = 50*60
while True:
    if time()-init_water>waterSec:
        print("Its time to dink water, Enter 'drank' to stop the alarm")
        itFunc.song_for_work("sabariya_song.mp3","drank")
        init_water = time()
        itFunc.setFile("yourFile","I've Drank water")
    elif time()-init_Eyes>eyeSec:
        print("Its time to do eyes exercise, Enter 'eyDone' to stop the alarm")
        itFunc.song_for_work("agar_Tum.mp3","eyDone")
        init_Eyes = time()
        itFunc.setFile("yourFile","I've done eyes exercise")
    if time()-init_Exercise>exerSec:
        print("Its time to do physical activity like you can do dance, jump like monkey, and become mad. Enter 'exDone' to stop the alarm")
        itFunc.song_for_work("matargasti.mp3","exDone")
        init_Exercise = time()
        itFunc.setFile("yourFile","I've done physical Activity")
    

