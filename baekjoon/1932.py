import sys

sys.stdin = open("./baekjoon/testcase.txt")
depth = int(sys.stdin.readline())
tree = []
for dep in range(depth):
    line = list(map(int, sys.stdin.readline().split())) 
    tree.append(line)

# print(tree)

for dep in range(1, depth):
    # prev = tree[dep-1]
    # curr = tree[dep]
    for i, num in enumerate(tree[dep]):
        prevmax = 0
        if i-1 >= 0:
            prevmax = max(prevmax, tree[dep-1][i-1])
        if i < dep:
            prevmax = max(prevmax, tree[dep-1][i])
        tree[dep][i] = prevmax + tree[dep][i]

# print(tree)
print(max(tree[-1]))