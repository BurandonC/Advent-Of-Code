import sys
from collections import defaultdict, Counter
infile = sys.argv[1] if len(sys.argv)>=2 else 'day4.in'
D = open(infile).read().strip().split('\n')

n = len(D)
m = len(D[0])

#genereate all directions
dd = []

for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            dd.append((dx, dy))

def has_xmas(i, j, d):
    dx, dy = d
    for k, x in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if D[ii][jj] != x:
            return False
    return True

def has_mas(i, j):
    if not(1 <= i < n - 1 and 1 <= j < m -1):
        return False
    if D[i][j] != "A":
        return False
    
    diag_1 = f"{D[i-1][j-1]}{D[i+1][j+1]}"
    diag_2 = f"{D[i-1][j+1]}{D[i+1][j-1]}"

    if diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]:
        return True
    return False

res = 0
ans = 0
for i in range(n):
    for j in range(m):
        for d in dd:
            res += has_xmas(i, j, d)

for i in range(n):
    for j in range(m):
        ans += has_mas(i, j)

        
print(res)
print(ans)