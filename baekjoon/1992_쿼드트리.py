rows = [
    "11110000",
    "11110000",
    "00011100",
    "00011100",
    "11110000",
    "11110000",
    "11110011",
    "11110011",
]

# rows= [ 
#     "1111",
#     "1111",
#     "0001",
#     "0001"
# ]

# print(rows)
matrix = []
for row in rows:
    matrix.append([c for c in row])
print(matrix)
N = len(matrix)

result = ""
def fn(r, c, N):
    global result
    init_value = matrix[r][c]
    if N == 1:
        result += init_value
        return
    half = N // 2

    # 중간에 다른 값이 없는지 확인
    is_valid = True
    for i in range(r, r+N):
        if not is_valid:
            break
        for j in range(c, c+N):
            v = matrix[i][j]
            if v != init_value:
                is_valid = False
                break
    # 모두 같다면 해당값 출력
    if is_valid:
        result += init_value
        return
    # 다르다면 분리
    # 괄호 시작
    result += "("
    # 4분할
    fn(r, c, half)
    fn(r, c+half, half)
    fn(r+half, c, half)
    fn(r+half, c+half, half)
    # 괄호 끝
    result += ")"

fn(0, 0, N)
print(result)
