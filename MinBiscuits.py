# Enter your code here. Read input from STDIN. Print output to STDOUT

#Alice is a kindergarden teacher. She wants to give some candies to the children in her class.  All the children sit in a line ( their positions are fixed), and each  of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to save money, so she needs to minimize the total number of candies given to the children.
#Input Format
#The first line of the input is an integer N, the number of children in Alice's class. Each of the following N lines contains an integer that indicates the rating of each child.
#Constraints
#Output Format
#Output a single line containing the minimum number of candies Alice must buy.

import sys

class MinBiscuits:

    rating =[]
    candy = []
    total_children =0


    def read(self):
        self.total_children = int(sys.stdin.readline())
        for i in range (0,self.total_children,1):
            self.rating.append(int(sys.stdin.readline()))


    def find_min(self):
        self.candy.append(1)
        for i in range (1,self.total_children,1):
            self.set_min(i)

    def printd(self):
        sum =0
        for i in range(0,self.total_children,1):
            sum = sum + self.candy[i]
            print self.candy[i]
        sys.stdout.writelines("%s" %sum)


    def set_min(self,i):
        if i > 0:
            if len(self.candy)==i:
                self.candy.append(1)
            if self.rating[i] > self.rating[i-1] and len(self.candy)==i+1:
                self.candy[i] = self.candy[i-1]+1
            #if self.rating[i] == self.rating[i-1] and len(self.candy) == i+1:
             #   self.candy[i] = self.candy[i-1]
            #if self.rating[i] == self.rating[i-1] and self.candy[i]>= self.candy[i-1]:
             #   self.candy[i-1]= self.candy[i]
            if self.rating[i] < self.rating[i-1] and self.candy[i]>= self.candy[i-1]:
                self.candy[i]= self.candy[i-1]
                self.candy[i-1] = self.candy[i-1]+1
            self.set_min(i-1)

m= MinBiscuits()
m.read()
m.find_min()
m.printd()