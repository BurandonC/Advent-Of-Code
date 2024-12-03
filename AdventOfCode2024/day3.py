import sys
from collections import defaultdict, Counter
infile = sys.argv[1] if len(sys.argv)>=2 else 'day3.in'
D = open(infile).read().strip()

import re

def calc_sum():
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    combined_pattern = f"{do_pattern}|{dont_pattern}|{pattern}"

    matches = re.finditer(combined_pattern, D)

    enabled = True
    total = 0

    for match in matches:
        if match.group()=="do()":
            enabled = True
        elif match.group() == "don't()":
            enabled = False
        else:
            if enabled:
                x, y = map(int, match.groups())
                total += x * y

    #res = sum(int(x) * int(y) for x, y in matches)
    #return res
    return total

if __name__ == "__main__":
    total = calc_sum()
    print(total)