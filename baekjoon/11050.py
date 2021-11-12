import sys
n, k = tuple(map(int, sys.stdin.readline().split()))

a, b, c = 1, 1, 1
total = 1
for i in range(1, n+1):
    total *= i
    if i == k:
        a = total
    if i == n-k:
        b = total
    if i == n:
        c = total

print(int(c / (a * b)))