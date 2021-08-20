import sys

sys.stdin = open("./baekjoon/testcase.txt", "r")

R, C = tuple(map(int, sys.stdin.readline().split()))
matrix = []
for _ in range(R):
    row = [c for c in sys.stdin.readline().rstrip()]
    matrix.append(row)
print(R, C, matrix)

# 탐색 시작점 설정
s = (0,0)
# 간선 정보 누적을 위한 parent 생성
parent = {s: None}
# 경로를 기록하기 위한 스택 생성
char = matrix[s[0]][s[1]]
stack = [char]
print(stack)



