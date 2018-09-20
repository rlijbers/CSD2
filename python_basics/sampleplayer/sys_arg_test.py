import sys
import time as tm

printTest = sys.argv[1]
noteArr = sys.argv[2: len(sys.argv)-2]
BPM = sys.argv[len(sys.argv)-1]
print(printTest)
print(noteArr)
print(BPM)
for note in noteArr:
    print(float(note))
