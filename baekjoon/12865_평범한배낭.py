import sys

sys.stdin = open("./baekjoon/testcase.txt")

N, K = tuple(map(int, sys.stdin.readline().split()))
# print(N, K)
items = []
for _ in range(N):
    w, value = tuple(map(int, sys.stdin.readline().split()))
    items.append((w, value))
items.sort()
print(items)

# 만들 수 있는 전체 경우의 수는 2^N
# nC0 + nC1 + nC2 + ... + nCn

candidates = [(0,0)]
max_value = 0
for w1, value1 in items:
    new_candidates = candidates[:]
    for w2, value2 in candidates:
        new_w = w1 + w2
        new_value = value1 + value2
        if new_w <= K:
            new_candidates.append((new_w, new_value))
            max_value = max(max_value, new_value)
    candidates = new_candidates
    print((w1, value1), K, max_value, new_candidates)

print(max_value)