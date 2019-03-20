#!python3

zoekstring='880751'
#zoekstring='51589'
#zoekstring='01245'
#zoekstring='92510'
#zoekstring='59414'
matchlen = None
matchstart = None
found = 0

def zoeken(list, zoekstring):
    print("zoeken in:" + str(list))
    start = None
    lengte = 0

    for letter in range(len(list)):
        if start is None:
            if zoekstring[0] == str(list[letter]):
                start = letter
                lengte = 1
        else:
            if zoekstring[lengte] == str(list[letter]):
                lengte += 1
            else:
                start = zoeken(list[start+1:], zoekstring)
                break
            
    return start

recipes = [3, 7]
elfrecipes = [0, 1]

#for teller in range(maxrecepten+10):
while not found:
    som = 0
    for elf in elfrecipes:
        som += int(recipes[elf])
    #print("Lus door som: " + str(som))
    for i in str(som):
        recipes.extend([int(i)])
        if matchstart is None:
            if i == zoekstring[0]:
                print("Eerste teken gevonden: " + i + " op index " + str(len(recipes)-1))
                matchstart = len(recipes) - 1
                matchlen = 1
        else:
            if i == zoekstring[matchlen]:
                print("Vervolgteken gevonden: " + i + " op index " + str(len(recipes)-1))
                matchlen += 1
                found = (matchlen == len(zoekstring))
            else: 
                print("Vervolgteken gemist: " + i + " op index " + str(len(recipes)-1))
                # terug en zoeken naar een nieuw begin
                #substart = zoeken(recipes[matchstart+1:], zoekstring)
                #if substart is None:
                matchstart = None
                matchlen = 0
                #else:
                    #matchstart += substart
                    #matchlen = len(recipes) - 1 - matchstart

#    print(recipes, elfrecipes)
    for elf in range(len(elfrecipes)):
        stap = recipes[elfrecipes[elf]] + 1
        newvalue = elfrecipes[elf] + stap
        if newvalue >= len(recipes):
            elfrecipes[elf] = newvalue % len(recipes)
        else:
            elfrecipes[elf] = newvalue

print("Het feest begint op " + str(matchstart))
