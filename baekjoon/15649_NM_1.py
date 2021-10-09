import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

def permute(seq, length):
    def fn(active, rest, results=[]):
        # if not rest:
        #     results.append(active)
        if len(active) == length:
            results.append(active)
        else:
            for i in range(len(rest)):
                fn(active + [rest[i]], rest[:i] + rest[i+1:], results)
        return results
    return fn([], seq, [])

seq = list(map(str, range(1, n+1)))
results = permute(seq, m)
results.sort()
for r in results:
    ans = " ".join(r)
    print(ans)
