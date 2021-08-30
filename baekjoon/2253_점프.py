import sys
sys.stdin = open("./baekjoon/testcase.txt")

N, M = tuple(map(int, sys.stdin.readline().split()))

fakes = set()
for _ in range(M):
    fakes.add(int(sys.stdin.readline()))

# 1단계: 부분 문제 정의

# 2단계: 메모 테이블 구성
# - 각 부분문제의 정답을 저장하기 위한 메모 테이블 구성
# - 부분문제는 점프개수 x 위치(k, 1~N) x 속도(v, 0~N-1) 
# - 점프 개수는 최소로 유지하여 중복 문제 제거
# - 가상의 위치 0 생성
import math
v_limit = int(math.sqrt(2*N - 2)) + 1
memo = [[0] * v_limit for _ in range(N+1)]
# 3단계: 부분 문제의 선후관계에 맞게 순서대로 부분 문제 해결
# - 일단 1회 점프 처리
# - v 는 1 이상이어야 함
# - fakes 고려
k, v, jump = 2, 1, 1
memo[k][v] = jump
# print(memo)
for k in range(2, len(memo)):
    for v in range(1, v_limit):
        jump = memo[k][v]
        if jump == 0:
            continue
        for new_v in [v-1, v, v+1]:
            new_k = k + new_v
            if new_v <= 0 or new_v > v_limit or new_k > N or new_k in fakes:
                continue
            memo[new_k][new_v] = jump + 1


answer = float("inf")
for jump in memo[N]:
    if jump != 0:
        answer = min(answer, jump)

if answer == float("inf"):
    print(-1)
else:
    print(answer)

## 하향식 접근
# # 2단계: 메모 테이블 구성
# # - 각 부분 문제의 정답을 저장하기 위한 메모 테이블 구성
# # - 부분문제는 점프개수 x 위치(k, 1~N) x 속도(v, 0~N-1) 
# # - 점프 개수는 최소로 유지하여 중복 문제 제거
# # - 가상의 위치 0 생성
# import math
# v_limit = int(math.sqrt(2*N - 2)) + 1
# memo = [[0] * v_limit for _ in range(N+1)]

# # 3단계: 부분 문제의 선후관계에 맞게 순서대로 부분 문제 해결
# # - 일단 1회 점프 처리
# # - v 는 1 이상이어야 함
# # - fakes 고려
# def fn(k, v):
#     if memo[k][v] != 0:
#         return memo[k][v]
#     # print(k, v)
#     if k == N:
#         return 0
#     min_score = float('inf')
#     for new_v in [v-1, v, v+1]:
#         new_k = k + new_v
#         if new_v <= 0 or new_v > v_limit or new_k > N or new_k in fakes:
#             continue
#         score = fn(new_k, new_v)
#         min_score = min(min_score, score)
    
#     memo[k][v] = 1 + min_score
#     return memo[k][v]

# answer = fn(1, 0)
# # print(memo)
# print(answer)
