import sys
n = int(sys.stdin.readline())

def toggle(r, c, width):
    # print(r, c, width)
    sub = width // 3
    if r >= sub and r < sub*2 and c >= sub and c < sub*2:
        return " "
    elif sub == 1:
        return "*"
    else:
        return toggle(r%sub, c%sub, sub)

for i in range(n):
    row = ""
    for j in range(n):
        row += toggle(i, j, n)
    print(row)