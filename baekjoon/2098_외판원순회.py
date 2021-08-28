## 잘못된 풀이: 중간에 방문했던 도시로의 방문은 제한되는데 이 점을 고려하지 못했음!

import sys

sys.stdin = open("./baekjoon/testcase.txt")
N = int(sys.stdin.readline())

costs = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    costs.append(row)

# 1단계: 부분 문제 정의
# - fn(k,B) = k개 도시를 방문하면서 B를 마지막으로 방문했을 때의 최소 비용
#           = min( fn(k-1,CITY) + dist(CITY,B) for CITY in {출발지 A와 도착지 B를 제외한 도시들} ) 
# - dist(A,B) = 도시 A에서 도시 B로 이동하는 비용
# - 부분 문제의 개수 = (n-1)**2 (이 때 n-1은 출발지를 제외한 방문해야 하는 도시의 개수)
# - 선택지의 개수 = 출발지와 도착지를 제외한 도시들의 개수

# 2단계: 메모 테이블 생성
# - 각 부분 문제의 정답을 저장하는 메모 테이블 생성
# - 방문한 도시의 개수 1~(n-1), 마지막이 되는 도시의 개수 1~(n-1)
# - 도시 인덱스와 맞추기 위해 방문 도시 개수, 마지막 도시 개수 모두 N으로 설정
# - 도시 개수가 1개 일 때는 사전 입력
memo = [[0]*(N) for _ in range(N)]
start = 0
# 방문 도시가 1개이고, 마지막 도시가 city일 때의 비용
for city in range(1, N):
    memo[1][city] = costs[start][city]
print(memo)

# 3단계: 부분 문제의 선후 관계에 따라 문제 해결
# - 방문 도시 개수가 k개인 부분 문제는 방문 도시 개수가 k-1개일 때의 부분 문제들을 활용하므로
# - 방문 도시 개수가 1개일 때부터 순차적으로 해결
for k in range(2, N):
    for city in range(1, N):
        # 구하려는 값: k개 도시를 방문하면서 city를 마지막으로 방문했을 때의 최소 비용
        min_score = float("inf")
        for prev_city in range(1, N):
            if city != prev_city:
                # k-1개 도시를 방문하면서 prev_city를 마지막으로 방문했을 때의 최소 비용에 
                # prev_city에서 city로 이동하는 비용을 추가
                score = memo[k-1][prev_city] + costs[prev_city][city]
                min_score = min(min_score, score)
        memo[k][city] = min_score

print(memo)
# 4단계: 본래의 문제 해결
# - n-1번째 도시를 방문하면서 각 city를 마지막으로 방문했을 때의 최소 비용에 다시 start로 돌아가는 비용 추가
# - 그 중의 최소값을 답으로 결정
min_score = float("inf")
for city in range(1, N):
    score = memo[-1][city] + costs[city][start]
    min_score = min(min_score, score)

print(min_score)