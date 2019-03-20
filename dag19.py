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

opcodes = [ 
    addr, addi, mulr, muli, 
    banr, bani, borr, bori, 
    setr, seti, 
    gtir, gtri, gtrr, 
    eqir, eqri, eqrr] 

opcodeindex = { 
    'addr': 0, 'addi': 1, 'mulr': 2, 'muli': 3, 
    'banr': 4, 'bani': 5, 'borr': 6, 'bori': 7, 
    'setr': 8, 'seti': 9, 
    'gtir': 10, 'gtri': 11, 'gtrr': 12, 
    'eqir': 13, 'eqri': 14, 'eqrr': 15} 

#lines = open('testinput.dag19').read().splitlines()
lines = open('input.dag19').read().splitlines()

# Read program
ipregister = None
progline = defaultdict(list)
index = 0
for line in lines:
    if line[0] == '#':
        ipregister = int(line[4:])
        #print(ipregister)
    else:
        words = line.split(' ')
        progline[index].append(words[0])
        progline[index].extend([int(x) for x in words[1:]])
        #print(index, progline)
        index += 1

#Execute program
registers = [0, 0, 0, 0, 0, 0]
ip = 0
while ip < len(progline):
    #print(ip, progline[ip][0],progline[ip][1], progline[ip][2], progline[ip][3], registers)
    registers[ipregister] = ip
    #print(ip, progline[ip][0],progline[ip][1], progline[ip][2], progline[ip][3], registers)
    opcodes[opcodeindex[progline[ip][0]]](progline[ip][1], progline[ip][2], progline[ip][3], registers)
    #print(ip, progline[ip][0],progline[ip][1], progline[ip][2], progline[ip][3], registers)
    ip = registers[ipregister] + 1
    #print(ip, progline[ip][0],progline[ip][1], progline[ip][2], progline[ip][3], registers)

print(registers[0])

#print(opcodes)
#print(tematchenopcodes)
#print(bekendeopcodes.keys())
#for op in bekendeopcodes:
    #print(str(op), bekendeopcodes[op])
