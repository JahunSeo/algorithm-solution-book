import sys
x = sys.stdin.readline().rstrip()
if x[0] != "0":
    # 10진수
    print(x)
elif x[1] != "x":
    # 8진수
    x = x[1:]
    total, z = 0, 1
    while x:
        num = int(x[-1])
        total += num * z
        x = x[:-1]
        z *= 8
    print(total)
else:
    # 16진수
    x = x[2:]
    total, z = 0, 1
    while x:
        num = x[-1]
        if num == "a": num = 10
        elif num == "b": num = 11
        elif num == "c": num = 12
        elif num == "d": num = 13
        elif num == "e": num = 14
        elif num == "f": num = 15
        else: num = int(num)
        total += num * z
        x = x[:-1]
        z *= 16
    print(total)

