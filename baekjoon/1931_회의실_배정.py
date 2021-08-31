import sys
sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
teams = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 1단계: 종료 시간 순으로 정렬
# - 종료 시간이 동일한 경우, 시작 시간 순으로 정렬
teams.sort(key=lambda t: (t[1], t[0]))

# 2단계: 기준에 맞게 하나씩 선택
# - 1) 종료 시간이 가장 빠른 팀 선택
# - 2) 선택된 팀과 양립 불가능한 팀 제거
# - 3) 남은 팀이 있을 때까지 1,2 절차 반복

selected = []
i = -1
last_finish_time = 0
while i < len(teams)-1:
    i += 1
    team = teams[i]
    ts, tf = team
    # 남은 팀들 중 시작 시간이 선택된 마지막 팀의 종료 시간보다 빠른 팀 제외
    if ts < last_finish_time:
        continue 
    # 종료 시간이 가장 빠른 팀을 선택
    # (종료 시간 순으로 정렬되어 있으므로 가장 앞에 있는 팀)
    last_finish_time = tf
    selected.append(team)

print(selected)
print(len(selected))