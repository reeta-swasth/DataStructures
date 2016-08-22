# A jail has prisoners, and each prisoner has a unique id number, , ranging from to . There are sweets that must be distributed to the prisoners.
# The jailer decides the fairest way to do this is by sitting the prisoners down in a circle (ordered by ascending ), and then, starting with some random , distribute one candy at a time to each sequentially numbered prisoner until all candies are distributed. For example, if the jailer picks prisoner , then his distribution order would be until all sweets are distributed.


import sys

test = sys.stdin.readline()
data = sys.stdin.readline().split()
total_prisoners = int(data[0])
total_sweets = int(data[1])
sequene_start_main = int(data[2])
sequene_start = sequene_start_main -1



list= []

while total_sweets > 0:
        if sequene_start < total_prisoners:
            sequene_start = sequene_start +1
        else:
            sequene_start = 1
        total_sweets = total_sweets -1


sys.stdout.write("%s" %sequene_start)
