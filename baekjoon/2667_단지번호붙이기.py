import sys
from collections import deque

sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    row = [int(c) for c in sys.stdin.readline().rstrip()]
    matrix.append(row)

# print(N)
# print(matrix)

# 인접 셀을 탐색하는 함수 생성
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def BFS(s, parent):
    frontier = deque([s])
    # 초기값 1로 설정, 참고로 인접한 셀이 아무것도 없을 수도 있음
    count = 1
    while frontier:
        v1 = frontier.popleft()
        r1, c1 = v1
        # 인접한 4개 방향을 탐색
        for dx, dy in zip(dxs, dys):
            r2, c2 = r1+dx, c1+dy
            # 존재하는 영역인지 확인
            if r2 < 0 or r2 >= N or c2 < 0 or c2 >= N:
                continue
            # 탐색 불필요한 영역인지 확인 (0인지 확인)
            if matrix[r2][c2] == 0:
                continue
            # 이미 방문한 영역인지 확인
            v2 = (r2, c2)
            if v2 in parent:
                continue
            # 새로운 영역인 경우
            parent[v2] = v1
            count += 1
            frontier.append(v2)
    return count


parent = {}
islands = {}
island_id = 2
# 전체 셀들을 돌면서 아직 발견되지 않은 셀 확인
for r in range(N):
    for c in range(N):
        v = (r, c)
        # 탐색 불필요한 영역인지 확인
        if matrix[r][c] == 0:
            continue
        # 아직 발견되지 않은 위치라면 발견 위치를 시작점으로 인접한 셀 탐색
        if v not in parent:
            parent[v] = None
            # 인접한 셀이 몇 개인지 리턴받아 저장
            count = BFS(v, parent)
            islands[island_id] = count
            # 아이디 업데이트
            island_id += 1


# 정답 출력
islands = list(islands.values())
islands.sort()

print(len(islands))
for v in islands:
    print(v)

