import sys
sys.stdin = open("./baekjoon/testcase.txt")
line = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

bomblen = len(bomb)

stack = ""
for c in line:
    stack += c
    # check stack
    if len(stack) >= bomblen and stack[-1] == bomb[-1] and (stack[-bomblen:] == bomb):
        del stack[bomblen:] 
        
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
    