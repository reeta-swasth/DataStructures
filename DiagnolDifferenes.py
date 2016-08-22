#Given a square matrix of size , Calculate the absolute difference between the sums of its diagonals.

size = int (raw_input('Size of matrix?'))

x =[[0 for y in xrange(100)] for x in xrange(100)]
for i in range(0,size,1):
    for j in range(0, size,1):
        x[i][j]= int (raw_input("Element at %d %d" % (i,j) ))


for i in range(0,size,1):
    for j in range(0, size,1):
        print x[i][j],
    print ()

primary_diagnol_total = 0
for i in range(0, size,1):
    primary_diagnol_total = x[i][i] + primary_diagnol_total


secondary_diagnol_total = 0
for i in range(0, size,1):
        secondary_diagnol_total = x[i][(size -1) - i] + secondary_diagnol_total

print " primary_diagnol_total =",
print primary_diagnol_total
print " secondary_diagnol_total =",
print secondary_diagnol_total

absoulute_difference = abs(primary_diagnol_total - secondary_diagnol_total)

print "absoulute_difference = ",
print absoulute_difference