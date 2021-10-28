import sys
n = int(sys.stdin.readline())

scores = [0] * (n+1)
scores[1], scores[2] = 1, 2
for i in range(3, n+1):
    scores[i] = (scores[i-1] + scores[i-2]) % 10007

print(scores[n])