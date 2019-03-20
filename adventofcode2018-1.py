#!python3

frequency = 0
freqlist = set()

input = open("input", "r")

while 1:
    for line in input:
        change = line
        frequency = frequency + int(change)
        if frequency in freqlist:
            print("eerste dubbele: " + str(frequency))
            exit()
        else:
            freqlist.add(frequency)
    input.seek(0,0)
