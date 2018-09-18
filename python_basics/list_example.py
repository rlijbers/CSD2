import time

values = [0.5, 0.25, 0.5, 2, 1]
numValues = 5
numValues = len(values)

print("forloop 1")
for index, value in enumerate(values):
    print(index, value)

print("forloop 2")
for index in range(len(values)):
    print(index)
    print(values[index])

print("forloop 3")
for value in values:
    print(value)
    for val2 in values:
        print(val2)
        if val2 == 0.25:
            break
print("end")
