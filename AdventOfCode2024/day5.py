with open ("./day5.in") as fin:
    raw_rules, updates = fin.read().strip().split("\n\n")
    rules = []
    for line in raw_rules.split("\n"):
        a, b = line.split("|")
        rules.append((int(a), int(b)))
    updates = [list(map(int, line.split(",")))for line in updates.split("\n")]

#part1
def follow_rules(update):
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i

    for a, b in rules:
        if a in idx and b in idx and not idx[a] < idx[b]:
            return False, 0
    return True, update[len(update) // 2]

#part2
def insertion_sort(update):
    sorted = []

    for page in update:
        #finding the correct position for insertion of the correct page
        inserted = False
        for i in range(len(sorted) + 1):
            temp_update = sorted[:i] + [page] + sorted[i:]

            #checking if temp list satisfies all rules
            if all(
                (a not in temp_update or b not in temp_update or temp_update.index(a) < temp_update.index(b))
                for a, b in rules
            ):
                sorted = temp_update
                inserted = True
                break
        if not inserted:
            raise ValueError(f"Cannot insert page {page} without violating rules")

    return sorted
    

ans = 0
ans_incorrect = 0

for update in updates:
    good, mid = follow_rules(update)
    if good:
        ans += mid

# Process updates
ans_incorrect = 0
for update in updates:
    good, mid = follow_rules(update)
    if not good:  # Incorrect updates
        ordered_update = insertion_sort(update)
        ans_incorrect += ordered_update[len(ordered_update) // 2]

print(ans_incorrect)
print(ans)