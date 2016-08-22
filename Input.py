import sys

data= list(map(int,sys.stdin.readline().rstrip().split(' ')))
x = data[0]
k= data[1]
v= input()
if v==k:
    print "True"
else:
    print "False"
