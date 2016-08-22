import sys

t=int(raw_input())
list_data =[[0 for y in xrange(100)] for x in xrange(100)]
len_list =[]
i=0
for x in xrange(t):
    n= int(raw_input())
    len_list.append(n)
    data = map(int,raw_input().split())
    m=0
    for j in range(0,n,1):
        list_data[i][j] = data[m]
        m= m +1
    i= i +1


val = 1

for i in xrange(0,t,1):
    val =0
    for j in xrange(1,len_list[i],1):
       for k in xrange(0,len_list[i]-j,1):
           m = 1
           for l in xrange(k, len_list[i],1):
                val = val ^ list_data[i][l]
                m= m + 1
                if m > j:
                    break

sys.stdout.writelines("%s" % val)