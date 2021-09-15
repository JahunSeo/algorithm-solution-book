import sys
sys.stdin = open("./baekjoon/testcase.txt")
K = int(sys.stdin.readline())

A, B = [1], [2]
results = A + B

while len(results) < K:
    new_B = [(a<<2) + 1 for a in A] + [b<<1 for b in B]
    new_B.sort()
    results += new_B
    A, B = B, new_B
    # print(K, results)

print(results[K-1])
