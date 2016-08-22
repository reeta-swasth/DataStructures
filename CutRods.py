import sys

required_length = int(sys.stdin.readline())
total_number_input = int(sys.stdin.readline())

input ={}
result =[]

for i in range(1,total_number_input +1,1):
    input[i] = int(sys.stdin.readline())

for i in range(1,total_number_input +1,1):
    print input[i]

result.append(0)


print "+++++++++++++++"
for i in range(1,total_number_input +1 ,1):
    q= -10000
    for j in range(1,i+1,1):
        q= max(q,result[i-j] + input[j])
    result.append(q)
    print result[i]


