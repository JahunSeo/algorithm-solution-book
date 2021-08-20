import sys

sys.stdin = open("./baekjoon/testcase.txt", "r")

R, C = tuple(map(int, sys.stdin.readline().split()))
matrix = []
for _ in range(R):
    row = [c for c in sys.stdin.readline().rstrip()]
    matrix.append(row)

# (참고) 이 문제에서는 이미 탐색된 위치인지 확인해 거르지 않음
#  - 이전에 탐색된 위치이더라도 다시 경로에 포함될 수 있음
#  - 가령, 아래의 사례에서 A B D C 순서로 깊이 우선 탐색을 진행하면서
#    순서대로 B D C 를 막아버리면, A C D B E 를 탐색할 수 없음
#  - A B E 
#    C D D
#  - 그러므로 parent 등으로 탐색된 곳인지 누적할 필요 없음

# 탐색 시작점 설정
s = (0,0)
# 경로를 기록하기 위한 스택 생성 (문자열로 대체)
char = matrix[s[0]][s[1]]
stack = char
# 스택의 최대 길이(최장 경로) 초기화
max_length = len(stack)

# 상하좌우 탐색을 위한 dx, dy
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def DFS_visit(v):
    global stack, max_length
    print("[visit]", v, max_length, stack)
    x1, y1 = v
    # 상하좌우를 모두 확인하며, 지나온 경로는 stack에 누적된 알파벳을 통해 걸러냄
    for dx, dy in zip(dxs, dys):
        x2, y2 = x1 + dx, y1 + dy    
        # 존재하지 않는 위치인지 확인
        if x2 < 0 or x2 >= R or y2 < 0 or y2 >= C:
            continue
        # 탐색하려는 위치의 알파벳이 기존에 있던 값인지 스택을 통해 확인
        char = matrix[x2][y2]
        if char in stack:
            continue
        # 새로운 알파벳이면 스택에 추가 후 다음 깊이로 탐색 시작
        v2 = (x2, y2)
        stack += char
        # 최장 경로인지 확인하여 업데이트
        if len(stack) > max_length:
            max_length = len(stack)
        DFS_visit(v2)
    # v에서 시작하는 탐색이 모두 종료되었을 때 stack에서 알파벳 제거
    stack = stack[:-1]

DFS_visit(s)
print(max_length)
