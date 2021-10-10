import sys
acnt, bcnt = tuple(map(int, sys.stdin.readline().split()))

aseq = list(map(int, sys.stdin.readline().split()))
bseq = list(map(int, sys.stdin.readline().split()))

infv = 10**9+1
aseq.append(infv)
bseq.append(infv)

final = []
aidx, bidx = 0, 0
while aidx < acnt or bidx < bcnt:
    av, bv = aseq[aidx], bseq[bidx]
    if av < bv:
        final.append(av)
        aidx += 1
    else:
        final.append(bv)
        bidx += 1

print(" ".join(map(str, final)))
