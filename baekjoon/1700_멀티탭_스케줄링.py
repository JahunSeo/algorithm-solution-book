import sys
sys.stdin = open("./baekjoon/testcase.txt")
N, K = tuple(map(int, sys.stdin.readline().split()))
items = list(map(int, sys.stdin.readline().split()))

current = set()
i = -1
count = 0
while i < K-1:
    i += 1
    item = items[i]
    print("item", i, item, current)
    # 이미 콘센트에 꽂혀 있는 경우
    if item in current:
        continue
    # 콘센트가 비어 있는 경우
    if len(current) < N:
        current.add(item)
        continue
    # 콘센트에 없는 경우, current에서 뽑을 대상을 선택
    # - current의 아이템 중, 현재 아이템 다음으로 오는 N-1개에서 없는 아이템 선택 
    #   (현재 아이템 다음으로 오는 N-1개 중에 없으면 결국에는 뽑여야 하는 아이템이기 때문)
    to_delete = None
    for c in current:
        if c not in items[i+1:i+N]:
            to_delete = c
            break
        # is_coming = False
        # for next_idx in range(i+1, i+N):
        #     if next_idx < K and c == items[next_idx]:
        #         is_coming = True
        #         break
        # if not is_coming:
        #     to_delete = c
        #     break
    print("  delete", items[i:i+N], current, to_delete)
    current.remove(to_delete)
    current.add(item)
    count += 1

print(current)
print(count)


    