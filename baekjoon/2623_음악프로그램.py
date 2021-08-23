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

# 2단계: 진입 차수가 0인 정점으로 큐 초기화
queue = deque()
for v in range(1, N+1):
    if in_deg[v] == 0:
        queue.append(v)
# print("큐 시작 :", queue)

# 3단계: 진입 차수가 0인 정점들을 하나씩 정리
# - 진입 차수가 0인 정점 v1을 빼면서 v1에서 출발하는 간선들을 제거
answers = []
while queue:
    v1 = queue.popleft()
    answers.append(v1)
    # v1에서 출발하는 간선들을 제거 (도착 정점 v2의 진입 차수에서 1씩 감소)
    for v2 in adj[v1]:
        in_deg[v2] -= 1
        # 진입 차수가 0이 되면 큐에 추가
        if in_deg[v2] == 0:
            queue.append(v2)

# 4단계: 순환 그래프인지 여부 확인
# - 탐색을 마친 뒤 모든 정점이 정리되지 않았다는 것은, 간선이 남은 정점이 있음을 의미
# - 간선이 남은 정점이 있다는 것은 순환이 존재했음을 의미!
if len(answers) == N:
    for singer in answers:
        print(singer)
else: 
    print(0)

