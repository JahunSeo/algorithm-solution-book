import sys
from collections import deque

sys.stdin = open("./baekjoon/testcase.txt")

N, M = tuple(map(int, sys.stdin.readline().split()))
matrix = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

def print_matrix():
    for row in matrix:
        print(row)
    print()

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 1단계: 외부 공기를 탐색
# - 반드시 외부 공기인 (0,0) 셀을 시작으로 탐색 가능한 영역까지 확장
# - 이 때, 자연스럽게 외부 공기가 닿은 치즈들을 확인하므로 본인(외부 공기)이 영향을 준 치즈들에 표시
# - 2개 이상의 외부 공기 셀에 영향을 받아야 하므로, 치즈 셀에 영향 받은 횟수를 누적하는 방식으로 진행
# - (이미 탐색 완료한 외부 공기 셀은 다시 방문하지 않도록 처리하므로, 동일한 카운팅이 반복되지 않음)
def update_matrix():
    s = (0,0)
    parent = {s: None}
    queue = deque([s])

    while queue:
        v1 = queue.popleft()
        r1, c1 = v1
        for dx, dy in zip(dxs, dys):
            r2, c2 = r1+dx, c1+dy
            # 존재하는 위치인지 확인
            if r2 < 0 or r2 >= N or c2 < 0 or c2 >= M:
                continue
            v2 = (r2, c2)
            # 이미 방문한 셀인지 확인 (외부 공기 셀만 추가되어 있음)
            if v2 in parent:
                continue
            cell = matrix[r2][c2]
            # 외부 공기 셀인 경우, 다음 탐색 범위에 추가
            if cell == 0:
                parent[v2] = v1
                queue.append(v2)
            # 치즈 셀인 경우, 본인(v1, 외부 공기)이 영향을 주게 되므로 치즈 셀에 +1
            else:
                matrix[r2][c2] += 1


# 2단계: 영향을 받은 치즈 정리
# - 2개 이상의 외부 공기 셀에 영향을 받은 치즈는 0으로, 그렇지 못한 치즈는 다시 1로 되돌림
# - 이 때, 종료 여부를 판단하기 위해 남아 있는 치즈 개수를 함께 확인
def count_cheese():
    cheese_count = 0
    for r in range(N):
        for c in range(M):
            cell = matrix[r][c]
            # 영향을 준 외부 공기가 2개 이상인 경우 (1부터 시작하므로 3 이상)
            if cell >= 3:
                matrix[r][c] = 0
            # 영향을 준 외부 공기가 0~1개인 경우, 사라지지 않으므로 다시 1로 되돌림
            elif cell >= 1:
                matrix[r][c] = 1
                # 남은 치즈 개수에 추가
                cheese_count += 1
            # 외부 공기인 경우(cell == 0) 패스     
    return cheese_count


cheese_count = count_cheese()
time = 0
while cheese_count:
    time += 1
    update_matrix()
    cheese_count = count_cheese()

print(time)

