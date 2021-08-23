import sys
from collections import defaultdict
sys.stdin = open("./baekjoon/testcase.txt")

N, M = tuple(map(int, sys.stdin.readline().split()))
print(N,M)

# 1단계: 정방향 인접 리스트와 역방향 인접 리스트를 각각 생성
adj_f = defaultdict(list) # forward
adj_b = defaultdict(list) # backward
for _ in range(M):
    v1, v2 = tuple(map(int, sys.stdin.readline().split()))
    adj_f[v1].append(v2)
    adj_b[v2].append(v1)

print(adj_f)
print(adj_b)

# 2단계: 위상정렬을 위한 DFS 함수 생성
def DFS(adj):
    parent = {}
    results = []
    for v1 in range(1, N+1):
        if v1 not in parent:
            parent[v1] = None
            DFS_visit(adj, v1, parent, results)
    # 위상정렬 절차를 명확히 하기 위해 탐색 마친 후 reverse
    # 하지만 이번 문제에서는 reverse를 하지 않더라도 풀 수 있음
    results.reverse()
    return results 
def DFS_visit(adj, v1, parent, results):
    if v1 in adj:
        for v2 in adj[v1]:
            if v2 not in parent:
                parent[v2] = v1
                DFS_visit(adj, v2, parent, results)
    results.append(v1)

# 3단계: 정방향과 역방향으로 각각 위상정렬
results_f = DFS(adj_f)
results_b = DFS(adj_b)

print("위상정렬 결과")
print(results_f)
print(results_b)

# 4단계: 각 vertex의 위치 확인
counter_f = [None] * N
counter_b = [None] * N 
for idx, v in enumerate(results_f):
    print(v, idx)
    counter_f[v-1] = idx
for idx, v in enumerate(results_b):
    counter_b[v-1] = idx

print("본인보다 앞에 있는 개수")
print(counter_f)
print(counter_b)