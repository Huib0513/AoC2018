#!python3

from collections import defaultdict

doek = defaultdict(int)

for line in open("input.dag3"):
    woorden = line.split()
    x, y = woorden[2].split(',')
    x = int(x)
    y= int(y[:-1])
    breedte, hoogte = woorden[3].split('x')
    breedte = int(breedte)
    hoogte = int(hoogte)

    for rij in range(x, x+breedte):
        for kolom in range(y, y+hoogte):
            doek[(rij, kolom)] += 1    

dubbelen = 0
for rij, kolom in doek:
    if doek[(rij, kolom)] > 1:
        dubbelen += 1

print(dubbelen)

