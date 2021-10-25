import sys
from collections import defaultdict
sys.stdin = open("./baekjoon/testcase.txt")

n = int(sys.stdin.readline())

# 본인을 목적지로 들어오는 라인의 수
cost = {}
# 본인이 출발지로 뻗어나가는 라인들 정리
adj = defaultdict(list)
for i in range(1, n+1):
    line = tuple(map(int, sys.stdin.readline().split()))
    cost[i] = line[0]
    for j in range(1, len(line)-1):    
        adj[i].append(line[j])

# print(cost)
# print(adj)

scores = [0] * (n+1)
def solve(num):
    global scores
    if scores[num]:
        return scores[num]
    
    total = 0
    for v in adj[num]:
        total = max(total, solve(v))
    total += cost[num]
    scores[num] = total
    return total

for i in range(1, n+1):
    solve(i)


# print(scores) 

for i in range(1, n+1):
    print(scores[i])