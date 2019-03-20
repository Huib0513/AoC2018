#!python3

tweetjes = 0
drietjes = 0

input = open("input.dag2", "r")

for line in input:
    lijst = {}
    for letter in range(0, len(line)-1):
        if line[letter] in lijst:
            lijst[line[letter]] += 1
        else:
            lijst[line[letter]] = 1
    if 2 in lijst.values():
        tweetjes += 1
    if 3 in lijst.values():
        drietjes +=1

input.close()

print(lijst)
print(str(tweetjes) + " " + str(drietjes) + " " + str(tweetjes * drietjes))

