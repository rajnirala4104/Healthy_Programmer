from pygame import mixer 
import time
mixer.init()

def song_for_work(Song_File,stopper):
    mixer.music.load(Song_File)
    mixer.music.play()
    while True:
        askStop =  input("Enter stop for stop the song: ")
        if askStop == stopper:
            mixer.music.stop()
        else:
            continue
        break

def setFile(fileName,what_Write):
    try:
        with open(fileName+".txt","x"):
            pass
    except:
        with open(fileName+".txt","a")as yourFile:
            yourFile.write(f"{what_Write} at -> {time.asctime()}\n")
        
def seTime(seconds):
    time.sleep(seconds)

if __name__=="__main__":
    song_for_work("hona_song.mp3","Drank")
