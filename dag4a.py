#!python3
from collections import defaultdict

#lines = open("testinput.dag4").read().splitlines()
lines = open("input.dag4").read().splitlines()
lines.sort()

print(lines)

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

maxminute = maxguard = 0
for guard in slaapjes:
    if len(slaapjes[guard]) > maxminute:
        maxguard = guard
        maxminute = len(slaapjes[guard])

maxcount = maxminute = 0
for minute in set(slaapjes[maxguard]):
    if slaapjes[maxguard].count(minute) > maxcount:
        maxcount = slaapjes[maxguard].count(minute)
        maxminute = minute

print(str(int(maxguard) * int(maxminute)))
