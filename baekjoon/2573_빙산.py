import sys
from collections import deque

sys.stdin = open("./baekjoon/testcase.txt")

N, M = tuple(map(int, sys.stdin.readline().split())) 
matrix = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)


# 매트릭스 전체적으로 돌면서 새로운 시작점을 발견하면 BFS 실시
def count_island():
    parent = {}
    island = 0
    for r in range(N):
        for c in range(M):
            # 매트릭스 상에서 값이 0 이면 넘어감
            if matrix[r][c] == 0:
                continue
            # 매트릭스 상에서 값이 0인데 이미 탐색되었으면 넘어감
            v1 = (r, c)
            if v1 in parent:
                continue
            # 탐색되지 않은 새로운 위치 발견 시, 해당 위치를 시작점으로 탐색 시작
            island += 1
            # print("new", island, v1)
            BFS(v1, parent)

    return island

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def BFS(s, parent):
    parent[s] = None
    queue = deque([s])
    while queue:
        v1 = queue.popleft()
        r, c = v1
        # 특정 위치의 4개 방향을 확인하며
        # - 0인 경우 v1의 값을 1 감소
        # - 0보다 큰 경우 새로운 탐색 영역으로 queue에 추가 
        height1 = matrix[r][c]
        zero_count = 0
        for dx, dy in zip(dxs, dys):
            r2, c2 = r+dx, c+dy
            v2 = (r2, c2)
            # 존재하지 않는 영역인지 확인
            if r2 < 0 or r2 >= N or c2 < 0 or c2 >= M:
                continue
            # 이미 방문한 영역인지 확인 
            # - 0보다 높은 영역만 이미 방문한 영역에 추가해주어야 함
            # - 0인 영역까지 방문 영역에 추가하면 인접한 다른 영역의 탐색에 영향을 줌
            if v2 in parent:
                continue
            # 새로운 영역인 경우, 높이 확인
            height2 = matrix[r2][c2]
            # 높이가 0인 경우
            if height2 == 0:
                zero_count += 1
            # 높이가 0보다 큰 경우
            else:
                parent[v2] = v1
                queue.append(v2)
        matrix[r][c] = max(height1 - zero_count, 0)

def print_matrix():
    for row in matrix:
        print(row)

time = -1
count = 1
while count == 1:
    time += 1
    count = count_island()
    # print_matrix()
    if count == 0:
        time = 0
        break

print(time)