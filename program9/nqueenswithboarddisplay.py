# N-Queens Problem

N = 4
board = [-1] * N

def is_safe(row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == N:
        display()
        return

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            solve(row + 1)
            board[row] = -1

def display():
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

print("N-Queens Solutions:")
solve(0)