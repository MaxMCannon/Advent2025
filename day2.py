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
matchs = []

def checknum(num):
    # print(num)
    global matchs
    for l in range(1, int(len(str(num))/2)+1):
        arr = [str(num)[:l]]
        # print(l)
        # print(arr)
        for i in range(l, len(str(num))+1, l):
            piece = str(num)[i:i+l]
            if piece != arr[-1]:
                break
            arr.append(piece)
            # print(arr)
        if l * len(arr) == len(str(num)) and len(arr) >= 2:
            matchs.append(num)
            print(arr)
        # if getarrlen(arr) == len(str(num)):
        #     return num
            # print("got one")
        # else:
        #     return 0

# checknum(21212121)

print(set(matchs))

p2sum = 0

for l in input:
    ids = [int(l.split('-')[0]), int(l.split('-')[1])]
    for i in range(ids[0], ids[1]+1):
        checknum(i)
    # print(ids)

print(set(matchs))

for item in set(matchs):
    p2sum += item

print(p2sum)

# checknum(123123)
        


