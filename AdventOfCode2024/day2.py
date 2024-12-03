import sys
from collections import defaultdict, Counter
infile = sys.argv[1] if len(sys.argv)>=2 else 'day2.in'
D = open(infile).read().strip()


def is_safe(report):
    #check if the report is safe
    #levels must all be increasing or decreasing
    #any two adjacent levels differ by 1 to 3 inclusive
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]

    AI = all(1 <= diff <= 3 for diff in diffs)
    AD = all(-3 <= diff <= -1 for diff in diffs)

    return AI or AD

def is_safe_with_removal(report):
    #can we make it safe by removing one level
    for i in range(len(report)):
        mod_report = report[:i] + report[i+1:]
        if is_safe(mod_report):
            return True
    return False
        
def count_safe(data):
    #counts the number of safe reports in input data
    SC = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_safe(report) or is_safe_with_removal(report):
            SC += 1
    return SC

data = D.splitlines()
safe_reports = count_safe(data)
print(safe_reports)