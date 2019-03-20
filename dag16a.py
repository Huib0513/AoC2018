#!python3

def addr(a, b, c, start):
    start[c] = start[a] + start[b]
def addi(a, b, c, start):
    start[c] = start[a] + b

def mulr(a, b, c, start):
    start[c] = start[a] * start[b]
def muli(a, b, c, start):
    start[c] = start[a] * b

def banr(a, b, c, start):
    start[c] = start[a] & start[b]
def bani(a, b, c, start):
    start[c] = start[a] & b

def borr(a, b, c, start):
    start[c] = start[a] | start[b]
def bori(a, b, c, start):
    start[c] = start[a] | b

def setr(a, b, c, start):
    start[c] = start[a]
def seti(a, b, c, start):
    start[c] = a

def gtir(a, b, c, start):
    start[c] = int(a > start[b])
def gtri(a, b, c, start):
    start[c] = int(start[a] > b)
def gtrr(a, b, c, start):
    start[c] = int(start[a] > start[b])

def eqir(a, b, c, start):
    start[c] = int(a == start[b])
def eqri(a, b, c, start):
    start[c] = int(start[a] == b)
def eqrr(a, b, c, start):
    start[c] = int(start[a] == start[b])

opcodes = { 
    addr, addi, mulr, muli, 
    banr, bani, borr, bori, 
    setr, seti, 
    gtir, gtri, gtrr, 
    eqir, eqri, eqrr} 

#lines = open('testinput.dag16').read().splitlines()
lines = open('input.dag16').read().splitlines()

matching = 0
registersvoor = registersna = values = []
for line in lines:
    if len(line) == 0:
        continue

    if line.split(':')[0] == 'Before':
        registersvoor= list([int(x) for x in line.split(': ')[1].strip('[ ]').split(',')])
        #print(registersvoor)
    elif line.split(':')[0] == 'After':
        registersna= list([int(x) for x in line.split(': ')[1].strip('[ ]').split(',')])
        
        matchingopcodes = 0
        for op in opcodes:
            before = registersvoor.copy()
            op(values[1], values[2], values[3], before)
            if before == registersna:
                matchingopcodes += 1

        if matchingopcodes >= 3:
            matching += 1
        #print('Doe iets met opcodes en controleer of het gelijk is aan')
        #print(registersna)
        registersvoor = registersna = values = []
    else:
        values= list([int(x) for x in line.split(' ')])
        #print(values)

print('Het zijn er ' + str(matching))
