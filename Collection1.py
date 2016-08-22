from collections import OrderedDict
import sys


n = int(sys.stdin.readline())

data =[]
ordered_dictionary = OrderedDict()


for i in range(0,n,1):
    data = sys.stdin.readline().strip().split(' ')
    m = len(data)
    new_data = data[:m-1]
    s=''
    s = s.join(new_data)
    if ordered_dictionary.has_key(s):
        ordered_dictionary[s] = ordered_dictionary[s] + int(data[m-1])
    else:
        ordered_dictionary[s] = int(data[m-1])

print ordered_dictionary



