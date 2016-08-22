import sys

n = int(sys.stdin.readline())

list_data =[[0 for y in xrange(2)] for x in xrange(1000)]



for i in range(0,n,1):
    data = map(int,raw_input().strip().split(' '))
    m=0
    for j in range(0,2,1):
        list_data[i][j] = data[m]
        m= m +1


for i in range(0,n,1):
    min_value = min(list_data[i])
    product = list_data[i][0]*list_data[i][1]
    c= 0
    for j in range(1,min_value+1,1):
        p = j *j
        if ( product % p == 0 ):
                c = product / p
    sys.stdout.writelines("%s\n" % c)

