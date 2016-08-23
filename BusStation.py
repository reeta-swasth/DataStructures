import sys

n = sys.stdin.readline()
groups = map(int,raw_input().strip().split(' '))
result = []

v= max(groups)

for i in xrange(v,sum(groups)+1,1):
    s=[]
    s.append(0)
    flag = True
    for j in  xrange(0,len(groups),1):
        if sum(s) > i:
            flag = False
            break
        if sum(s)+groups[j] == i:
            s =[]
            s.append(0)
            continue
        if groups[j] < i:
            s.append(groups[j])
            continue
        if (groups[j] >= i) and ((sum(s) + groups[j]) > i):
            flag = False
            break
    if flag == False:
        continue
    if sum(s) > 0 and sum(s)!=i:
        continue
    else:
        result.append(i)

for i in range(0,len(result),1):
    sys.stdout.writelines("%s " % result[i])




