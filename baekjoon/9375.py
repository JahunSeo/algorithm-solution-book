import sys
sys.stdin = open("./baekjoon/testcase.txt")

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    counter = {}
    for __ in range(n):
        name, species = sys.stdin.readline().split()
        if species in counter:
            counter[species] += 1
        else:
            counter[species] = 1
    # print(counter)
    score = 1
    for k, v in counter.items():
        score *= (v + 1)
    print(score - 1)