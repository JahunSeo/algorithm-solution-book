import sys
n = int(sys.stdin.readline())
counter = {}
for v in sys.stdin.readline().split():
    if v in counter:
        counter[v] += 1
    else:
        counter[v] = 1

m = int(sys.stdin.readline())
ans = []
for v in sys.stdin.readline().split():
    if v in counter:
        ans.append(str(counter[v]))
    else:
        ans.append(str(0))

print(" ".join(ans))
