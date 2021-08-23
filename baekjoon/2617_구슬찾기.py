import sys
from collections import defaultdict
sys.stdin = open("./baekjoon/testcase.txt")

N, M = tuple(map(int, sys.stdin.readline().split()))

# 1단계: 정방향 인접 리스트와 역방향 인접 리스트를 각각 생성
adj_f = defaultdict(list) # forward
adj_b = defaultdict(list) # backward
for _ in range(M):
    v1, v2 = tuple(map(int, sys.stdin.readline().split()))
    adj_f[v1].append(v2)
    adj_b[v2].append(v1)

# print(adj_f)
# print(adj_b)

# 2단계: DFS 함수 생성
def DFS_visit(adj, v1, parent, results):
    if v1 in adj:
        for v2 in adj[v1]:
            if v2 not in parent:
                parent[v2] = v1
                DFS_visit(adj, v2, parent, results)
    results.append(v1)

answers = set()
# 각 vertex를 시작점으로 했을 때, 해당 vertex의 자손들의 수를 셈
for v1 in range(1, N+1):
    # 정순 방향
    parent, results = {}, []
    parent[v1] = None
    DFS_visit(adj_f, v1, parent, results)
    # print(v1, results)
    # 본인을 제외한 자손들의 수 확인
    # - 본인 제외 자손들의 수가 (N+1)//2 이상이면 본인은 가운데에 올 수 없음
    # - 가령, 구슬이 5개일 때, 자손이 3개 이상이면 본인의 인덱스는 중간인 2보다 커짐
    if len(results)-1 >= (N+1)//2:
        answers.add(v1)
        continue
    # 역순 방향
    parent, results = {}, []
    parent[v1] = None
    DFS_visit(adj_b, v1, parent, results)
    # print(v1, results)
    if len(results)-1 >= (N+1)//2:
        answers.add(v1)

print(len(answers))