import sys
sys.stdin = open("./baekjoon/testcase.txt")
n = int(sys.stdin.readline())
results = []
# loop results
for i in range(0, n):
    curpoint = tuple(map(int, sys.stdin.readline().split()))
    results.append(curpoint)

results.sort(key=lambda x: (x[0], x[1]))    
    
for x, y in results:
    print(x, y)