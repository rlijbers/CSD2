import time as tm
import simpleaudio as sa
intervalArr = [4, 1, 0.5, 1.5, 0.5,]
loopAmt = int(input("How many times? ")
for x in range(0, loopAmt):
    for i in intervalArr:
        print (i)
        tm.sleep(i)

