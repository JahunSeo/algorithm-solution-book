import sys
import re
n = int(sys.stdin.readline())
question = sys.stdin.readline().rstrip()

# print(question)
question = re.sub('[^0-9]', ' ', question)
print(question)
print(sum(map(int, question.split())))