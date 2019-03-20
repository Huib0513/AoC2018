#!python3

def printje(lines):
    for line in lines:
        print(str(line))

def bepaalomgeving(x, y, lines):
    minkol = max(0, x-1)
    minrow = max(0, y-1)
    maxkol = min(len(lines[0])-1, x+1)
    maxrow = min(len(lines)-1, y+1)
    open = trees = lumber = 0

    for row in range(minrow, maxrow+1):
        for kol in range(minkol, maxkol+1):
            #print('Checking ('+str(kol)+', '+str(row)+')')
            if (row == y) and (kol == x):
                continue
            if lines[row][kol] == '.':
                open += 1
            elif lines[row][kol] == '|':
                trees += 1
            else:
                lumber +=1
    #print('Around ('+str(x)+', '+str(y)+'): '+str(open)+', '+str(trees)+', '+str(lumber))
    return open, trees, lumber

#part 1: maxminuten = 10
maxminuten = 1000000000
grid = []
grid.append([])
#grid[0] = open('testinput.dag18').read().splitlines()
grid[0] = open('input.dag18').read().splitlines()

print("Initial state:")
printje(grid[0])

for minuut in range(1, maxminuten+1):
    grid.append([])
    #minuut = 1
    current = grid[minuut-1]

    for line in range(len(current)):
        newline = []
        for teken in range(len(current[line])):
            open, trees, lumber = bepaalomgeving(teken, line, current)
            if current[line][teken] == '.':
                # open with >= 3 trees --> tree
                if trees>=3:
                    newline.append('|')
                else:
                    newline.append(current[line][teken])
            elif current[line][teken] == '|':
                # tree with >= 3 lumber --> lumber
                if lumber>=3:
                    newline.append('#')
                else:
                    newline.append(current[line][teken])
            else:
                if lumber and trees:
                    # lumber with >= 1 lumber and >=1 tree --> lumber
                    newline.append('#')
                else:
                    # else --> open
                    newline.append('.')
        grid[minuut].append(''.join(newline))

    #print('Na ' + str(minuut) + ' minuten:')
    #printje(grid[minuut])

trees = lumber = 0
for line in grid[maxminuten]:
    for teken in line:
        if teken == '|':
            trees += 1
        elif teken == '#':
            lumber += 1

print('Eindresultaat: ' + str(trees * lumber))
