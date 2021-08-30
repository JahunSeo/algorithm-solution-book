import sys
import heapq

sys.stdin = open("./baekjoon/testcase.txt")
N, K = tuple(map(int, sys.stdin.readline().split()))
items = list(map(int, sys.stdin.readline().split()))

where = {}
updated = []
for idx in range(K):
    item = items[idx]
    if item in where:
        prev_idx = where[item]
        updated[prev_idx][1] = idx
    where[item] = idx
    updated.append([item, float("inf")])

# print(updated)

count = 0        
current = []    
for item, next_loc in updated:
    # print(item, next_loc, current)
    # 이미 콘센트에 있는 경우
    # - 주의! 최신값으로 업데이트해주어야 함
    used = False
    for j in range(len(current)):
        _, c = current[j]
        if c == item:
            used = True
            current[j][0] = -next_loc
            heapq.heapify(current)
            break
    if used:
        continue
    # 콘센트에 자리가 남는 경우
    if len(current) < N:
        heapq.heappush(current, [-next_loc, item])
        continue
    # 콘센트에서 뽑아야 하는 경우
    deleted = heapq.heappop(current)
    # print("  pop",  deleted)
    heapq.heappush(current, [-next_loc, item])
    count += 1

print(count)