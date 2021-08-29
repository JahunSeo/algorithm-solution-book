import sys
sys.stdin = open("./baekjoon/testcase.txt")

A = int(sys.stdin.readline(), 2)
B = int(sys.stdin.readline(), 2)

print(A, B)
L = 10**5
L = 20
print(bin(A & B)[2:].zfill(L))
print(bin(A | B)[2:].zfill(L))
print(bin(A ^ B)[2:].zfill(L))
print(bin(~A))
print(bin(~B))
