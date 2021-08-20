import sys
from collections import defaultdict, deque

sys.stdin = open("./beakjoon/testcase.txt", "r")

N, M, s = list(map(int, sys.stdin.readline().split()))
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 인접 리스트 구성하기
# 정점 번호가 낮은 것부터 먼저 처리해야 하므로(순서가 있으므로) list로 선택
adj = defaultdict(list)
for v1, v2 in edges:
    adj[v1].append(v2)
    adj[v2].append(v1)
# 각 정점의 인접 리스트 정렬
for v in adj:
    adj[v].sort()


def DFS(adj, s):
    # 본래 여러 개의 트리가 만들어지는 상황을 고려해야 하지만
    # 문제 특성 상 하나의 트리가 만들어지는 것으로 설정
    parent = {s: None}
    visited = [s]

    def DFS_visit(adj, s):
        for v in adj[s]:
            if v not in parent:
                parent[v] = s
                visited.append(v)
                DFS_visit(adj, v)

    DFS_visit(adj, s)
    return visited

def BFS(adj, s):
    parent = {s: None}
    visited = [s]
    frontier = deque([s])
    while frontier:
        v1 = frontier.popleft()
        for v2 in adj[v1]:
            if v2 not in parent:
                parent[v2] = v1
                visited.append(v2)
                frontier.append(v2)
    return visited

print(" ".join(str(v) for v in DFS(adj, s)))
print(" ".join(str(v) for v in BFS(adj, s)))