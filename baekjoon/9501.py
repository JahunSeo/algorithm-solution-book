import sys
sys.stdin = open("./baekjoon/testcase.txt")
T = int(sys.stdin.readline())

for _ in range(T):
    n, dist = tuple(map(int, sys.stdin.readline().split()))
    count = 0
    for i in range(n):
        ship = tuple(map(int, sys.stdin.readline().split()))
        count += int(dist * ship[2] <= ship[0] * ship[1])
    print(count)