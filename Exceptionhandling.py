import sys

list1 =[]
t= int(sys.stdin.readline())
for i in range(t):
    data = list(sys.stdin.readline().rstrip().split())
    list1.append(data)

#print list1


for j in range(t):
    data= list1[j]
    a = data[0]
    b = data[1]
    try:
        print int(a)/int(b)
    except ValueError as e1:
        print "Error Code:" , e1
    except ZeroDivisionError as e:
        print "Error Code:",e


