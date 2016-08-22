# The Minion Game

import sys

string_input= sys.stdin.readline()
conso_array =[]
conso_map ={}
vow_array=[]
vow_map={}
sum_conso =0
sum_vowel =0

for i in xrange(0,len(string_input),1):
    if string_input[i] in ('A','E','I','O','U'):
        continue
    else:
        for j in xrange(1,len(string_input),1):
            conso_array.append(string_input[i:j])


for i in xrange(0,len(conso_array)-1,1):
    if len(conso_array[i]) >0:
        conso_map[conso_array[i]]= conso_array.count(conso_array[i])
        sum_conso= sum_conso + conso_map[conso_array[i]]

conso_values = conso_map.values()



for i in xrange(0,len(string_input),1):
    if string_input[i] in ('A','E','I','O','U'):
        for j in xrange(1,len(string_input),1):
            vow_array.append(string_input[i:j])


for i in xrange(0,len(vow_array)-1,1):
    if len(vow_array[i])>0:
        vow_map[vow_array[i]]= vow_array.count(vow_array[i])



vow_values = vow_map.values()
a= sum(conso_values)
b = sum(vow_values)
print a
print b

if a > b:
    sys.stdout.writelines("Stuart %s"% a)
if a ==b:
    sys.stdout.writelines("Draw")
if a<b:
    sys.stdout.writelines("Kevin %s" % b)
