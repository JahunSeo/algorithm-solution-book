import sys
import heapq
sys.stdin = open("./baekjoon/testcase.txt")

class Node(object):
    def __init__(self, val:int):
        self.val = val
        self.absval = abs(val)

    def __repr__(self):
        return str(self.val)
    
    def __lt__(self, other):
        if self.absval == other.absval:
            return self.val < other.val
        else:
            return self.absval < other.absval


n = int(sys.stdin.readline())

heap = []
for i in range(n):
    v = int(sys.stdin.readline())
    if v != 0:
        heapq.heappush(heap, Node(v))
    elif len(heap) > 0:
        t = heapq.heappop(heap)
        print(t)
    else:
        print(0)