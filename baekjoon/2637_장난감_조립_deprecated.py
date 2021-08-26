import sys
from collections import defaultdict, deque

sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 1단계: 각 부품 별로 필요한 하위 부품을 파악
# - 각 상위 부품을 만드는 데 필요한 하위 부품을 필요한 개수 만큼 배열에 저장
# - 가령, {상위: [(하위1, 2), (하위2, 3), (하위3, 1)]}
# - 이 때, adj에 key로 등록되지 않은 부품은 더 이상 분리될 수 없는 기본 부품을 의미
adj = defaultdict(list)
for _ in range(M):
    x, y, k = tuple(map(int, sys.stdin.readline().split()))
    # x를 만드는데 하위 부품 y가 필요한 개수만큼 인접 리스트에 추가
    adj[x].append((y, k))

# 2단계: 최종 제품을 만들기 위해 필요한 기본 부품 세기
# 누적된 기본 부품을 세는 dict 초기화
subitems = defaultdict(int)
# 최종 제품으로 frontier 초기화 (DFS를 위해 스택으로 변경)
s = N
frontier = [(s, 1)]
storage = {}

def DFS_visit(v1):
    if v1 in storage:
        return storage[v1]
    v1_sub = defaultdict(int)
    for v2, k2 in adj[v1]:
        if v2 not in adj:
            v1_sub[v2] += k2
        else:
            v2_sub = DFS_visit(v2)
            for v3, k3 in v2_sub.items():
                v1_sub[v3] += k2*k3
    storage[v1] = v1_sub
    return v1_sub

DFS_visit(s)

for i in range(1, N+1):
    if i in storage[s]:
        print(i, storage[s][i])
