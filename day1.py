import math
input = open("day1in.txt").read().splitlines()

pos = 50
p2pw = 0

def countup(num):
    global pos
    global p2pw
    while num > 0:
        pos += 1
        num -= 1
        if pos > 99:
            pos = 0
        # print(pos)

def countdown(num):
    global pos
    global p2pw
    num = abs(num)
    while num > 0:
        pos -= 1
        num -= 1
        if pos < 0:
            pos = 99
        # print(pos)

pw = 0

# countdown(int(input[0][1:]))

for i in range(len(input)):
    print(input[i])
    if input[i][0] == "R":
        countup(int(input[i][1:]))
    elif input[i][0] == "L":
        countdown(int(input[i][1:]))
    if pos == 0:
        pw += 1
    print(pos)

print(pw)
print("Part 2:" + str(p2pw))
