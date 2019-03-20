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

for line in open("input.dag3"):
    woorden = line.split()
    x, y = woorden[2].split(',')
    x = int(x)
    y= int(y[:-1])
    breedte, hoogte = woorden[3].split('x')
    breedte = int(breedte)
    hoogte = int(hoogte)

    uniek = 1
    for rij in range(x, x+breedte):
        for kolom in range(y, y+hoogte):
            if doek[(rij, kolom)] > 1:
                uniek = 0
    if uniek == 1:
        print(woorden)

