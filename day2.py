#Advent of Code - Day 2

input = open("day2in.txt").read().split(',')

def checkid(f, e):
    count = 0
    outarr = []
    for i in range(f, e + 1):
        if len(str(i))%2 == 0:
            p1 = str(i)[:int(len(str(i))/2)]
            p2 = str(i)[int(len(str(i))/2):]
            if p1 == p2:
                # print("Match found: " + str(i))
                outarr.append(i)
    return outarr

checkid(998, 1012)
globalsum = 0

for l in input:
    temp = []
    ids = [int(l.split('-')[0]), int(l.split('-')[1])]
    temp = checkid(ids[0], ids[1])
    for item in temp:
        globalsum += item
    temp = []
    # print(ids)

print("Part 1: " + str(globalsum))

#Start Part 2

def checkid2(f, e):
    for i in range(f, e + 1):
        for i in range(1, len(i//2)):
            pass
        if len(str(i))%2 == 0:
            p1 = str(i)[:int(len(str(i))/2)]
            p2 = str(i)[int(len(str(i))/2):]
            if p1 == p2:
                doubleflag = False
                for char in set(p1):
                    if p1.count(char) == 2:
                        doubleflag = True
                if doubleflag:
                    # print("Match found: " + str(i))
                    outarr.append(i)
