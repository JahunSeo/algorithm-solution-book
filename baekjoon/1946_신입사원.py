import sys
sys.stdin = open("./baekjoon/testcase.txt")

T = int(sys.stdin.readline())

def solve(applicants):
    # 1단계: 점수_1을 기준으로 정렬하기
    applicants.sort()
    # 2단계: 점수_1의 등수가 가장 낮은 인원부터 높은 인원까지 통과 여부 판단
    # - 이 때, 인원_i의 점수_2 등수가 앞선 인원들의 점수_2 등수보다 작아야만 통과
    # - 그러므로 최소값을 유지하며 갱신되는지 확인
    # 점수_1의 1등은 무조건 통과이므로 count 초기값 1
    count = 1
    min_score = applicants[0][1]
    for i in range(1, len(applicants)):
        score = applicants[i][1]
        if score < min_score:
            count += 1
            min_score = score
    return count

for _ in range(T):
    N = int(sys.stdin.readline())
    applicants = []
    for _ in range(N):
        a = tuple(map(int, sys.stdin.readline().split()))
        applicants.append(a)
    count = solve(applicants)
    print(count)