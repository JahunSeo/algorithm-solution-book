import sys
from collections import deque, defaultdict

sys.stdin = open("./baekjoon/testcase.txt")

N, M = tuple(map(int, sys.stdin.readline().split()))

# 1단계: 인접 리스트와 진입 차수 파악하기
adj = defaultdict(list)
in_deg = [0] * (N + 1) # 정점이 1부터 시작하므로 편의를 위해 길이를 N+1로 설정
for _ in range(M):
    singers = list(map(int, sys.stdin.readline().split()))[1:]
    for i in range(len(singers)-1):
        v1, v2 = singers[i], singers[i+1]
        adj[v1].append(v2)
        in_deg[v2] += 1
# print("인접 리스트 :", adj)
# print("진입 차수 :", in_deg)

# 2단계: 깊이 우선 탐색 함수 구현하기
def DFS_visit(adj, v1, visited, stack):
    # v1가 이미 탐색 완료 항목에 있는 경우, 추가 탐색 불필요
    if v1 in visited:
        return True
    # v1가 이미 스택에 있는 경우, 조상에 해당하므로 순환 그래프임
    if v1 in stack:
        return False
    # 탐색 시작 시점에 스택에 v1 추가
    stack.append(v1)
    # 다음 depth의 정점들을 탐색 
    if v1 in adj:
        for v2 in adj[v1]:
            # 앞선 탐색에서 순환이 발생했는지 확인
            if not DFS_visit(adj, v2, visited, stack):
                return False
    # 탐색 종료 시점에 스택에서 v1 제거
    stack.pop()
    # 탐색 완료 항목에 v1 추가
    visited.append(v1)
    return True

# 3단계: 탐색 실시
visited = [] # 정점들이 탐색이 종료된 순서대로 추가됨
stack = [] # 새로운 정점의 탐색을 시작할 때 스택에 추가하고 탐색 종료 시 스택에서 제거
for v1 in range(1, N+1):
    # 순환이 발생하면 탐색 종료
    if not DFS_visit(adj, v1, visited, stack):
        break
# 역순으로 정렬
visited.reverse()    

# 4단계: 순환 그래프인지 여부 확인
# - 탐색을 마친 뒤 모든 정점이 정리되지 않았다는 것은, 간선이 남은 정점이 있음을 의미
# - 간선이 남은 정점이 있다는 것은 순환이 존재했음을 의미!
if len(visited) == N:
    for singer in visited:
        print(singer)
else: 
    print(0)

