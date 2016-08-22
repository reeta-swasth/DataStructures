import sys

number_of_test = int(sys.stdin.readline())
input_string =[]

for i in range(0,number_of_test,1):
    input_string.append(str(sys.stdin.readline().rstrip('\n')))

var =''
for i in range(0,number_of_test,1):
    for j in range(0,number_of_test,1):
        if (i != j):
            if (input_string[i]).startswith(input_string[j]):
                var = input_string [i]
                break
            if (input_string[j]).startswith(input_string[i]):
                var = input_string [j]
                break
    if var != '':
        break

if var !='':
    sys.stdout.writelines("BAD SET\n")
    sys.stdout.writelines("%s\n" % var)
else:
    sys.stdout.writelines("GOOD SET\n")
