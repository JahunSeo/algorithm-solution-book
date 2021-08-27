import sys

sys.stdin = open("./baekjoon/testcase.txt")

N, K = tuple(map(int, sys.stdin.readline().split()))
# print(N, K)
items = []
for _ in range(N):
    w, value = tuple(map(int, sys.stdin.readline().split()))
    items.append((w, value))
# items.sort()
print(items)

# 만들 수 있는 전체 경우의 수는 2^N
# nC0 + nC1 + nC2 + ... + nCn


# 추상화 1단계: 답이 될 수 있는 조합들을 모두 남긴다
# candidates = [(0,0)]
# max_value = 0
# for w, value in items:
#     new_candidates = []
#     for prev_w, prev_value in candidates:
#         new_w = prev_w + w
#         new_value = prev_value + value
#         if new_w <= K:
#             new_candidates.append((new_w, new_value))
#             max_value = max(max_value, new_value)
#     candidates = candidates + new_candidates

# print(max_value)

# 추상화 2단계: 답이 될 수 있는 조합들에서 동일 무게 중 가치가 최대인 조합만 남긴다
# - 동일 무게 중 가치가 작은 조합은, 동일 무게 중 가치가 큰 조합보다 더 좋은 조합을 만들 수 없음
# candidates는 각 무게에서 최대의 가치를 저장
candidates = {0: 0}
for w, value in items:
    new_candidates = dict(candidates)
    for prev_w, prev_value in candidates.items():
        new_w = prev_w + w
        new_value = prev_value + value
        # print(w2, value2, new_w, new_value)
        if new_w <= K:
            if new_w not in candidates or candidates[new_w] < new_value:
                new_candidates[new_w] = new_value
    candidates = new_candidates

print(max(candidates.values()))


# def sum_weights(subset):
#     return sum(item[0] for item in subset)

# def sum_values(subset):
#     return sum(item[1] for item in subset)

# def fn2(items):
#     # 종료 조건: 아이템이 없을 경우
#     if len(items) == 0 :
#         return 0, [[]]
#     # 아이템이 존재할 경우, 아이템 하나를 제외한 아이템들로 하위 문제 구성
#     item = items[0]
#     prev_max, prev_subsets = fn2(items[1:])
#     # 하위 문제의 부분집합들에 새로운 아이템을 추가해, 새로운 부분집합 생성
#     new_subsets = []
#     new_max = 0
#     for s in prev_subsets:
#         ns = s + [item]
#         if sum_weights(ns) <= K:
#             new_max = max(new_max, sum_values(ns))
#             new_subsets.append(ns)
#     max_value = max(new_max, prev_max)
#     subsets = prev_subsets + new_subsets   
#     return max_value, subsets

# max_value, subsets = fn2(items)
# print(max_value)
