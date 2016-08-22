import sys


class EvenOdd:

    list =[]
    def read(self):
        n = int(sys.stdin.readline())
        self.list = map(int,sys.stdin.readline().split())
        q = int(sys.stdin.readline())

        main_data =[[0 for y in xrange(2)] for x in xrange(100000)]

        for i in xrange(q):
            data = map(int,raw_input().split())
            m=0
            for j in range(0,2,1):
                main_data[i][j] = data[m]
                m= m +1
            i= i +1

        for i in xrange(q):
            val =self.find(main_data[i][0]-1,main_data[i][1]-1)
            if val %2 ==0:
                sys.stdout.writelines("Even\n")
            else:
                sys.stdout.writelines("Odd\n")
            i= i +1



    def find(self,x,y):
        if(x>y):
            ans =1
        else:
            sys.stdout.writelines("%s, %s %s\n" % (self.list[x],x+1,y))
            ans = pow(self.list[x],self.find(x+1,y))
        return ans


e = EvenOdd()
e.read()