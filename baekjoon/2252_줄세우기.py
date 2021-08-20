import sys
from collections import defaultdict

sys.stdin = open("./baekjoon/testcase.txt", "r")

N, M = tuple(map(int, sys.stdin.readline().split()))
# 인접 리스트 구성
adj = defaultdict(list)
for _ in range(M):
    v1, v2 = tuple(map(int, sys.stdin.readline().split()))
    # 주의: 단방향이므로 한 쪽만 저장! 
    adj[v1].append(v2)

# 초기 설정
# 탐색 시작점으로 인접 리스트 내에서 임의의 값으로 지정 (인접 리스트에 1이 없을 수 있음)
# DFS 함수 구성
results = []
parent = {}

def DFS():
    # 주의: 학생들 전체가 탐색 대상이 될 수 있도록 함
    for v1 in range(1, N+1):
        if v1 not in parent:
            parent[v1] = None
            DFS_visit(v1)

def DFS_visit(v1):
    ## v1에서 출발하는 edge가 있는지 확인 후 추가 탐색
    if v1 in adj:
        for v2 in adj[v1]:
            if v2 not in parent:
                parent[v2] = v1
                DFS_visit(v2)
    # v1의 탐색이 종료될 때마다 results에 추가
    results.append(v1)
# DFS 실행
DFS()
# results를 역순으로 구성
results.reverse()
# 출력
print(" ".join([str(c) for c in results]))
