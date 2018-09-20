#module imports
import time as tm
import simpleaudio as sa
import sys

#example command
# python3 rhythm_player.py 4 1 0.5 1.5 0.5 120

#input/argument data
noteArr = (sys.argv[2: len(sys.argv)-1])
stepAmt = len(noteArr)
BPM = sys.argv[len(sys.argv)-1]

#prompts for sample select, use only 16 bit files!
sampleSel = input("Which sample? ")
loopAmt = (sys.argv[1])

#BPM calculation
def bpmCalc(BPM, note):
    return (60./int(BPM))*note

#play function
def playSample(sample):
    wave_obj = sa.WaveObject.from_wave_file(sample)
    play_obj = wave_obj.play()

#play loop
for loopStat in range(0, int(loopAmt)):
    for note in noteArr:
        playSample(sampleSel)
        tm.sleep(bpmCalc(BPM, float(note)))


#test prints
#print(bpmCalc(BPM, float(note)))
#print(note)
#print(range(0, (int(loopAmt)+1))
#print(loopAmt, stepAmt, noteArr, BPM)
