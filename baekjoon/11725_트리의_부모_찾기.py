import sys
from collections import deque, defaultdict
sys.stdin = open("./baekjoon/testcase.txt", "r")

N = int(sys.stdin.readline())

adj = defaultdict(list)
for _ in range(N-1):
    v1, v2 = tuple(map(int, sys.stdin.readline().split()))
    adj[v1].append(v2)
    adj[v2].append(v1)

s = 1
parent = {s: None}

def DFS_visit(v1):
    for v2 in adj[v1]:
        if v2 not in parent:
            parent[v2] = v1
            DFS_visit(v2)

DFS_visit(s)

# def BFS(s):
#     global parent
#     frontier = deque([s])
#     while frontier:
#         v1 = frontier.popleft()
#         for v2 in adj[v1]:
#             if v2 not in parent:
#                 parent[v2] = v1
#                 frontier.append(v2)

# BFS(s)

for i in range(2, N+1):
    print(parent[i])
