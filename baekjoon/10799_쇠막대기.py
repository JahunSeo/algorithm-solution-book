questions = "()(((()())(())()))(())" # 17
questions = "(((()(()()))(())()))(()())" # 24
# questions = "(()())"
# questions = "((()()))" # 반례!
print("questions", questions)

stack = []
answer = 0
i = 0
# 레이저의 닫는 괄호를 건너 뛰는 코드를 넣기 위해 for문 대신 while문 사용
while i < len(questions):
    q = questions[i]
    # 시작 괄호인 경우, 레이저인지 막대인지 구분
    if q == "(":
        if questions[i+1] == ")": # 레이저
            answer += len(stack)
            # 다음에 오는 닫는 괄호는 탐색에서 건너 뛰도록 하고
            # 그러므로 레이저 시작 괄호 또한 스택에 넣지 않음
            i += 1 
        else: # 새로운 막대
            answer += 1
            stack.append(q)
    # 닫는 괄호인 경우, 막대를 닫아줌
    else:
        stack.pop()
    i += 1


print(answer)