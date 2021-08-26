import sys 
N = int(sys.stdin.readline())

# memo = {}
# def f(n):
#     if n in memo:
#         return memo[n]
#     if n == 1:
#         # 1
#         return 1
#     if n == 2:
#         # 11 00 
#         return 2
#     memo[n] = (f(n-2) + f(n-1)) % 15746
#     return memo[n]

# print(f(N))

memo = {}
for i in range(1, N+1):
    if i <= 2:
        memo[i] = i
    else:
        memo[i] = (memo[i-2] + memo[i-1]) % 15746

print(memo[N])