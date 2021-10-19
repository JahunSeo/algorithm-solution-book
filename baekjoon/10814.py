import sys 
n = int(sys.stdin.readline())
people = []
for i in range(n):
    line = sys.stdin.readline().rstrip()
    age = int(line.split()[0])
    people.append((age, i, line))

people.sort(key=lambda x: (x[0], x[1]))

for age, i, line in people:
    print(line)
