import sys
cnta = int(sys.stdin.readline())
seqa = list(map(int, sys.stdin.readline().split()))
cntb = int(sys.stdin.readline())
seqb = list(map(int, sys.stdin.readline().split()))

seqa.sort()

def find(seq, num):
    start, end = 0, len(seq)-1
    while start <= end:
        mid = (start+end)//2
        midv = seq[mid]
        if midv == num:
            return 1
        elif num < midv:
            end = mid - 1
        else:
            start = mid + 1
    return 0

ans = [find(seqa, num) for num in seqb]
print(" ".join(map(str, ans)))