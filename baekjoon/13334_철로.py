# https://www.acmicpc.net/problem/13334

import heapq
import sys

def search(routes, d):
    """
    1단계. 경로 정렬
     - 각 경로를 시작점, 끝점 순으로 정렬
     - 전체 경로를 끝점, 시작점 기준으로 정렬 (끝점 오름차순, 시작점 오름차순)
    2단계. 각 경로들의 끝점을 기준으로 탐색
     1) 탐색 조건
       - 탐색 조건 1(끝점 조건): 경로_끝점 <= 철로_끝점
       - 탐색 조건 2(시작점 조건): 경로_시작점 >= 철로_시작점
     2) 끝점이 작은 경로부터 탐색하는 이유
       - 끝점이 오름차순으로 정렬되어 있어, 경로1_끝점 <= 경로2_끝점 이므로
       - 경로2_끝점 <= 철로_끝점이면, 경로1_끝점 <= 철로_끝점
       - 다시 말해 끝점이 작은 경로부터 탐색하여 누적된 경로들은 
       - 다음 경로의 끝점을 기준으로 탐색 시 끝점 조건을 무조건 충족하기 때문에,
       - 시작점 조건의 충족 여부만 확인하면 됨
     3) 시작점 조건을 충족하지 못한 경로를 탐색 범위에서 제외 가능한 이유
       - 경로의 끝점을 기준으로 철로의 끝점이 이동할 때, 철로의 시작점 또한 계속 커짐
       - 이에 따라 이번 경로의 시작점 조건을 통과 못하면, 다음 경로의 시작점 조건도 통과 못함
       - 그러므로 탐색 범위에서 제외 가능
     4) 시작점 조건 충족 여부 판단을 위해 우선순위 큐 활용
       - 각 탐색 회차에서 시작점 조건을 충족한 경로들을 시작점을 기준으로 최소 우선순위 큐에 누적
       - 다음 탐색 회차에서 다시 시작점 조건 충족 여부를 판단하는데,
       - 큐는 시작점이 가장 낮은, 즉 철로의 끝점과 가장 먼 위치부터 제시해주며,
       - 시작점 조건을 충족한 경로를 찾으면 남은 경로들은 모두 충족할 것이므로 탐색 종료
    """
    # 경로 정렬
    # 각 경로를 시작점, 끝점 순으로 정렬
    routes = [sorted(tuple(map(int, r.split()))) for r in routes]
    # 전체 경로를 끝점, 시작점 기준으로 정렬 (끝점 오름차순, 시작점 오름차순) 
    routes.sort(key=lambda r: (r[1], r[0]))
    
    # 정답 초기화
    max_count = 0
    # 우선순위 큐 생성
    queue = []
    for route in routes:
        r_start, r_end = route
        d_start, d_end = r_end - d, r_end
        # 본인 또한 조건 충족 여부를 확인해야 하므로 queue에 추가
        heapq.heappush(queue, route)
        while queue:
            prev = heapq.heappop(queue)
            p_start, p_end = prev
            # 이전 경로가 d에 포함되는지 확인
            if d_start <= p_start:
                # 우선순위 큐에서 시작점이 최소인 경로가 d에 포함되면 
                # 큐의 남은 경로들도 모두 d에 포함되므로
                # 이전 경로 다시 추가 후 큐 탐색 종료
                heapq.heappush(queue, prev)
                break
        count = len(queue)
        if max_count < count:
            max_count = count
    return max_count

N = int(sys.stdin.readline())
routes = []
for _ in range(N):
    routes.append(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline())

print(search(routes, d))