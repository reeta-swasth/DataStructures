from itertools import product
import sys

A = list(map(int,sys.stdin.readline().rstrip().split(' ')))
B= list(map(int,sys.stdin.readline().rstrip().split(' ')))

l = list(product(A,B))

for i in range(0,len(l),1):
    v= l[i]
    print v,

