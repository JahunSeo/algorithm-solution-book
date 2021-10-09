import sys
import heapq
n, k = tuple(map(int, sys.stdin.readline().split()))

# 입력값 받기
stones = []
for _ in range(n):
    m, v = tuple(map(int, sys.stdin.readline().split()))
    stones.append((m, v))
bags = []
for _ in range(k):
    c = int(sys.stdin.readline())
    bags.append(c)

# 보석 무게 순으로 정렬하기
stones.sort()
# 가방 크기 순으로 정렬하기
bags.sort()
# print(stones, bags)

# 각 가방에 들어갈 수 있는 보석들을 확인 
# 이 때, 해당 가방에 들어갈 수 있는 보석의 최대 가치를 heap으로 관리
total = 0
bidx = 0 # 가방 
sidx = 0 # 보석
heap = []
while bidx < len(bags) and sidx < len(stones):
        bag = bags[bidx]
        (m, v) = stones[sidx]
        # print("stone bag", m, v, bag, total, heap)
        # 보석이 가방에 들어가는 경우
        if m <= bag:
            heapq.heappush(heap, -v)
            sidx += 1            
        # 보석이 가방에 들어가지 않는 경우
        else:
            if len(heap) > 0:
                total += heapq.heappop(heap)
            bidx += 1
# 가방이 남은 경우            
while bidx < len(bags):
    if len(heap) > 0:
        total += heapq.heappop(heap)
    bidx += 1

print(-total)
