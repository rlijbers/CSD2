import simpleaudio as sa
import time as tm
sampleSel = input("Which sample? ")
repAmt = int(input("How many times? "))
repInt = float(input("At what interval? "))

def repeat(play, sampleSel, repAmt, repInt):
    for i in range(repAmt):
        play(sampleSel)
        tm.sleep(repInt)

def play(sample):
    wave_obj = sa.WaveObject.from_wave_file(sample)
    play_obj = wave_obj.play()

repeat(play, sampleSel, repAmt, repInt)
