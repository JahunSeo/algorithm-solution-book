import sys
sys.stdin = open("./baekjoon/testcase.txt")

N, M = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

total = sum(arr)
maxvalue = max(arr)
# 답이 될 수 있는 최소값과 최대값
start, end = total // M, total
# 정답의 초기값은 최대값으로 설정
optimal = end


def solve(arr, boxsize):
    global N, M, maxvalue
    # arr의 처음부터 각 box 안에 최대한으로 채우며 box 개수를 늘려나갈 때
    # 전체 필요한 box의 개수가 M 보다 작거나 같다면 통과, 아니면 실패
    subsum, count = 0, 1
    for item in arr:
        # 만약 한 아이템의 크기가 boxsize 보다 크다면, 결국 성공할 수 없으므로 바로 리턴 
        if item > boxsize:
            return False
        # 현재 박스에 담을 수 있는 경우
        if subsum + item <= boxsize:
            subsum += item
        # 현재 박스에 담을 수 없는 경우
        else:
            count += 1
            subsum = item
            # 이 때 count가 M을 초과하면 실패
            if count > M:
                return False
    # 필요한 최종 box의 개수가 M보다 작거나 같으므로 통과
    return True

while start <= end:
    # 정답이 될 수 있는 값의 후보인 mid를 설정
    mid = (start + end) // 2
    # 정답이 될 수 있는지 판단: mid값으로 M개에 나누어 담기가 가능한지 여부
    result = solve(arr, mid)
    # 정답이 될 수 있는 경우
    # - 저장 후 더 낮은 범위를 탐색
    if result:
        optimal = min(optimal, mid)
        end = mid - 1
    else:
        start = mid + 1

print(optimal)


