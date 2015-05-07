import math
import random
import sys

try:
    N = int(sys.argv[1])
    L = float(sys.argv[2])
except: 
    print("Use: estimate_pi.py N L")
    exit(1)

if L > 1 or L < 0:
    print("AssertionError: L should be smaller than 1")
    exit(1)

if len(sys.argv) > 3:
    seed = float(sys.argv[3])
    random.seed(seed)

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
    
pi = 2*L*N / hits


print(str(hits), "hits in", str(N), "tries \nPi =", str(pi))