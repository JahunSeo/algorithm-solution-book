import sys

sys.stdin = open("./baekjoon/testcase.txt")
N = int(sys.stdin.readline())

costs = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    costs.append(row)

def print_matrix(m):
    for r in m:
        print(r)
    print("")

# 1단계: 부분 문제 정의
# - 각 시점이 처할 수 있는 상태 S(i) = i번째로 방문 가능한 도시의 수 x 남은 도시의 구성
# - 가령, A를 출발해 {B,C,D,E}를 방문한다고 할 때
#   1번째 도시로 B를 방문하면, 남는 도시는 {C,D,E}
#   2번째 도시로 B를 방문하면, 남는 도시는 {D,E}, {C,E}, {C,D} 중 하나의 경우
#                        (각각 1번째로 C,D,E를 방문한 뒤, 2번째로 B를 방문한 경우)       
# - 결과적으로, 각 시점 i의 상태 개수 S(i)는
#   (출발지를 제외한 도시 개수 N-1) x (본인까지 제외한 N-2개 중 남은 도시 N-1-i개를 선택하는 경우의 수) 
# - 부분 문제의 개수 = sum(N * S(i) for i in range(1, N))

# 2단계: 메모 테이블 구성
# - 각 부문 문제의 정답을 저장할 메모 테이블 구성
# - 각 시점마다 S의 개수가 달라 난해함
# - 하지만 남은 도시의 구성은 도시 방문 여부를 0,1로 표시한 tuple로 표현 가능하고, 이를 일반화하면 2^(N-1)개임
# - 즉, B,C,D,E 중 C,D가 남았다면 (0,1,1,0)이며 이는 0~15 중 6에 해당함
# - 그러므로 S(i)는 (N-1) * (2^(N-1))개 중 하나의 상태로 표현 가능함
start = 0
cities = [c for c in range(1, N)]
print(cities)
# memo[time][city_to_visit][id_of_rest_cities]
# - 편의를 위해 0번째 시간, 0번째 도시 추가
memo = []
for i in range(0, N):
    timeline = []
    for c in range(0, N):
        timeline.append([0] * (2**N))
    memo.append(timeline)


# 메모는 마지막 도시 방문부터 시작
for c in cities:
    id_of_rest = 0 # 남은 도시가 없으므로 (A,B,C,D,E) = (0,0,0,0,0) = 0
    memo[N-1][c][id_of_rest] = costs[c][start]
print_matrix(memo[-1])

# 3단계: 부분 문제의 선후관계에 맞게 부분 문제 해결 
# - 이제 비트마스크를 사용해야하는 타이밍..