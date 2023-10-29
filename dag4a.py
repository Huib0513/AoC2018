#!python3
from collections import defaultdict

regels = open('input.dag4').read().splitlines()
regels.sort()

guard = None
slaapjes = defaultdict(int)

for regel in regels:
    words = regel.split(" ")
    if words[2] == 'Guard':
        guard = int(words[3][1:])
        print(guard)
    elif words[2] == 'falls':
        start = words






#[1518-05-28 00:59] wakes up
#[1518-06-29 00:54] falls asleep
#[1518-08-22 00:16] falls asleep
#[1518-07-04 00:46] wakes up
#[1518-09-02 00:00] Guard #2137 begins shift
#[1518-05-01 00:45] falls asleep
#[1518-08-15 00:47] wakes up
#[1518-07-03 00:56] wakes up
