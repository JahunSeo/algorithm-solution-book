import sys
from collections import deque, Counter

sys.stdin = open("./baekjoon/testcase.txt")
t = int(sys.stdin.readline())
for _ in range(t):
    n, target = tuple(map(int, sys.stdin.readline().split()))
    # print(n, target)
    arr = list(map(int, sys.stdin.readline().split()))
    weight_counter = Counter(arr)
    weight_counter = [[w, c] for w, c in weight_counter.items()]
    weight_counter.sort(reverse=False) # 편의를 위해 높은 우선순위가 뒤에 오도록
    # print(weight_counter)
    queue = deque([(w, i) for i, w in enumerate(arr)])
    # print(queue)

    solved_idx = -1
    solved_cnt = 0
    while solved_idx != target:
        # 시도 횟수 1 추가
        # print("try", solved_idx, target, queue)
        # 현 시점 가장 높은 우선순위 체크
        max_weight = weight_counter[-1][0]
        # queue의 앞에서 하나 뽑아 확인
        front = queue.popleft()
        # 가장 높은 중요도인 경우
        if front[0] == max_weight:
            solved_cnt += 1
            # print("hey!", front, solved_cnt)
            solved_idx = front[1]
            weight_counter[-1][1] -= 1
            if weight_counter[-1][1] == 0:
                weight_counter.pop()
        # 중요도가 낮은 경우
        else:
            queue.append(front)

    print(solved_cnt)

                
        