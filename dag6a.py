#!python3
from collections import defaultdict, namedtuple

Point = namedtuple('Point', 'x y')
punten = defaultdict(Point)
dist = defaultdict(int)

# Main loop
maxx = 0
maxy = 0
regels = list(open('input.dag6').read().splitlines())

for punt in regels:
    x = int(punt.split(', ')[0])
    y = int(punt.split(', ')[1])
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y
    punten[x,y] = Point(x, y)

for i in range(maxx):
    for j in range(maxy):
        d = {}
        for x, y in punten:
            d[x,y] = abs(x - i) + abs(y - j)
        for x,y in d:
            print(d)




#for locatie in regels:
#    toreplace = letter.lower() + "|" + letter.upper()
#    solution = krimp(re.sub(toreplace, "", regels[0]))
#    print(toreplace + ": " + str(len(solution)))
