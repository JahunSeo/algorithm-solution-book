import sys
N = int(sys.stdin.readline())

# 1. memoization DP 방식
# memo = {}
# def f(n):
#     if n in memo:
#         return memo[n]
#     if n <= 2:
#         return 1
#     memo[n] = f(n-1) + f(n-2)
#     return memo[n]

# print(f(N))

# 2. bottom-up DP 방식
fib = {}
for i in range(1, N+1):
    if i <= 2:
        fib[i] = 1
    else:
        fib[i] = fib[i-1] + fib[i-2]

print(fib[N])