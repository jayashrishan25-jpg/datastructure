# Job Allocation using Branch and Bound

cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

n = 3
best_cost = [9999]
best_assignment = []

def solve(employee, assigned, current_cost, assignment):
    if employee == n:
        if current_cost < best_cost[0]:
            best_cost[0] = current_cost
            best_assignment.clear()
            best_assignment.extend(assignment)
        return

    for job in range(n):
        if job not in assigned:
            new_cost = current_cost + cost[employee][job]

            if new_cost < best_cost[0]:
                assigned.add(job)
                assignment.append(job)
                solve(employee + 1, assigned, new_cost, assignment)
                assignment.pop()
                assigned.remove(job)

solve(0, set(), 0, [])

print("Minimum Cost:", best_cost[0])
print("Assignment:")

for i, job in enumerate(best_assignment):
    print("Employee", i + 1, "-> Job", job + 1)