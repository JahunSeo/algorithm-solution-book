import sys
from collections import deque

sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())

matrix = []
shark = None 
for r in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for c in range(N):
        cell = row[c]
        # 상어인 경우, 위치 저장
        if cell == 9:
            shark = (r, c)
    matrix.append(row)


# 다음으로 찾아갈 먹이 위치를 찾는 함수
# - 남은 먹이들을 하나씩 탐색하며 가장 최적의 조건으로 업데이트
# - 필수 조건: 1) 본인보다 낮아야 함 2) 이동 거리가 최소여야 함
# - 선별 조건: 1) 상단일수록 좋음(행이 낮은 것) 2) 좌측일수록 좋음(열이 낮은 것)

# [주의] 이 때, 우선 순위에 맞게 탐색될 수 있도록 상>좌>우>하 순으로 설정
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def find_shortest(shark, shark_size):
    r, c = shark
    # 초기 설정
    s = (r, c)
    parent = {s: None}
    time = 0
    frontier = deque([s])
    while frontier:
        time += 1
        next_frontier = []
        fishes = []
        for v1 in frontier:
            r1, c1 = v1
            for dx, dy in zip(dxs, dys):
                r2, c2 = r1+dx, c1+dy
                v2 = (r2, c2)   
                # 존재하는 영역인지 확인
                if r2 < 0 or r2 >= N or c2 < 0 or c2 >= N:
                    continue
                cell2 = matrix[r2][c2]
                # 지나갈 수 없는 영역인지 확인 (본인보다 큰 물고기가 있는 경우 우회해야 함)
                if cell2 > shark_size:
                    continue
                # 이미 탐색한 영역인지 확인
                if v2 in parent:
                    continue
                # 새로운 영역인 경우
                parent[v2] = v1
                next_frontier.append(v2)
                # 본인이 먹을 수 있는 물고기이면 물고기 리스트에 추가
                if cell2 > 0 and cell2 < shark_size:
                    fishes.append((r2, c2))
        # frontier 탐색 마친 상황에서 찾은 물고기가 있는지 확인
        if fishes:
            fishes.sort(key=lambda f: (f[0], f[1]))
            return fishes[0], time
        # 찾은 물고기가 없으면 다음 범위 탐색
        frontier = next_frontier
    # 목적지에 도달할 수 없는 경우 무한 리턴
    return None, float("inf")

def print_matrix():
    for row in matrix:
        print(row)
    print()


total_time = 0
fish_count = 0
shark_size = 2
# print("init:", shark, fish_count, total_time)
while shark:
    # 다음 타겟 찾기
    target, shortest = find_shortest(shark, shark_size)    
    # 다음 타겟이 없는 경우, 탐색 종료
    if not target:
        break
    # 다음 타겟이 있는 경우
    # 매트릭스에서 상어 위치 업데이트 (먹은 물고기 제거)
    sc, sr = shark
    tc, tr = target
    matrix[sc][sr] = 0
    matrix[tc][tr] = 9
    # 상어 정보 업데이트
    shark = (tc, tr)
    fish_count += 1
    if fish_count >= shark_size:
        shark_size += 1
        fish_count = 0
    total_time += shortest
    # print("result:", shark, fish_count, total_time)
    # print_matrix()

print(total_time)