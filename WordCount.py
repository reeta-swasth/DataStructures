from collections import OrderedDict
import sys


n = int(sys.stdin.readline())

data =[]
ordered_dictionary = OrderedDict()


for i in range(0,n,1):
    data.append(sys.stdin.readline().strip())
    s = data[i]
    if ordered_dictionary.has_key(s):
        ordered_dictionary[s] = ordered_dictionary[s] + 1
    else:
        ordered_dictionary[s] = 1

new_count_list = list(ordered_dictionary.values())

sys.stdout.writelines("%s\n" %len(new_count_list))

for i in range(0,len(new_count_list),1):
    sys.stdout.writelines("%s " %new_count_list[i])
