import sys

# sys.stdin = open("./baekjoon/testcase.txt")
n, k = tuple(map(int, sys.stdin.readline().split()))
lines = [int(sys.stdin.readline()) for _ in range(n)]

start = 1         # min_candidate
end = max(lines)  # max_candidate
ans = start       # init with min_candidate because we want to find maximum possible value

while start <= end:
    mid = (start + end) // 2
    # print(start, end, mid, ans)
    count = sum([a // mid for a in lines])
    if count >= k:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)