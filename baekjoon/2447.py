import sys
n = int(sys.stdin.readline())

answer = [""] * n

def blank(r, c, width):
    for i in range(width):
        for j in range(width):
            answer[r+i] += " "

def fill(r, c, width):
    sub = width // 3
    if width == 1:
        answer[r] += "*"
        return
    fill(r, c, sub)
    fill(r, c+sub, sub)
    fill(r, c+sub*2, sub)
    fill(r+sub, c, sub)
    blank(r+sub, c+sub, sub)
    fill(r+sub, c+sub*2, sub)
    fill(r+sub*2, c, sub)
    fill(r+sub*2, c+sub, sub)
    fill(r+sub*2, c+sub*2, sub)

fill(0, 0, n)

for row in answer:
    print(row)