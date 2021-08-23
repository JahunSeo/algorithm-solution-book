import sys
sys.stdin = open("./baekjoon/testcase.txt")

N, M = tuple(map(int, sys.stdin.readline().split())) 
print(N, M)
matrix = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)
print(matrix)

