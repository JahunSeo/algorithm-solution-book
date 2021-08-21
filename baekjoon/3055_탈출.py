import sys

sys.stdin = open("./baekjoon/testcase.txt")

R, C = tuple(map(int, sys.stdin.readline().split()))
matrix = []
START, GOAL = None, None
WIZARD = []

for r in range(R):
    row = [v for v in sys.stdin.readline().rstrip()]
    for c, value in enumerate(row):
        if value == "D": 
            GOAL = (r, c)
        elif value == "S":
            START = (r, c)
        elif value == "*": 
            WIZARD.append((r, c))
    matrix.append(row)

# 2단계: 각 매트릭스의 탐색 실시
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# frontier 큐 생성: 
# - 행위자 정보를 함께 저장
# - 홍수 먼저, 고슴도치 다음
frontier = [(v, "*") for v in WIZARD] + [(START, "S")]
time = 0
success = False

# print("[time]", time)
# print("  matrix:")
# for row in matrix:
#     print("  ", row)
# print("  frontier:")
# print("  ", frontier)

while not success and frontier:
    time += 1
    next_frontier = []
    for v1, actor in frontier:
        x1, y1 = v1
        for dx, dy in zip(dxs, dys):
            x2, y2 = x1+dx, y1+dy
            v2 = (x2, y2)
            # 존재하는 위치인지 확인
            if x2 < 0 or x2 >= R or y2 < 0 or y2 >= C:
                continue
            # 장애물이 놓인 위치인지 확인
            status = matrix[x2][y2]
            if status == "X":
                continue
            # actor에 따라 구분하여 행동
            # 행위자가 홍수인 경우, 이동하려는 위치의 상태가 홍수, D이면 제외
            if actor == "*" and (status in [".", "S"]):
                matrix[x2][y2] = "*"
                next_frontier.append((v2, "*"))
            # 행위자가 고슴도치인 경우, 아동하려는 위치의 상태가 홍수, 본인이면 제외
            elif actor == "S" and status == "D":
                # 도착지에 도착했으면 탐색 종료
                matrix[x2][y2] = "S"
                success = True
                break
            elif actor == "S" and status == ".":
                matrix[x2][y2] = "S"
                next_frontier.append((v2, "S"))
    frontier = next_frontier

    # print("[time]", time)
    # print("  matrix:")
    # for row in matrix:
    #     print("  ", row)
    # print("  frontier:")
    # print("  ", frontier)

if success:
    print(time)
else:
    print("KAKTUS")