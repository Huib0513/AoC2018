#!python3

from collections import namedtuple

#lines = open('testinput.dag23').read().splitlines()
lines = open('input.dag23').read().splitlines()

Coordinates = namedtuple('Coordinates', 'x y z')
nanobots = []

def distance(bot1, bot2):
    return abs(bot1.x - bot2.x) + abs(bot1.y - bot2.y) + abs(bot1.z - bot2.z)

for line in lines:
    words = line.split(',')
    print(words[0][5:], words[1], words[2][:-1], words[3][3:])
    nanobots.append([Coordinates(int(words[0][5:]), int(words[1]), int(words[2][:-1])), int(words[3][3:])])
    #print(nanobots)

maxrange = maxbot = 0
for bot in range(len(nanobots)):
    if nanobots[bot][1] > maxrange:
        maxrange = nanobots[bot][1]
        maxbot = bot

print(maxbot, nanobots[maxbot])

aantal = 0
for bot in nanobots:
    afstand = distance(nanobots[maxbot][0], bot[0])
    print(afstand, nanobots[maxbot][0], bot[0])
    if afstand <= maxrange:
        aantal += 1

print(aantal)
