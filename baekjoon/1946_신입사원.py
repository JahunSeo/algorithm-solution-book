import sys
sys.stdin = open("./baekjoon/testcase.txt")

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    # 1단계: 점수_1을 기준으로 정렬하기 
    # - 배열의 인덱스를 점수_1로 삼아 입력 시점부터 정렬하기
    applicants = [0]*(N+1)
    for _ in range(N):
        s1, s2 = tuple(map(int, sys.stdin.readline().split()))
        applicants[s1] = s2

    # 2단계: 점수_1의 등수가 가장 낮은 인원부터 높은 인원까지 통과 여부 판단
    # - 이 때, 인원_i의 점수_2 등수가 앞선 인원들의 점수_2 등수보다 작아야만 통과
    # - 그러므로 최소값을 유지하며 갱신되는지 확인
    # count 초기값: 점수_1의 1등은 무조건 통과이므로 count 초기값 1
    count = 1
    # min_score 초기값: 점수_1이 1등인 인원의 점수_2
    min_score = applicants[1] 
    # 점수_1이 2등인 인원부터 통과여부 확인
    for i in range(2, len(applicants)):
        score = applicants[i]
        if score < min_score:
            count += 1
            min_score = score
    print(count)