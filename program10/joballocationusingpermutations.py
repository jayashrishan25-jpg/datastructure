# Job Allocation using Branch and Bound

from itertools import permutations

cost = [
    [10, 2, 8],
    [9, 7, 5],
    [6, 4, 3]
]

n = len(cost)

minimum = 9999
best = None

for jobs in permutations(range(n)):
    total = 0

    for employee in range(n):
        total += cost[employee][jobs[employee]]

    if total < minimum:
        minimum = total
        best = jobs

print("Minimum Cost:", minimum)

for employee in range(n):
    print("Employee", employee + 1,
          "-> Job", best[employee] + 1)