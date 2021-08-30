import sys
sys.stdin = open("./baekjoon/testcase.txt")

N, K = tuple(map(int, sys.stdin.readline().split()))

coins = []
for _ in range(N):
    coin = int(sys.stdin.readline())
    if coin <= K:
        coins.append(coin)
coins.sort()

# print(N, K, coins)

count = 0
while K > 0:
    coin = coins.pop()
    used, K = K//coin, K%coin
    count += used

print(count)