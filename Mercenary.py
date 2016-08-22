import sys

number_test = map(int,raw_input().strip().split(' '))
data =[]
output =[]
list_data =[[0 for y in xrange(100)] for x in xrange(100)]

N = number_test[0]
K= number_test[1]


for i in range(0,K,1):
    data = map(int,raw_input().strip().split(' '))
    print data
    m=0
    for j in range(0,N,1):
        list_data[i][j] = data[m]
        m= m +1


cost =0
output.append(10001)
for j in range(0,K,1):
    if list_data[j][0] < output[0]:
        output[0] = list_data[j][0]
cost = output[0]


for i in range(0,N,1):
    cost =0
    output.append(10001)


print output
