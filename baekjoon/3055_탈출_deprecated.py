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

print("flood before", flood_matrix)
frontier = deque(WIZARD[:])
while frontier:
    v1 = frontier.popleft()
    x1, y1 = v1
    for dx, dy in zip(dxs, dys):
        x2, y2 = x1+dx, y1+dy
        # 존재하는 위치인지 확인
        if x2 < 0 or x2 >= R or y2 < 0 or y2 >= C:
            continue
        # 장애물이거나 이미 탐색된 영역인지 확인 
        # (홍수 매트릭스의 경우, 도착지점 여부 함께 확인)
        if flood_matrix[x2][y2] != 0:
            continue
        # 탐색되지 않은 영역인 경우
        flood_matrix[x2][y2] = flood_matrix[x1][y1] + 1
        frontier.append((x2,y2))
print("flood after ", flood_matrix)

print("route before", route_matrix)
frontier = deque([START])
while frontier:
    v1 = frontier.popleft()
    x1, y1 = v1
    time1 = route_matrix[x1][y1]
    for dx, dy in zip(dxs, dys):
        x2, y2 = x1+dx, y1+dy
        time2 = time1 + 1
        # 존재하는 위치인지 확인
        if x2 < 0 or x2 >= R or y2 < 0 or y2 >= C:
            continue
        # 장애물이거나 이미 탐색된 영역인지 확인
        if route_matrix[x2][y2] != 0:
            continue
        # 이미 물이 차오른 영역인지 확인
        if flood_matrix[x2][y2] != 0 and flood_matrix[x2][y2] <= time2:
            continue
        # 이동 가능한 영역인 경우
        route_matrix[x2][y2] = time2
        frontier.append((x2,y2))
print("route after ", route_matrix)

# 3단계: 좌표 확인하기
x, y = GOAL
time = route_matrix[x][y] 
if time:
    print(time - 1)
else:
    print("KAKTUS")