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
# for w1, value1 in items:
#     new_candidates = candidates[:]
#     for w2, value2 in candidates:
#         new_w = w1 + w2
#         new_value = value1 + value2
#         if new_w <= K:
#             new_candidates.append((new_w, new_value))
#             max_value = max(max_value, new_value)
#     candidates = new_candidates
#     print((w1, value1), K, max_value, new_candidates)

# print(max_value)

# 추상화 2단계: 답이 될 수 있는 조합들에서 동일 무게 중 가치가 최대인 조합만 남긴다
# - 동일 무게 중 가치가 작은 조합은, 동일 무게 중 가치가 큰 조합보다 더 좋은 조합을 만들 수 없음
# candidates는 각 무게에서 최대의 가치를 저장
# - 각 위치에 무게가 k이고 가치가 0인 아이템이 있었다고 생각
candidates = [0] * (K+1)

candidates = {0: 0}
for w, value in items:
    print("start!", w, value, candidates)
    new_candidates = dict(candidates)
    for prev_w, prev_value in candidates.items():
        new_w = prev_w + w
        new_value = prev_value + value
        # print(w2, value2, new_w, new_value)
        if new_w <= K:
            if new_w not in candidates:
                new_candidates[new_w] = new_value
            elif candidates[new_w] < new_value:
                print("update:", (w, value), (new_w, new_value), candidates[new_w])
                new_candidates[new_w] = new_value
    candidates = new_candidates
    print("result:", (w, value), K, candidates)

print(max(candidates.values()))