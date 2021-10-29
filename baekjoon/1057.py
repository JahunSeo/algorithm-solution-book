import sys
n, a, b = tuple(map(int, sys.stdin.readline().split()))

count = 0
while a != b:
    a -= a//2
    b -= b//2
    count += 1
print(count)
