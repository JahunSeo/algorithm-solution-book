import sys
sys.stdin = open("./baekjoon/testcase.txt")
R, C = tuple(map(int, sys.stdin.readline().split()))

matrix = []
for _ in range(R):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

# print(R, C)
# print(matrix)

memo = [[None] * C for _ in range(R)]
# print(memo)

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def DFS_visit(v1):
    (x1, y1, h1) = v1
    if x1 == R-1 and y1 == C-1:
        return 1

    if memo[x1][y1] != None:
        return memo[x1][y1]
    # next_local = []
    total = 0
    for dx, dy in zip(dxs, dys):
        x2 = x1 + dx
        y2 = y1 + dy
        if x2 < 0 or x2 >= R or y2 < 0 or y2>=C:
            continue
        h2 = matrix[x2][y2]
        if h2 < h1:
            # next_local.append((x2,y2,h2))
            count = DFS_visit((x2,y2,h2))
            total += count
    
    memo[x1][y1] = total
    return total

score = DFS_visit((0,0, matrix[0][0]))
print(score)