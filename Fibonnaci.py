import sys

n= int(sys.stdin.readline())
fibo_list =[]
fibo_list.append(0)
fibo_list.append(1)

for i in range(2,n,1):
    fibo_list.append(fibo_list[i-2]+fibo_list[i-1])

cube = lambda a : a*a*a

cube_list = list(map(cube, fibo_list))
print fibo_list
print (cube_list)
