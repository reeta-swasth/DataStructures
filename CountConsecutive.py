#Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters and only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.
#Your task is to find the minimum number of required deletions

import sys

count = int(sys.stdin.readline())

strings =[]
for i in range(0,count,1):
    strings.append(sys.stdin.readline())


for m in range(0,count,1):
    s = strings[m]
    c =0
    for i in range(0, len(s) -1,1):
        if i == len(s) -2:
            if s[i] == s[i+1]:
                c =  c + 1
                i= i+1
        else:
            if s[i] == s[i+1]:
                c = c +1
                i= i+1

    sys.stdout.write("%s \n"%c)





