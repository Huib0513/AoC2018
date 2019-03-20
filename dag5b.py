#!python3
import re

def ongeveergelijk(letter1, letter2):
    if letter1 == letter2:
        return 0

    if letter1.lower() == letter2.lower():
        return (letter1.isupper() and letter2.islower()) or (letter1.islower() and letter2.isupper())

def krimp(thingy):
    teller = 0
    while teller < (len(thingy)-1):
        if ongeveergelijk(thingy[teller], thingy[teller+1]):
            thingy = thingy[:teller] + thingy[teller+2:]
            if teller > 0:
                teller -= 1
        else:
            teller += 1
    return thingy

# Main loop
regels = open('input.dag5').read().splitlines()

unieken = set(regels[0].lower())

for letter in unieken:
    toreplace = letter.lower() + "|" + letter.upper()
    solution = krimp(re.sub(toreplace, "", regels[0]))
    print(toreplace + ": " + str(len(solution)))
