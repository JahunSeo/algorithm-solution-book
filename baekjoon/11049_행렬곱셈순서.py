import sys
sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
matrices = []
for _ in range(N):
    m = tuple(map(int, sys.stdin.readline().split()))
    matrices.append(m)
# print(matrices)

# 1단계: memo 생성
memo = []
for _ in range(N):
    row = [0] * N
    memo.append(row)

# 2단계: 상향식으로 각 행렬조합을 만들기 위한 최소 계산 횟수 구하기
# diag은 c - r 이며, r == c 인 구간은 이미 0으로 설정되어 있으므로, 1부터 시작
for diag in range(0, N):
    print("diag!", diag)
    for c in range(diag, N):
        r = c - diag
        print("to calculate:", (r, c))
        if r == c:
            memo[r][c] = (0, *matrices[r])
            continue
        min_matrix = (float("inf"), None, None)
        for i in range(r, c):
            m1, m2 = memo[r][i], memo[i+1][c]
            score = m1[0] + m2[0] + m1[1]*m1[2]*m2[2]
            if score < min_matrix[0]:
                min_matrix = (score, m1[1], m2[2])
        print("result", min_matrix)
        memo[r][c] = min_matrix

print(memo[0][N-1][0])
        

