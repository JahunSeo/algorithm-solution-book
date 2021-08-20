import sys
from collections import deque
sys.stdin = open("./beakjoon/testcase.txt", "r")

M, N, H = tuple(map(int, sys.stdin.readline().split()))

# 1단계: 매트릭스 구성하기 + 여러 개의 시작점 찾기 (익어 있는 토마토)
# - 여러 개의 익어 있는 토마토를 시작 시점의 frontier로 판단
# - 익어야 하는 개수(goal_count)를 정해, 탐색된 위치의 수가 이 값보다 작은지 확인
matrix = []
frontier = []
goal_count = 0
for h in range(H):
    space = []
    for x in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        space.append(row)
        for y in range(M):
            if row[y] == 1:
                frontier.append((h, x, y))
            elif row[y] == 0:
                goal_count += 1
    matrix.append(space)


# 2단계: 탐색하기
# - 매트릭스 상의 값이 0 이면 아직 탐색이 안된 상태를 의미
# - 매트릭스 상의 값이 1 이상이면 이미 탐색이 된 상태를 의미하며, 그 값은 탐색된 순서를 의미
def BFS(matrix, frontier):
    # 탐색한 위치 개수 초기값 설정
    search_count = 0
    # 만약 이미 탐색할 위치가 없다면 종료
    if goal_count == 0:
        return search_count
    
    # 탐색 소요 시간 초기값 설정
    max_time = 0

    dhs = [0,0,0,0,-1,1]
    dxs = [-1,1,0,0,0,0]
    dys = [0,0,-1,1,0,0]

    frontier = deque(frontier)
    while frontier:
        v1 = frontier.popleft()
        v1_h, v1_x, v1_y = v1
        v1_time = matrix[v1_h][v1_x][v1_y]
        for dh, dx, dy in zip(dhs, dxs, dys):
            h = v1_h + dh
            x = v1_x + dx
            y = v1_y + dy
            # 매트릭스 상에 존재하는 위치인지 확인
            if h < 0 or h >= H or x < 0 or x >= N or y < 0 or y >= M:
                continue
            # 이동 가능한 위치인지 확인
            #  - 값이 -1인 경우, 이동 불가
            #  - 값이 1 이상인 경우, 이미 발견 혹은 탐색된 영역
            if matrix[h][x][y] != 0:
                continue
            # 새로운 위치인 경우
            search_count += 1
            # 해당 위치의 시간 표시
            matrix[h][x][y] = v1_time + 1
            # 소요 시간 계산
            # - 시작점의 시간이 1 부터 시작됨을 고려해 계산
            if max_time < v1_time: 
                max_time = v1_time
            # 탐색할 영역으로 추가
            frontier.append((h, x, y))

    if search_count == goal_count:
        return max_time
    else:
        return -1

print(BFS(matrix, frontier))