import time
import sys
getallen = open(sys.argv[2], 'w')
N = int(sys.argv[1])
PrimeList = list(range(0,N))
priemgetallen = []
PrimeList[1] = 0

T1 = time.perf_counter()
for i in range(1,N):
    if PrimeList[i] != 0:
        priemgetallen.append(PrimeList[i])
        getallen.write(str(PrimeList[i])+'\n')
        for j in range(2*i,N,i):
            PrimeList[j] = 0
T2 = time.perf_counter() 
getallen.close()

print('Found',len(priemgetallen), 'Prime numbers smaller than', N,'in', T2-T1, 'sec.')
