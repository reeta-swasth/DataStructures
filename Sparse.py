import sys

a =int(sys.stdin.readline())

print bin(a)
b= a>>1
c = a & b

if  c ==0:
    print "sparse"
else:
    print "not sparse"
