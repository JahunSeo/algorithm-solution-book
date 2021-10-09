import sys
sys.stdin = open("./baekjoon/testcase.txt")
K = int(sys.stdin.readline())

A, B = [1], [2]
count = 2

while count < K:
    new_B = [(a<<2) + 1 for a in A] + [b<<1 for b in B]
    new_B.sort()
    count += len(new_B)
    A, B = B, new_B
    print(K, count, B)

print(B[K-count-1])
