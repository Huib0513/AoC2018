#!python3
from collections import deque

#aantalelfen = 9
#maximummarble = 25
#aantalelfen = 10
#maximummarble = 1618
#aantalelfen = 13
#maximummarble = 7999
#aantalelfen = 17
#maximummarble = 1104
#aantalelfen = 21
#maximummarble = 6111
#aantalelfen = 30
#maximummarble = 5807

# Deel 1
aantalelfen = 466
maximummarble = 71436

# Deel 2
aantalelfen = 466
maximummarble = 7143600


elfscore = {}
currentelf = deque([x for x in range(1, aantalelfen+1)])
for x in range(1, aantalelfen+1):
    elfscore[x] = 0

# initialize deque to prevent edge cases
cirkel = deque([x for x in (2, 1, 0)])
currentelf.rotate(-2)

def addmarble(cirkel, value):
    cirkel.rotate(-2)
    cirkel.extendleft(value)

def removemarble(cirkel):
    cirkel.rotate(7)
    return cirkel.popleft()

print(cirkel, elfscore, currentelf)

for marble in range(3, maximummarble):
    if marble%23:
        addmarble(cirkel, [marble])
    else:
        elfscore[currentelf[0]] += removemarble(cirkel)
        elfscore[currentelf[0]] += marble
        #print("Removed marble "+ str(elfscore[currentelf[0]]-marble) + " for elf " + str(currentelf[0]))

    currentelf.rotate(-1)

print(elfscore)
max = maxelf = 0
for elf in range(1, len(elfscore)+1):
    if elfscore[elf] > max:
        max = elfscore[elf]
        maxelf = elf

print("winnende elf is " + str(maxelf) + " met " + str(max) + " punten")
