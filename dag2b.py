#!python3

def compare(code1, code2):
    ongelijken = 0

    if len(code1) != len(code2):
        return 0
    for teller in range(0, len(code1)):
        if code1[teller] != code2[teller]:
            ongelijken += 1
    return ongelijken

def equality(code1, code2):
    result = ''
    for teller in range(0, len(code1)):
        if code1[teller] == code2[teller]:
            result = result + code1[teller]
    return result

# initialize
gelijken = {}

input = open("input.dag2", "r")
allcodes = input.readlines()
input.close()

# Main loop
for teller in range(0, len(allcodes)):
    for latere in allcodes[teller+1:]:
        if compare(allcodes[teller], latere) == 1:
            gelijken[allcodes[teller]] = latere;


for key in gelijken:
    print(key)
    print(gelijken[key])
    print(equality(key, gelijken[key]))

