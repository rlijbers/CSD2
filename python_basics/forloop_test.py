import time as tm
repAmt = int(input("How many times? "))
repInt = int(input("At which interval? "))
def repeat(f, repAmt, repInt):
    for i in range(repAmt):
        f()
        tm.sleep(repInt)
def f():
    print ("test!")
repeat(f, repAmt, repInt)
