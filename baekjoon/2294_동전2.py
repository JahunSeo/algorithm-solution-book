import sys
from collections import deque
sys.stdin = open("./baekjoon/testcase.txt")

N, K = tuple(map(int, sys.stdin.readline().split()))
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
# 작은 값부터 확인 가능하도록 오름차순 정렬
coins.sort()

# 초기값 설정
# 동전들 중 목표 금액과 일치하는 값이 있는지 확인하여 조기 종료
if K in coins:
    min_count = 1
    frontier = []
else:
    min_count = -1
    frontier = deque([(K, 0)])

# 하위 문제로 분할 및 기록 누적하기
# - 너비 우선 탐색 과정에서 이미 지나간 숫자가 나중에 다시 등장하는 경우,
# - 해당 숫자까지 도달하는데까지의 누적 동전 수는 크고 남은 경로는 동일할 것이기 때문에
# - 결국 누적 동전 수가 최소가 될 수 없으며, 추가 탐색할 필요가 없음
parent = {K: None}
while min_count < 0 and frontier:
    # 남은 금액 v1, 누적 동전 수 cnt1
    v1, cnt1 = frontier.popleft()
    # 사용 가능한 동전들 하나씩 확인
    for coin in coins:
        # 남은 금액에서 동전 값만큼 빼서 새로운 값 구성
        # 누적 동전 수에 1 추가
        v2, cnt2 = v1 - coin, cnt1 + 1
        # 이미 탐색한 금액인 경우, 다음 동전으로 이동
        if v2 in parent:
            continue
        # 남은 금액이 음수인 경우, 다음 동전도 확인할 필요 없으므로 종료
        if v2 < 0:
            break
        # 남은 금액이 0인 경우, 조합 완성이며 다음 동전은 음수가 나올 것이므로 종료
        elif v2 == 0:
            min_count = cnt2
            break
        # 남은 금액이 양수인 경우, 추가 분할을 위해 큐에 추가
        else:
            # 중복 탐색을 막기 위해 parent에 추가
            parent[v2] = v1
            frontier.append((v2, cnt2))

print(min_count)