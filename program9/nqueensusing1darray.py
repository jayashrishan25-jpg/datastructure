# N-Queens using Backtracking

N = 4
board = [-1] * N

def safe(row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve(row):
    if row == N:
        print(board)
        return

    for col in range(N):
        if safe(row, col):
            board[row] = col
            solve(row + 1)
            board[row] = -1

print("Solutions:")
solve(0)