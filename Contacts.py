import sys


class Contacts:

    list_contacts=[]

    def add (self,name):
        self.list_contacts.append(name)

    def find(self,name):
        count =0
        for i in range(0,len(self.list_contacts),1):
                if str(self.list_contacts[i]).startswith(name) == True:
                    count = count +1
        sys.stdout.writelines("%s\n" % count)




c= Contacts()

def add(name):
    c.add(name)

def find(name):
    c.find(name)

number_of_ops = int(sys.stdin.readline())

for i in range(0,number_of_ops,1):
    inp = sys.stdin.readline().split()
    if(inp[0] =="find"):
        find(inp[1])
    else:
        add(inp[1])








