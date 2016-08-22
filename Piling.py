from  collections import deque

import sys

n = int(sys.stdin.readline())
m_list=[]
list_data = [[0 for y in range(100000)] for x in range(5)]

for i in range(0,n,1):
    m = int(sys.stdin.readline())
    m_list.append(m)
    data = map(int,sys.stdin.readline().rstrip().split(' '))
    v=0
    for j in range(0,m,1):
        list_data[i][v] = data[v]
        v= v +1

for i in range(0,n,1):
    temp_list = []
    q = deque(list_data[i][0:m_list[i]])
    v =deque(list_data[i][0:m_list[i]])

    c= len(q)
    l =0
    p = c-1
    z=10000
    for j in range(0,c,1):
        if q[l] >= q[p] and q[l] <= z:
            z= v.popleft()
            l=l+1
            #print z
        elif q[p] > q[l] and q[p] <= z:
            p= p-1
            z= v.pop()
            #print z
        elif q[l] > z and q[p] > z:
            break
    if len(v) > 0:
        sys.stdout.writelines("No\n")
    else:
        sys.stdout.writelines("Yes\n")




