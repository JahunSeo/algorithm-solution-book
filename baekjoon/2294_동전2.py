import sys
from collections import deque
sys.stdin = open("./baekjoon/testcase.txt")

N, K = tuple(map(int, sys.stdin.readline().split()))
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
# 작은 값부터 확인 가능하도록 오름차순 정렬
coins.sort()

# 사용 동전의 최대 개수 초기 설정
min_count = K 
# 동전들 중 목표 금액과 일치하는 값이 있는지 확인하여 조기 종료
if K in coins:
    min_count = 1
    frontier = []
else:
    # (목표 금액, 누적 동전 수)
    frontier = deque([(K, 0)])

# 동전 분할하기
# 분할 성공 여부 초기화
success = False
while frontier:
    # 남은 금액 v1, 누적 동전 수 cnt1
    v1, cnt1 = frontier.popleft()
    # 사용 가능한 동전들 하나씩 확인
    for coin in coins:
        # 남은 금액보다 동전 값이 크다면 분할 불가능하며, 다음 동전도 확인할 필요 없으므로 종료
        if coin > v1:
            break
        # 남은 금액보다 동전 값이 작거나 같으면 분할 
        # 남은 금액은 동전 값으로 나눈 나머지
        v2 = v1 % coin
        # 누적 동전 수는 남은 금액을 동전 값으로 나눈 몫을 기존 개수에 추가한 값
        cnt2 = cnt1 + v1//coin 
        # 만약 남은 금액이 없다면, 조합 완성
        if v2 == 0:
            success = True
            min_count = min(min_count, cnt2)
        # 남은 금액이 있다면, 추가 분할을 위해 큐에 추가
        else:
            frontier.append((v2, cnt2))

if success:
    print(min_count)
else:
    print(-1)