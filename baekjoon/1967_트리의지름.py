import sys
from collections import defaultdict

sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
adj = defaultdict(list)

for _ in range(N-1):
    v1, v2, k = tuple(map(int, sys.stdin.readline().split()))
    adj[v1].append((v2, k))


s = 1

max_score = 0
def DFS_visit(v1):
    global max_score
    score = 0
    max_childsum = 0
    for v2, k in adj[v1]:
        childsum = DFS_visit(v2) + k
        score += childsum
        max_childsum = max(max_childsum, childsum)

    print(v1, score)
    max_score = max(max_score, score)
    return max_childsum

DFS_visit(s)
print(max_score)