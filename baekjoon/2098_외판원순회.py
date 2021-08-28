import sys

sys.stdin = open("./baekjoon/testcase.txt")
N = int(sys.stdin.readline())

matrix = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

print(matrix)

