import sys
N = int(sys.stdin.readline())

# 1단계: 부분 문제 정의
# - 문제의 정답(solution)이 될 수 있는 부분문제의 선택지는 3개 (나누기 3, 나누기 2, 빼기 1)
# - f(X) = 1 + min(f(X//3), f(X//2), f(X-1))
# - 1부터 N까지의 모든 값이 부분 문제가 될 수 있으며, 부분 문제의 개수 N

# 2단계: memo table 생성
# - 각 부분 문제들의 정답(solution)을 저장하는 메모 테이블 생성
# - 부분 문제의 입력값은 1~N 이므로 인덱스가 부분문제의 입력값을 의미하는 배열 생성
# - (x가 인덱스와 매칭될 수 있도록 배열의 길이를 N+1로 설정)
memo = [None] * (N+1)

# 3단계: 함수 생성 
# - 하위 문제의 순서(topological order)를 고려해 순서대로 실행

# 하향식 방식
def fn_topdown(x):
    if memo[x]:
        return memo[x]
    if x == 1:
        return 0

    subproblems = [] # 현재 문제 x의 부분문제들
    if x%3 == 0: subproblems.append(x//3)
    if x%2 == 0: subproblems.append(x//2)
    if x > 1: subproblems.append(x-1)

    subscores = [] # 각 부분문제들의 정답
    for p in subproblems:
        memo[p] = fn_topdown(p)
        subscores.append(memo[p])

    # 각 부분문제의 정답을 고려해 현재 문제 x에 대한 정답을 선택
    return 1 + min(subscores)

# 하향식 방식 효율화 버전
def fn_topdown2(x):
    if memo[x]:
        return memo[x]
    if x == 1:
        return 0

    min_subscore = float("inf")
    if x%3 == 0:
        min_subscore = min(min_subscore, fn_topdown2(x//3))
    if x%2 == 0: 
        min_subscore = min(min_subscore, fn_topdown2(x//2))
    if x > 1:
        min_subscore = min(min_subscore, fn_topdown2(x-1))

    # 각 부분문제의 정답을 고려해 현재 문제 x에 대한 정답을 선택
    memo[x] = 1 + min_subscore
    return memo[x]  

# 상향식 방식
from collections import deque
def fn_bottomup(x):
    memo[1] = 0
    frontier = deque([1])
    while not memo[x] and frontier:
        v = frontier.popleft() # v 는 subproblem
        subscore = memo[v] # subsccore는 부분문제 v의 정답
        for next_v in [v*3, v*2, v+1]: # next_v 는 v에서 간선으로 이어진 다음 subproblem
            if next_v == x:
                memo[next_v] = subscore + 1
                break
            elif next_v < N+1:
                memo[next_v] = subscore + 1
                frontier.append(next_v)
        # print(memo)                
    return memo[x]
    

# 4단계: 본래의 문제 해결
print(fn_topdown2(N))
# print(fn_bottomup(N))