# Job Allocation System

employees = ["Arun", "Priya", "Kumar"]

cost = [
    [10, 2, 8],
    [9, 7, 5],
    [6, 4, 3]
]

n = len(employees)

best_cost = [9999]
best_assignment = []

def allocate(index, used, total, assignment):
    if index == n:
        if total < best_cost[0]:
            best_cost[0] = total
            best_assignment.clear()
            best_assignment.extend(assignment)
        return

    for job in range(n):
        if job not in used:
            new_total = total + cost[index][job]

            if new_total < best_cost[0]:
                used.add(job)
                assignment.append(job)

                allocate(index + 1, used,
                         new_total, assignment)

                assignment.pop()
                used.remove(job)

allocate(0, set(), 0, [])

print("Minimum Cost:", best_cost[0])
print("Job Allocation:")

for i in range(n):
    print(employees[i],
          "-> Job", best_assignment[i] + 1)