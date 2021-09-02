import sys
sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())

steps = []
for _ in range(N):
    s = int(sys.stdin.readline())
    steps.append(s)

# 1단계: 부분문제 정의하기

# 2단계: 메모 테이블 구성하기
memo = [[0,0] for _ in range(N)]

# 1번째 계단의 False (이전 계단을 밟지 않은 경우)
memo[0][0] = steps[0]
# 2번째 계단 처리
if N >=2 :
    memo[1][0] = steps[1]
    memo[1][1] = memo[0][0] + steps[1]

for i in range(2, N):
    # False 처리
    memo[i][0] = max(memo[i-2]) + steps[i]
    # True 처리
    memo[i][1] = max(memo[i-1][0], memo[i-2][0], memo[i-2][1]) + steps[i]

# print(memo)
print(max(memo[-1]))