import sys
sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))

print(N, values)

# [반례] 모든 값이 음수가 나오는 상황 주의하기
memo = [[0] * N for _ in range(N)]
# 길이가 1인 상황 먼저 처리
max_value = float("-inf")
for i in range(N):
    memo[i][i] = values[i]
    max_value = max(max_value, memo[i][i])

for diag in range(1, N):
    for c in range(diag, N):
        r = c - diag
        memo[r][c] = memo[r][c-1] + memo[c][c]
        max_value = max(max_value, memo[r][c])

print(max_value)