import math
input = open("day1in.txt").read().splitlines()

pos = 50
pw = 0
p2pw = 0

def countup(num):
    global pos
    global p2pw
    while num > 0:
        pos += 1
        num -= 1
        if pos > 99:
            p2pw += 1
            pos = 0
        # elif pos == 0:
        #     p2pw += 1
        # print(pos)

def countdown(num):
    global pos
    global p2pw
    num = abs(num)
    while num > 0:
        pos -= 1
        num -= 1
        if pos < 0:
            # p2pw += 1
            pos = 99
        elif pos == 0:
            p2pw += 1
        # print(pos)

for i in range(len(input)):
    # print(input[i])
    if input[i][0] == "R":
        countup(int(input[i][1:]))
    elif input[i][0] == "L":
        countdown(int(input[i][1:]))
    if pos == 0:
        pw += 1
    # print(pos)

print("Part 1: " + str(pw))
print("Part 2: " + str(p2pw))
