import sys

number_test = int(sys.stdin.readline())
total_elems = []
data =[]


def is_sorted(array_input):
    b =True
    for i in range(0,len(array_input)-1,1):
        if (array_input[i] > array_input[i+1]):
           b= False
    return b


# Read input data
for i in range(0,number_test,1):
    total_elems.append(int(sys.stdin.readline()))
    data.append(map(int,sys.stdin.readline().split()))

sorted_array = False

# Print input data
for i in range(0,number_test,1):
    sorted_array = False
    for j in range(0,len(data[i])-2,1):
        array_3_numbers =[]
        array_3_numbers = list(data[i][j:j+3])
        if is_sorted(array_3_numbers) == False:
            low= data[i][j]
            mid = data[i][j+1]
            high = data[i][j+2]
            data[i][j] = mid
            data[i][j+1]= high
            data[i][j+2]= low
            array_3_numbers =[]
            array_3_numbers = list(data[i][j:j+3])
            if is_sorted(array_3_numbers) == False:
                low= data[i][j]
                mid = data[i][j+1]
                high = data[i][j+2]
                data[i][j] = mid
                data[i][j+1]= high
                data[i][j+2]= low
        if is_sorted(data[i]):
            sorted_array = True
            break
    if sorted_array == True:
        sys.stdout.writelines("YES\n")
    else:
        sys.stdout.writelines("NO\n")
