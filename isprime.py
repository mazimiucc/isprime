class prime(object):
    def isprime(self,a,b):
        A = []
        B = [item for item in range(a,b)]
        for i in range(a,b):
            for j in  range(2,i):
                if i%j == 0:
                    A.append(i)
                    break
        C = [item for item in B if item not in A]
        return C
    def listing(self):
        a = int(input("Enter min"))
        b = int(input("Enter max"))
        C = self.isprime(a,b)
        return C
    def indexing(self):
        D = []
        C = self.listing()
        for i in range(0,len(C)):
            if i%2 == 0:
                D.append(C[i])
        return print(D)
x = prime()
x.indexing()        