import sys

N = int(sys.stdin.readline())

scores = [0]*(N+1)
for i in range(N+1):
    if i <= 2:
        scores[i] = 1
    else:
        scores[i] = scores[i-1] + scores[i-2]

print(scores[N])