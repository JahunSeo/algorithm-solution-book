import sys

sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))

# 각 값들까지 중 최대 부분 수열 길이 저장
results = []
# storage의 각 인덱스는 부분 수열의 길이, 값은 그 길이를 가진 부분 수열 끝값 중 가장 작은 값을 의미
# 편의성을 위해 0번 인덱스에 0을 배치 (모든 value는 0보다 큼)
storage = [0]
for v in values:
    # 이분탐색으로 storage에서 값이 자신보다 작은 가장 높은 인덱스를 찾기
    start, end = 0, len(storage)-1
    # 인덱스의 최대값을 찾는 것이므로 최소값으로 초기값 설정
    max_len = start 
    while start <= end:
        mid = (start+end)//2
        mid_value = storage[mid]
        if mid_value < v:
            max_len = mid
            start = mid + 1
        else:
            end = mid - 1
    # 현재 값으로 만든 최대 부분 수열 길이 저장
    max_len = max_len + 1
    results.append(max_len)
    # storage 업데이트
    if len(storage)-1 < max_len:
        storage.append(v)
    elif v < storage[max_len]:
        storage[max_len] = v

max_length = len(storage) - 1
answer = []
count = max_length
for i in range(len(values)-1, -1, -1):
    r, v = results[i], values[i]
    if r == count:
        answer.append(v)
        count -= 1
answer.reverse()

print(results, values, storage)
print(max_length)
print(" ".join([str(c) for c in answer]))