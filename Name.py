import sys

name1= sys.stdin.readline().rstrip()
name2 = sys.stdin.readline()
name2 = name2.rstrip()

sys.stdout.writelines("Hello %s %s! You just delved into python" % (name1,name2) )