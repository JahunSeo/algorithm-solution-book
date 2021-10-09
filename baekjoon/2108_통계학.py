import sys
from collections import Counter
sys.stdin = open("./baekjoon/testcase.txt")
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    v = int(sys.stdin.readline())
    arr.append(v)

arr.sort()
counted = Counter(arr)
dist = arr[-1] - arr[0]

mc = counted.most_common(1)[0]
modes = [k for k, v in counted.items() if v == mc[1]]
modes.sort()
if (len(modes) > 1):
    mc = modes[1]
else:
    mc = modes[0]

print(round(sum(arr)/n))
print(arr[n//2])
print(mc)
print(dist)