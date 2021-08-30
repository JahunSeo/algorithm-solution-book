import sys

sys.stdin = open("./baekjoon/testcase.txt")

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

# 1단계: 부분 문제 정의
# - f(i, j) = A[i:]와 B[j:]의 최장 공통 부분 수열
#           = 1 + f(i+1, j+1) if A[i] == B[i] else max(f(i, j+1), f(i+1, j))
#   - 이 때의 본래 문제는 f(0, 0)
# - 상향식으로 수정
#   - DP(i, j) = A[:i]와 B[:j]까지의 최장 공통 부분 수열
#   - 이 때의 본래 문제는 DP(len(A)-1, len(B)-1)
# - 전체 부분 문제: len(A) * len(B)개
#   - DP(0,0)부터 DP(len(A)-1, len(B)-1)까지 순차적으로 해결
# - 선택지: 3개 
#   - DP(i+1,j+1), DP(i+1,j), DP(i,j+1)

# 2단계: 메모 테이블 구성
# - 부분 문제의 최적해를 저장하기 위한 메모 테이블 구성
# - 0<=i<len(A), 0<=j<len(B)를 담을 수 있는 matrix 생성
# 편의를 위해 A, B에 더미 문자 추가
A = "$" + A
B = "$" + B

memo = [[(0,"")]*(len(B)) for _ in range(len(A))]
# 각 문자열의 첫번째 값들이 일치하는지 확인하여 memo 초기 설정

def print_memo():
    for r in memo:
        print(r)
    print()

# print_memo()
for i in range(1, len(A)):
    for j in range(1, len(B)):
        # 앞선 3개의 부분문제 확인
        # 문자열의 맨 앞 글자 두 개가 같은 경우
        if A[i] == B[j]:
            prev_score, prev_text = memo[i-1][j-1]
            score = prev_score + 1
            text = prev_text + A[i]
            memo[i][j] = (score, text)
        # 다른 경우
        else:
            if memo[i-1][j][0] < memo[i][j-1][0]:
                memo[i][j] = memo[i][j-1]
            else: 
                memo[i][j] = memo[i-1][j]
            
# print_memo()
answer = memo[len(A)-1][len(B)-1]
print(answer[0])
print(answer[1])
