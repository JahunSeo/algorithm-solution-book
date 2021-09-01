import sys
sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))

print(N, values)

# [반례] 모든 값이 음수가 나오는 상황 주의하기
max_value = float("-inf")

for i in range(N):
    for prev in range(0, i+1):
        if i != prev:
            values[prev] = values[prev] + values[i]
        max_value = max(max_value, values[prev])

print(max_value)