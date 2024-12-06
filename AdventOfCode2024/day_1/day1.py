import sys
from collections import defaultdict, Counter
infile = sys.argv[1] if len(sys.argv)>=2 else 'day1.in'
D = open(infile).read().strip()


LEFT = []
RIGHT = []
RC = Counter() #right counter

for line in D.strip().split('\n'):
    l, r = map(int, line.split())
    LEFT.append(l)
    RIGHT.append(r)
    RC[r] += 1

p1 = 0
LEFT = sorted(LEFT)
RIGHT = sorted(RIGHT)
for l,r in zip(LEFT,RIGHT): #
    p1 += abs(r-l)
print(p1)

p2 = 0
for l in LEFT:
    p2 += l * RC.get(l,0)
print(p2)