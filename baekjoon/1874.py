import sys
sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
questions = [int(sys.stdin.readline()) for _ in range(N)]
top_idx = 0

stack = []
answers = []

num = 1
while top_idx < N:
    # print(stack)
    if stack and stack[-1] == questions[top_idx]:
        stack.pop()
        answers.append("-")
        top_idx += 1
    else:
        stack.append(num)
        answers.append("+")
        num += 1
        if num > N+1:
            break

# print(stack, answers)
if (stack):
    print("NO")
else:
    for c in answers:
        print(c)
