import sys

sys.stdin = open("./baekjoon/testcase.txt")

line = sys.stdin.readline().rstrip()
values = line.split("-")   
values = [sum(map(int, e.split("+"))) for e in values]
result = values.pop(0)
for v in values:
    result -= v
print(result)