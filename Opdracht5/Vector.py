from array import array

class Vector(object):
    def __init__(self,n,other=0):
        if isinstance(other, float):
            self.vector = array('d',n*[other])
        else:
            self.vector = array('d',other)
        self.n = n
        
    def __str__(self):
        opscherm = ''
        for i in range(self.n):
            opscherm += str(self.vector[i]) + '\n'
        return(opscherm)

    def lincomb(self,other,alpha,beta):
        c = array('d',[])
        for i in range(self.n):
            a = alpha*self.vector[i]
            b = beta*other.vector[i]
            c.append(a+b)
        return(Vector(self.n,c))

    def scalar(self,alpha):
        d = self.lincomb(self,alpha,0)
        return(d)
    
    def inner(self,other):
        x = 0
        for i in range(self.n):
            x += self.vector[i]*other.vector[i]
        return(x)
    
    def norm(self):
        f = self.inner(self)
        return(f**0.5)
        

