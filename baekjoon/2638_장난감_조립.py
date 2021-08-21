import sys
from collections import defaultdict, deque

sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 1단계: 각 부품 별로 필요한 하위 부품을 파악
# - 각 상위 부품을 만드는 데 필요한 하위 부품을 필요한 개수 만큼 배열에 저장
# - 가령, {상위: [하위1, 하위1, 하위2, 하위2, 하위2, 하위3 ]}
# - 이 때, adj에 key로 등록되지 않은 부품은 더 이상 분리될 수 없는 기본 부품을 의미
adj = defaultdict(list)
for _ in range(M):
    x, y, k = tuple(map(int, sys.stdin.readline().split()))
    # x를 만드는데 하위 부품 y가 필요한 개수만큼 인접 리스트에 추가
    for _ in range(k):
        adj[x].append(y)

# 누적된 기본 부품을 세는 dict 초기화
subitems = defaultdict(int)

s = N
frontier = deque(adj[s])
while frontier:
    v1 = frontier.popleft()
    # v1이 인접 리스트에 없는 경우, 기본 부품임으로 더 이상 분리 불가
    if v1 not in adj:
        # 기본 부품 개수에 누적 후 다음 아이템으로 넘어감
        subitems[v1] += 1
        continue
    # v1이 인접 리스트에 있는 경우, 하위 부품으로 분리해주어야 함
    # v1의 모든 하위 부품을 frontier에 추가
    for v2 in adj[v1]:
        frontier.append(v2)

# 누적된 기본 부품 개수 출력
for i in range(1, N+1):
    if i in subitems:
        print(i, subitems[i])

