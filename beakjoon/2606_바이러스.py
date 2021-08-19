import sys
from collections import defaultdict, deque

sys.stdin = open("./beakjoon/testcase.txt", "r")

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

edges = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]

adj = defaultdict(list)
for v1, v2 in edges:
    adj[v1].append(v2)
    adj[v2].append(v1)


def BFS(adj, s=1):
    # 감염된 수 초기 설정
    count = 0
    # 탐색된 여부 기록
    parent = {s: None}
    frontier = deque([s])
    while frontier:
        v1 = frontier.popleft()
        for v2 in adj[v1]:
            if v2 not in parent:
                count += 1
                parent[v2] = v1
                frontier.append(v2)
    return count

print(BFS(adj, 1))