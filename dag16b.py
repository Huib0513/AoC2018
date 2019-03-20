#!python3
from collections import defaultdict

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
tematchenopcodes = opcodes.copy()

#lines = open('testinput.dag16').read().splitlines()
lines = open('input.dag16').read().splitlines()

bekendeopcodes = defaultdict(list)
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
        dematch = None
        #print('Proberen te matchen met ' + str(len(tematchenopcodes)) + ' opcodes.')
        for op in tematchenopcodes:
            before = registersvoor.copy()
            op(values[1], values[2], values[3], before)
            if before == registersna:
                matchingopcodes += 1
                dematch = op
                bekendeopcodes[values[0]].append(op)

        #print(str(values[0])+' matcht ' + str(matchingopcodes) + ' opcodes')
        if matchingopcodes == 1:
            #print(dematch)
            bekendeopcodes[values[0]] = [dematch]
            tematchenopcodes.remove(dematch)
        registersvoor = registersna = values = []
    else:
        values= list([int(x) for x in line.split(' ')])
        #print(values)

#print(opcodes)
#print(tematchenopcodes)
#print(bekendeopcodes.keys())
#for op in bekendeopcodes:
    #print(str(op), bekendeopcodes[op])

programlines = open('input.dag16b').read().splitlines()

registers = [0, 0, 0, 0]
for line in programlines:
    values = []
    values= list([int(x) for x in line.split(' ')])
    #print(values)
    print(bekendeopcodes[values[0]])
    bekendeopcodes[values[0]][0](values[1], values[2], values[3], registers)

print(registers)


#0 [<function eqir at 0x7ffddb254400>]
#1 [<function borr at 0x7ffddb254048>]
#2 [<function addr at 0x7ffddc44a268>]
#3 [<function gtri at 0x7ffddb2542f0>]
#4 [<function muli at 0x7ffddb25ee18>]
#5 [<function gtir at 0x7ffddb254268>]
#6 [<function mulr at 0x7ffddb2572f0>]
#7 [<function banr at 0x7ffddb25eea0>]
#8 [<function bori at 0x7ffddb2540d0>]
#9 [<function eqri at 0x7ffddb254488>]
#10 [<function eqrr at 0x7ffddb254510>]
#11 [<function bani at 0x7ffddb25ef28>]
#12 [<function setr at 0x7ffddb254158>]
#13 [<function gtrr at 0x7ffddb254378>]
#14 [<function addi at 0x7ffddc44a488>]
#15 [<function seti at 0x7ffddb2541e0>]
