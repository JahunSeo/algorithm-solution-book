import sys
sys.stdin = open("./beakjoon/testcase.txt", "r")

N, M = tuple(map(int, sys.stdin.readline().split()))

matrix = []
for _ in range(N):
    row = sys.stdin.readline().rstrip()
    row = [int(c) for c in row]
    matrix.append(row)

def find_edge(r, c):
    edges = []
    if r-1 >= 0 and matrix[r-1][c]:
        edges.append((r-1, c))
    if r+1 < N and matrix[r+1][c]:
        edges.append((r+1, c))
    if c-1 >= 0 and matrix[r][c-1]:
        edges.append((r, c-1))
    if c+1 < M and matrix[r][c+1]:
        edges.append((r, c+1))
    return edges


def BFS(s=(0,0)):
    # 시작 위치도 포함이므로, s를 1로 설정
    level = {s: 1}
    parent = {s: None}
    i = 2
    frontier = [s]
    while frontier:
        next_frontier = []
        for v1 in frontier:
            edges = find_edge(v1[0], v1[1]) # r, c
            for v2 in edges:
                if v2 not in parent:
                    level[v2] = i
                    parent[v2] = v1
                    next_frontier.append(v2)
        frontier = next_frontier
        i += 1
    return level[(N-1, M-1)]

init_local = (0,0)
print(BFS(init_local))