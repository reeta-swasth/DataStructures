from itertools import product
from itertools import repeat

import sys

n= int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().rstrip().split(' ')))
k= int(sys.stdin.readline())



for i in range(0,n-k+1,1):
    l = list(a[i:i+k:1])
    print l














