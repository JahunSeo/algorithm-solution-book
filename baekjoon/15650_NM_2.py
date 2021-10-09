import sys
n, m = tuple(map(int, sys.stdin.readline().split()))

def combine(seq, length):
    def fn(active, rest, results=[]):
        # print("fn", active, rest, results)
        if len(active) == length:
            # print("hey", active)
            results.append(active)
        elif not len(rest):
            return
        else:
            fn(active + [rest[0]], rest[1:], results)
            fn(active, rest[1:], results)
        return results
    return fn([], seq)

seq = list(range(1, n+1))
results = combine(seq, m)
print(results)
for c in results:
    print(" ".join(sorted(list(map(str, c)))))
    