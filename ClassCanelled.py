import sys

number_of_test = int(sys.stdin.readline())

list_number_students=[]
list_min_number_students =[]
list_time =[]


for i in range(0,number_of_test,1):
    data = sys.stdin.readline().split()
    list_number_students.append(int(data[0]))
    list_min_number_students.append(int(data[1]))
    sub_list_time = sys.stdin.readline().split()
    list_time.append(sub_list_time)

for i in range(0,number_of_test,1):
    sum1 =0
    for n in range(0,list_number_students[i],1):
        if int(list_time[i][n]) <= 0:
            sum1 = sum1 + 1
    if sum1 < list_min_number_students[i]:
        sys.stdout.writelines("YES\n")
    else:
        sys.stdout.writelines("NO\n")





