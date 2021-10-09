import sys
acnt, bcnt = tuple(map(int, sys.stdin.readline().split()))

if acnt < bcnt:
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
else:
    B = list(map(int, sys.stdin.readline().split()))
    A = list(map(int, sys.stdin.readline().split()))
        
A.sort()
B.sort()

def include(seq, num):
    start=0
    end=len(seq)-1
    while start <= end:
        mid = (start + end)//2
        if seq[mid] == num:
            return 1
        elif seq[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0

common = 0
for a in A:
    common += include(B, a)

print(acnt + bcnt - common)