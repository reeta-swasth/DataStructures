import sys

s = sys.stdin.readline()
m =[]

for i in range(0,len(s),1):
    if i==0 and s[i].isalpha():
        m.append(s[i].upper())
    elif (s[i-1].isspace()):
        m.append(s[i].upper())

    else:
        m.append(s[i])

st = ''.join(m)
sys.stdout.writelines("%s" % st )