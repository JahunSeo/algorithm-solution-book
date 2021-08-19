questions = "()(((()())(())()))(())"
# questions = "(()())"
# questions = "((()()))" # 반례!
print("questions", questions)

stack = []
answer = 0
sub_count = 0
for q in questions:
    # 시작 괄호인 경우 스택에 추가
    if q == "(":
        sub_count += 1
        stack.append(q)
        continue
    # 끝 괄호인 경우
    # 바로 닫히는 경우, 즉 레이저인 경우
    if stack[-1] == "(":
        # 스택에서 레이저를 뺀 뒤, 남은 시작 괄호의 수를 센다
        stack.pop()
        sub_count -= 1
        answer += sub_count # sum((c == "(" for c in stack))
        # 스택에 L을 추가한다
        stack.append("L")
        continue
    elif stack[-1] == "L":
        # 스택에서 "(" 를 만날 때까지 레이저를 뺀다
        while stack:
            prev = stack.pop()
            if prev == "(":
                # 막대 끝단을 개수에 추가
                sub_count -= 1
                answer += 1
                # 다시 막대임을 표시해줌
                stack.append("L")
                break

print(answer)