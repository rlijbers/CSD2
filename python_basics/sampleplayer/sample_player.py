import time as tm
import simpleaudio as sa
# numPlayBackTimes
# BPM
def play(sample):
    wave_obj = sa.WaveObject.from_wave_file(sample)
    play_obj = wave_obj.play()
    play_obj.wait_done()

sampleSel = input("Which sample?  ")
#playAmt = input("How many times?  ")
#playInt = input("At which time BPM?  ")

play(sampleSel)

