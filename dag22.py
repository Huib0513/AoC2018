#!python3

test = 0

if test:
    targetx = 10
    targety = 10
    depth = 510
else:
    targetx = 9
    targety = 731
    depth = 11109

def erosionlevel(index, depth):
    return (index + depth) % 20183

grid = []
for y in range(0,targety+1):
    grid.append([])
    #print(grid)
    for x in range(0,targetx+1):
        if y == 0:
            if x == 0:
                grid[y].append(erosionlevel(0, depth))
            else:
                grid[y].append(erosionlevel(x*16807, depth))
        else:
            if x == 0:
                grid[y].append(erosionlevel(y*48271, depth))
            elif (y == targety) and (x == targetx):
                grid[y].append(erosionlevel(0, depth))
            else:
                xje = grid[y][x-1]
                yje = grid[y-1][x]
                grid[y].append(erosionlevel(xje*yje, depth))

dangersum = 0
for y in range(0,targety+1):
    for x in range(0, targetx+1):
        dangersum += grid[y][x] % 3


print(dangersum)
