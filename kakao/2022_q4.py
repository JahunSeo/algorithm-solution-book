def solution(n, info):
    matrix = [[(0,[])]*(n+1) for _ in range(11)]

    i = 1
    oppo = info[10-i]
    matrix[i][n] = (matrix[i-1][n][0] + cal_keep(i, oppo), matrix[i-1][n][1])
    matrix[i][n - oppo - 1] = (matrix[i-1][n][0] + i, matrix[i-1][n][1] + [oppo+1])
    
    print(matrix)

    for i in range(2, 11):
        oppo = info[10-i]
        for k in range(0, n+1):
            if matrix[i-1][k][1]:
                matrix[i][k] = (matrix[i-1][k][0] + cal_keep(i, oppo), matrix[i-1][k][1])
            if k - oppo - 1 >= 0 and matrix[i-1][k][1]:
                matrix[i][k - oppo - 1] = (matrix[i-1][k][0] + i, matrix[i-1][k][1] + [oppo+1])
    
    print()
    print(matrix[-1])

    answer = []
    return answer

def cal_keep(i, oppo):
    if oppo > 0:
        return -1 * i
    else:
        return 0

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

print(solution(n, info))