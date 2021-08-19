def get_dist(p1, p2):
    dx, dy = p1[0] - p2[0], p1[1] - p2[1]
    return  dx * dx + dy * dy

def bruteforce(start, end):
    global P, Q
    min_dist = float("inf")
    for i in range(start, end+1):
        for j in range(i+1, end+1):
            dist = get_dist(P[i], P[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def find_closest(start, end):
    global P, Q
    # 베이스 케이스: 3개보다 작으면 단순 계산
    if start >= end:
        return float("inf")
    if end - start + 1 <= 3:
        return bruteforce(start, end)
    
    # 1단계: 좌우 영역으로 분리하여 최소 거리 계산
    mid = (start + end) // 2
    mid_point = P[mid]
    left_min = find_closest(start, mid)
    right_min = find_closest(mid+1, end)
    # 현재 시점 최소 거리며, strip을 생성하는 기준
    d = min(left_min, right_min) 
    
    # 2단계: 가운데 점의 x 좌표 기준으로 탐색할 대상 strip 찾기
    #  - 이 때, y 좌표를 기준으로 이미 정렬되어 있는 Q에서 찾아
    #  - strip을 y를 기준으로 졍렬된 상태로 만듦
    strip = []    
    for point in Q:
        dx = point[0] - mid_point[0]
        if dx * dx <= d:
            strip.append(point)
    print("strip", d, mid_point, strip)

    # 3단계: strip 중에서 최소 거리 찾기
    #  - y를 기준으로 정렬된 상태이므로, y 좌표 거리가 d 이상인 경우 탐색 대상에서 제외
    min_dist = d
    for i in range(len(strip)):
        p1 = strip[i]
        for j in range(i+1, len(strip)):
            p2 = strip[j]
            # 두 점 간 y 좌표의 거리가 d 이상인 경우, 다음 p1으로 이동 
            # (비교 시, 거리는 제곱되어 있으므로 y좌표 차이도 제곱 필요)
            dy = p2[1] - p1[1]
            print(p1, p2, dy**2)

            if dy * dy >= min_dist: 
                break
            dist = get_dist(p1, p2)
            print("dist", dist, min_dist)
            if dist < min_dist:
                min_dist = dist

    return min_dist


import sys
sys.stdin=open("2261_test_1.txt","r")
N = int(sys.stdin.readline())
points = []
for _ in range(N):
    point = tuple(map(int, sys.stdin.readline().split()))
    points.append(point)
    print(point)

P = sorted(points, key=lambda p: p[0])
Q = sorted(points, key=lambda p: p[1])

print(P)
print(Q)

print(find_closest(0, len(P)-1))
