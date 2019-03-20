#!python3

maxrecepten=880751

recipes = [3, 7]
elfrecipes = [0, 1]

for teller in range(maxrecepten+10):
    som = 0
    for elf in elfrecipes:
        som += int(recipes[elf])
    recipes.extend([int(i) for i in str(som)])

#    print(recipes, elfrecipes)
    for elf in range(len(elfrecipes)):
        stap = recipes[elfrecipes[elf]] + 1
        newvalue = elfrecipes[elf] + stap
        if newvalue >= len(recipes):
            elfrecipes[elf] = newvalue % len(recipes)
        else:
            elfrecipes[elf] = newvalue

print(''.join(str(d) for d in recipes[maxrecepten:maxrecepten+10]))
