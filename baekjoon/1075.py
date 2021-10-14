import sys
n, f = tuple(map(int, sys.stdin.readline().split()))
ren = n - (n % 100)
ans = 0
for i in range(100):
    if (ren + i) % f == 0:
        ans = i 
        break

if ans < 10:
    print(f"0{ans}")
else:
    print(ans)