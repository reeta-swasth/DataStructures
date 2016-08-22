import sys

class list_replication:
    data_list=[]
    s =0
    n =0

    def read(self):
        self.s = int(sys.stdin.readline())
        self.n = int(sys.stdin.readline())
        for i in range(self.n):
            self.data_list.append(int(sys.stdin.readline()))
        self.elaborate(self.n,self.s)


    def elaborate(self,size,times):
        new_list=[]
        for i in range(self.n):
            for j in range(self.s):
                new_list.append(self.data_list[i])

        for i in range(self.n * self.s):
                print new_list[i]

a= list_replication()
a.read()


