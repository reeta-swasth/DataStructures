#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
new_array = arr



while len(new_array) > 0:
    temp_array = new_array
    smallest_elem = min(new_array)
    count =0
    for i in range(0,len(new_array),1):
        if temp_array[i] >= smallest_elem:
            temp_array[i] = temp_array[i] -smallest_elem
            count = count + 1
    new_temp_array=[]
    for i in range(0,len(new_array),1):
        if temp_array[i] > 0:
            new_temp_array.append(temp_array[i])
    sys.stdout.writelines("%s\n" % count)
    new_array = new_temp_array





