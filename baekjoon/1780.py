import sys 
sys.stdin = open("./baekjoon/testcase.txt")

n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)
    

counts = [0,0,0]

def solve(r, c, width):
    v = matrix[r][c]
    valid = True
    for i in range(r, r+width):
        for j in range(c, c+width):
            if v != matrix[i][j]:
                valid = False
                break
    if (valid):
        counts[v] += 1
    else:
        new_width = width // 3
        for i in range(0, 3):
            for j in range(0, 3):
                solve(r+i*new_width, c+j*new_width, new_width)

r, c, width = 0, 0, n
solve(r, c, width)
print(counts[-1])
print(counts[0])
print(counts[1])