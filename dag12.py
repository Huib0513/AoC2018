#!python3

teller = 0
pattern = []
garden = []

for line in open('testinput.dag12'):
    if line.find('initial') == 0:
        garden.append(line.rstrip()[15:])
    elif len(line) == 1:
        pass
    else:
        pattern.append([line.rstrip().split(' => ')[0], line.rstrip().split(' => ')[1]])
        teller += 1
         

print(garden)
print(pattern)
