#!python3

from collections import defaultdict
first = defaultdict(list)
todo = defaultdict(list)

#regels = open("testinput.dag7").readlines()
regels = open("input.dag7").readlines()

for line in regels:
    woorden = line.split(' ')
    first[woorden[7]].append(woorden[1])

todo = first.copy()
print(todo, first)

# Requirements zoeken die zelf nergens op wachten
for l in first.values():
    for r in l:
        if not r in first:
            todo[r] = []
            print("gevonden: "+ r)

solution = ""
while len(todo.keys()) > 0:
    # Eerstvolgende requirement zoeken
    for k in sorted(todo.keys()):
        print(todo[k])
        if len(todo[k]) == 0:
            current_step = k
            solution = solution + k
            todo.pop(k)
            print(current_step, solution)
            break

    # Requirement uit todo halen en uit alle lijstjes
    for k, l in todo.items():
        l = [x for x in l if x != current_step]
        todo[k] = l

    print(todo)

