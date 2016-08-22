#Shil has a string, , consisting of lowercase English letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "" would become either "" or "" after operation.
import sys

s = sys.stdin.readline()
old_input_string = s

while True:
    old_input_string = s
    input_list = []
    for i in range(0, len(s), 1):
        input_list.append(s[i])


    for i in range(1,len(input_list),1):
        val = input_list[i]
        for j in range(i-1,i,1):
            if val == input_list[j]:
                input_list[j]=0
                input_list[i]=0

    new_list=[]


    for i in range(0,len(input_list),1):
        if input_list[i] != 0:
            new_list.append(input_list[i])



    s = new_list

    if old_input_string == s:
        break


if len(s) ==0:
    str1 = "Empty String"
else:
    str1 = ''.join(str(e) for e in s)
sys.stdout.write(str1)