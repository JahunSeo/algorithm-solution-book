import sys
from collections import deque
sys.stdin = open("./baekjoon/testcase.txt")

N, K = tuple(map(int, sys.stdin.readline().split()))

def BFS(s):
    parent = {s} # set   
    frontier = deque([(s, 0)])
    while frontier:
        v1, time1 = frontier.popleft()
        # 한 노드에서 이동할 수 있는 경우 3가지
        for v2 in [v1*2,v1+1,v1-1]:
            time2 = time1+1
            # 이동 불가능한 지점인지 확인
            if v1 <=0:
                continue
            # 이미 방문한 위치인지 확인
            if v2 in parent:
                continue
            # 새로운 위치인 경우, 우선 목표 지점인지 확인
            if v2 == K:
                print("find", v2, v1)
                return time2
            # 새로운 위치이지만 목표 지점이 아닌 경우
            # 새로운 탐색 대상인지 판단
            # if v2 > K*2:
            #     continue
            # 새로운 탐색 대상으로 판단될 경우
            print("new", v2, v1, frontier)
            parent.add(v2)
            frontier.append((v2, time2))
    return False

s = N
if s == K:
    print(0)
else:
    time = BFS(s)
    print(time)