import sys
import math
a, b = tuple(map(int, sys.stdin.readline().split()))
if a > b:
    tmp = b
    b = a
    a = tmp

sub = set()
P, Q = None, None
for i in range(1, int(math.sqrt(a))+1):
    print(a, i, a % i)
    if a % i == 0:
        sub.add(i)
        if b % (a//i) == 0:
            P = a//i
            break


if P == None:
    sub = list(sub)
    sub.sort(reverse=True)
    for n in sub:
        if b % n == 0:
            P = n
            break

Q = P * (a // P) * (b // P)
print(P)
print(Q)