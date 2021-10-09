import sys
n = int(sys.stdin.readline())
while n > 1:
    found = False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            print(i)
            n = n // i
            found = True
            break
    if not found:
        print(n)
        break
