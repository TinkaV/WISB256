import math
import random
import sys

N = int(sys.argv[1])
L = int(sys.argv[2])

def drop_needle(L):
    x0 = random.random()
    y0 = random.random()
    a = random.vonmisesvariate(0,0)
    x1 = x0 + L*math.cos(a)
    y1 = y0 + L*math.sin(a)
    
    if x1 >= 1 or x1 <= 0:
        return True
    else:
        return False
      
i = 0
hits = 0
while i < N:
    if drop_needle(L):
        hits = hits + 1
    i = i + 1
    
print(hits)
