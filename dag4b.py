#!python3
from collections import defaultdict

#lines = open("testinput.dag4").read().splitlines()
lines = open("input.dag4").read().splitlines()
lines.sort()

#print(lines)

slaapjes = defaultdict(list)
startminuut = 0

for line in lines:
    words = line.split(' ')
    minute = int(words[1].split(':')[1][0:2])

    if words[2] == 'Guard':
        currentguard = words[3][1:]
        #print(line, currentguard)
    elif words[2] == 'falls':
        startminuut = minute
        #print(line, str(startminuut))
    else:
        for x in range(startminuut, minute):
            slaapjes[currentguard].append(x)
        #print(slaapjes)

guardminutes = defaultdict(int)
maxguard = totalmax = maxminute = 0
for guard in slaapjes.keys():
    maxcount = 0
    for minute in set(slaapjes[guard]):
        if slaapjes[guard].count(minute) > maxcount:
            maxcount = slaapjes[guard].count(minute)
            guardminutes[guard] = minute
            if maxcount > totalmax:
                maxguard = guard
                maxminute = minute
                totalmax = maxcount

#print(guardminutes)
print(maxguard, maxminute, str(int(maxguard)*int(maxminute)))
#print(str(maxguard), str(guardminutes[maxguard]))
