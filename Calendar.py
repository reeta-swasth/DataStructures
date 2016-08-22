import calendar,sys

days ={
    0:"MONDAY",
    1:"TUESDAY",
    2:"WEDNESDAY",
    3:"THURSDAY",
    4:"FRIDAY",
    5:"SATURDAY",
    6:"SUNDAY"
}

data = list(map(int,sys.stdin.readline().rstrip().split(' ')))
val = calendar.weekday(data[2],data[0],data[1])
print days.get(val)




