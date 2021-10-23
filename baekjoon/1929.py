import sys
import math
a, b = tuple(map(int, sys.stdin.readline().split()))

primes = [None] * (b+1)
primes[0] = 0
primes[1] = 0

for num in range(2, b+1):
    if primes[num] == None:
        primes[num] = 1
        # num의 배수들을 0으로 처리
        k = 2
        while num * k <= b:
            primes[num * k] = 0
            k += 1

for num in range(a, b+1):
    if primes[num]:
        print(num)