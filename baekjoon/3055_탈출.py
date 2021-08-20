import sys
from collections import deque

sys.stdin = open("./baekjoon/testcase.txt")

R, C = tuple(map(int, sys.stdin.readline().split()))
matrix = []
START, GOAL = None, None
BLOCK, WIZARD = [], []

for r in range(R):
    row = [v for v in sys.stdin.readline().rstrip()]
    for c, value in enumerate(row):
        if value == "D": 
            GOAL = (r, c)
        elif value == "S":
            START = (r, c)
        elif value == "*": 
            WIZARD.append((r, c))
        elif value == "X":
            BLOCK.append((r, c))
    matrix.append(row)

# 1단계: 매트릭스 생성
# 홍수 매트릭스 생성
flood_matrix = []
for r in range(R):
    row = [0]*C
    flood_matrix.append(row)
# 홍수 매트릭스에 발원지, 목적 지점, 장애물 표시
flood_matrix[GOAL[0]][GOAL[1]] = float("inf")
for r, c in WIZARD:
    flood_matrix[r][c] = 1
for r, c in BLOCK:
    flood_matrix[r][c] = -1

# 이동경로 매트릭스 생성
route_matrix = []
for r in range(R):
    row = [0]*C
    route_matrix.append(row)
# 이동경로 매트릭스에 출발 지점, 장애물 표시
route_matrix[START[0]][START[1]] = 1
for r, c in BLOCK:
    route_matrix[r][c] = -1

# 2단계: 각 매트릭스의 탐색 실시
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def BFS(matrix, frontier):
    frontier = deque(frontier)
    while frontier:
        v1 = frontier.popleft()
        x1, y1 = v1
        for dx, dy in zip(dxs, dys):
            x2, y2 = x1+dx, y1+dy
            # 존재하는 위치인지 확인
            if x2 < 0 or x2 >= R or y2 < 0 or y2 >= C:
                continue
            # 장애물이거나 이미 탐색된 영역인지 확인 (홍수 매트릭스의 경우, 도착지점 여부 함께 확인)
            if matrix[x2][y2] != 0:
                continue
            # 탐색되지 않은 영역인 경우
            matrix[x2][y2] = matrix[x1][y1] + 1
            frontier.append((x2,y2))

# print("flood before", flood_matrix)
BFS(flood_matrix, WIZARD[:])
# print("flood after ", flood_matrix)

# print("route before", route_matrix)
BFS(route_matrix, [START])
# print("route after ", route_matrix)

# 3단계: 좌표 비교하기
# 목표 지점의 상하좌우 중 한 곳이라도 flood_matrix > route_matrix 인 곳이 있다면 성공
# 성공이라면 목표지점의 최소 경로 제출

success_time = float("inf")
for dx, dy in zip(dxs, dys):
    x, y = GOAL[0] + dx, GOAL[1] + dy
    if x < 0 or x >= R or y < 0 or y >= C:
        continue
    route_time = route_matrix[x][y]
    flood_time = flood_matrix[x][y]
    if route_time < flood_time and route_time < success_time:
        success_time = route_time

if success_time:
    # 정확히는 1을 더한 뒤 다시 1을 뺀 값
    print(success_time) 
else:
    print("KAKTUS")