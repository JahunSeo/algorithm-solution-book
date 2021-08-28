import sys

sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
keynum = values.pop()

# 1단계: 부분 문제 정의 (조금 더 잘 정리해보자)
# - fn(seq) = seq를 이용해 0부터 20까지의 숫자를 각각 몇 개 만들 수 있는지에 대한 결과
#   가령, fn([8]) = {8: 1}  #[8]을 이용하면 8을 1개 만들 수 있음
#        fn([8, 3]) = {5: 1, 11: 1} #8-3, 8+3을 1개 씩 만들 수 있음 
#                   = fn([8])에서 3을 더하거나 빼서 만들어내는 숫자들의 개수로 구성
# - 부분 문제의 개수: seq의 길이

# 2단계: 메모 테이블 구성
# - 각 부분 문제의 정답을 구성하는 메모 테이블 구성
# - 새로운 숫자가 추가될 때마다 0~20의 개수를 저장해주어야 함
# - 그러므로, 부분 문제의 개수(=seq 길이) x 21로 테이블 생성
memo = [ [0]*21 for _ in range(len(values)) ]

# 3단계: 부분 문제의 선후관계에 따라 문제 해결
# - 모든 부분 문제를 적어도 한번씩 계산해야 하므로 상향식으로 구성
# - 첫 번째 숫자는 바로 넣고 시작
memo[0][values[0]] = 1
for i in range(1, len(values)):
    v = values[i]
    for num, count in enumerate(memo[i-1]):
        if count != 0:
            plus = num + v
            if plus >= 0 and plus <= 20:
                memo[i][plus] += count
            minus = num - v
            if minus >= 0 and minus <= 20:
                memo[i][minus] += count

# 4단계: 본래의 문제 해결
# - 모든 숫자(values)를 사용했을 때 만들 수 있는 특정 숫자(keynum)의 개수
print(memo[-1][keynum])