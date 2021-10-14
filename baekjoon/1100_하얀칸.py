import sys
sys.stdin = open("./baekjoon/testcase.txt")
count = 0
for r in range(8):
    line = sys.stdin.readline().rstrip()
    for c in range(8):
        is_white = (r + c) % 2 == 0
        print(r, c, is_white, line[c] == 'F')
        if (is_white and line[c] == 'F'):
            count += 1
print(count)

