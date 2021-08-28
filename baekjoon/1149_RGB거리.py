import sys
sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
costs = []
for _ in range(N):
    cost = tuple(map(int, sys.stdin.readline().split()))
    costs.append(cost)

# 1단계: 부분 문제 정의
# - fn(seq[i:], R) = i번째 집을 R로 시작하여 뒤따르는 집들을 칠하는 최소 비용
#   = i번째 집을 R로 칠하는 비용 + (i+1)번째 집을 G 또는 B로 시작하여 뒤따르는 집들을 칠하는 최소 비용 
#   = R(i) + min( fn(seq[i+1:], G), fn(seq[i+1:], B) )
# - solve(seq[i:]) = min( fn(seq[i:],R), fn(seq[i:],G), fn(seq[i:],B) )
# - 현재 문제의 정답이 될 수 있는 선택지(부분 문제)는 3개이며, 전체 부분 문제의 개수 N * 3

# 2단계: 메모 테이블 생성
# - 각 부분 문제의 정답을 저장하는 메모 테이블 생성
# - 집의 위치 0 ~ N-1이고, i번째 집을 R,G,B로 시작하는 최소 비용
# - 계산 편의를 위해 인덱스가 N인 집을 추가
memo = [[0, 0, 0] for _ in range(N+1)] # 순서대로 R, G, B

# 3단계: 부분 문제의 선후관계에 따라 문제 해결
# - 모든 부분 문제를 적어도 한번씩 풀어야하므로 상향식으로 구성
# - 부분 문제 정의에 따라 맨 뒤의 집부터 해결 (topological order)
for i in range(N-1, -1, -1):
    # i번째 집이 고려할 수 있는 3가지 색 중 하나 선정
    for color in range(3):
        # 선정되지 않은 나머지 2가지 색으로 뒤따르는 집의 최소 비용 확인
        min_subscore = float("inf")
        for other in range(3):
            if color != other:
                min_subscore = min(min_subscore, memo[i+1][other]) 
        memo[i][color] = costs[i][color] + min_subscore

# 4단계: 본래의 문제 해결
# - 인덱스 0번째 집을 R, G, B 중 하나로 시작하는 비용 중 최소값 출력
min_score = min(memo[0])
print(min_score)