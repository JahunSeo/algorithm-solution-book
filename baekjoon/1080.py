import sys
sys.stdin = open("./baekjoon/testcase.txt")

R, C = tuple(map(int, sys.stdin.readline().split())) 
A = []
for i in range(R):
    row = [int(c) for c in sys.stdin.readline().rstrip()]
    A.append(row)
B = []
for i in range(R):
    row = [int(c) for c in sys.stdin.readline().rstrip()]
    B.append(row)

def replace(val):
    if val == 0: return 1
    else: return 0

def solve():
    global A, B
    count = 0
    for r in range(R):
        for c in range(C):
            if A[r][c] != B[r][c]:
                if r + 2 >= R or c + 2 >= C:
                    return -1
                count += 1
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        A[i][j] = replace(A[i][j])
    return count

print(solve())
