import sys
from collections import defaultdict, deque

sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 1단계: 인접 리스트 및 진입 차수 만들기
# - 인접 리스트: 각 하위 부품이 어떤 상위 부품을 만드는데 쓰이는지와 필요한 개수를 함께 저장
# - 진입 차수: 각 상위 부품을 만드는데 필요한 하위 부품들의 종류 개수를 진입 차수에 저장
adj = defaultdict(list)
in_deg = [0] * (N+1) # 부품(정점)이 1부터 시작하므로 편의상 길이를 N+1로 함
for _ in range(M):
    v2, v1, k = tuple(map(int, sys.stdin.readline().split()))
    # 하위 부품 v1이 상위 부품 v2을 만드는데 k개가 필요
    adj[v1].append((v2, k))
    # 상위 부품 v2의 진입 차수 업데이트
    in_deg[v2] += 1

# 2단계: 진입 차수가 0인 항목들로 큐 구성
# - 이 때, 진입 차수가 0인 항목은 기본 부품이므로, 별도로 기록 
queue = []
for i in range(1, N+1):
    if in_deg[i] == 0:
        queue.append(i)
base_items = queue[:]
queue = deque(queue)

# 3단계: 기본 부품부터 완제품까지 순차적으로 각각이 필요한 하위 부품의 개수 누적
components = [ [0]*(N+1) for _ in range(N+1)  ]
results = []
while queue:
    # 하위 부품 v1을 그래프에서 제거
    v1 = queue.popleft()
    results.append(v1)
    # v1을 필요로 하는 상위 부품 v2 각각에 대하여
    for v2, k in adj[v1]:
        # 가중치 누적
        # v1이 기본 부품인 경우
        if v1 in base_items:
            components[v2][v1] = k
        # v1이 중간 부품인 경우
        else: 
            # v1을 만드는데 필요한 기본 부품 v0 각각을 k배 하여 v2에 추가
            for v0, count in enumerate(components[v1]):
                components[v2][v0] += count * k
        # 진입 차수 1 감소
        in_deg[v2] -= 1
        # 진입 차수가 0이 된 정점은 큐에 추가
        if in_deg[v2] == 0:
            queue.append(v2)


for i in range(1, N+1):
    count = components[N][i]
    if count != 0:
        print(i, count)