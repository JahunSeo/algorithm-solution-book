import sys
# sys.stdin = open("./baekjoon/testcase.txt")
C, R = tuple(map(int, sys.stdin.readline().split()))

matrix = []
for _ in range(R):
    row =  [c for c in sys.stdin.readline().rstrip()]
    matrix.append(row)

# print(C, R)
# print(matrix)

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def DFS_visit(v1, target):
    global count
    # print(v1, target, count)
    # 개수 추가
    count += 1
    # 방문 처리
    x1, y1 = v1
    matrix[x1][y1] = 0
    for dx, dy in zip(dxs, dys):
        x2, y2 = x1 + dx, y1 + dy
        v2 = (x2, y2)
        # 존재하는 영역인지 확인
        if x2 < 0 or x2 >= R or y2 < 0 or y2 >= C:
            continue
        # 이미 방문한 영역인지 확인
        if matrix[x2][y2] == 0:
            continue
        # 추가 탐색
        if matrix[x2][y2] == target:
            DFS_visit(v2, target)


white_score = 0
blue_score = 0
for r in range(R):
    for c in range(C):
        target = matrix[r][c]
        if target != 0:
            count = 0
            DFS_visit((r,c), target)
            # print((r,c), target, count)
            if target == "W":
                white_score += count * count
            else:
                blue_score += count * count

print(white_score, blue_score)
