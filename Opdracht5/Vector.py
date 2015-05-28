class Vector(object):
    def __init__(self,n,other):
        self.len = n
        if isinstance(other, float):
            self.vector = n*[other]
        elif isinstance(other, list):
            self.vector = [float(i) for i in other]
        else:
            self.vector = n*[0.0]
            
        
    def __str__(self):
        opscherm = ''
        for i in range(self.len):
            opscherm += str(self.vector[i]) + '\n'
        return(opscherm)


