import sys
sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))

# print(N, values)


memo = {}
def solve(i, j):
    if i==j:
        return values[i]
    k = (i+j)//2
    max_left, left = 0, 0
    for p in range(k, -1, -1):
        left += values[p]
        max_left = max(max_left, left)
    max_right, right = 0, 0
    for q in range(k+1, len(values)):
        right += values[q]
        max_right = max(max_right, right)
    
    first = solve(i, k)
    second = solve(k+1, j)
    third = max_left + max_right
    
    memo[(i, j)] = max(first, second, third)
    # print((i, j), memo[(i,j)], first, second, third)

    return memo[(i, j)]

print(solve(0, len(values)-1))