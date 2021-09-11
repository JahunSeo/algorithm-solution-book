def solution(n, k):
    answer = 0

    prime = [False, False] + [None]* (n*k)
    def is_prime(x):
        if prime[x] != None:
            return prime[x]
        for i in range(2, x//2):
            if x % i == 0:
                prime[x] = False
                return False
        prime[x] = True
        return True


    rest = n
    keep, length = 0, 0
    while rest:
        rest, to_add = rest//k, rest % k
        if to_add == 0:
            if length != 0 and is_prime(keep):
                answer += 1
            keep, length = 0, 0
            continue
        keep += (10**length) * to_add
        length += 1

    if length != 0 and is_prime(keep):
        answer += 1       

    return answer



print(solution(437674, 10))