import sys
sys.stdin = open("./baekjoon/testcase.txt")
T = int(sys.stdin.readline())

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

for _ in range(T):
    # 1단계: matrix 구성하기
    C, R, K = tuple(map(int, sys.stdin.readline().split()))
    matrix = [[0]*R for _ in range(C)]
    total = 0
    for _ in range(K):
        # 좌표 확인
        x, y = tuple(map(int, sys.stdin.readline().split()))
        # 좌표 상에 표시
        matrix[x][y] = 1
    
    # 2단계: BFS 실행
    total = 0
    for x in range(C):
        for y in range(R):
            if matrix[x][y] == 1:
                total += 1
                frontier = [(x, y)]
                while frontier:
                    v = frontier.pop()
                    for dx, dy in zip(dxs, dys):
                        nx, ny = v[0] + dx, v[1] + dy
                        if nx < 0 or nx >= C or ny < 0 or ny >= R:
                            continue
                        if matrix[nx][ny]:
                            matrix[nx][ny] = 0
                            frontier.append((nx, ny))

    print(total)
