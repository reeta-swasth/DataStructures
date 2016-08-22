import sys

class rotate_string:
    data_list=[]
    n =0

    def read(self):
        self.n = int(sys.stdin.readline())
        for i in range(self.n):
            self.data_list.append(sys.stdin.readline())
        self.rotate(self.n)


    def rotate(self,size):
        for i in range(size):

            for j in range(0,len(self.data_list[i])-1,1):
               k = self.data_list[i]
               m= k[j:]
               v = k[:j]
               print m
               print v
               print v.join(m)
               print "00000000000000000000000"





a= rotate_string()
a.read()