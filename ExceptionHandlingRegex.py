import re
import sys

list1 =[]
t= int(sys.stdin.readline())
for i in range(t):
    list1.append(sys.stdin.readline().rstrip())

for i in range(t):
    try:
        re.compile(list1[i])
        is_valid = True
    except re.error:
        is_valid = False
    print is_valid