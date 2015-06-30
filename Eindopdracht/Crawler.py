import urllib
import urllib.request
import re
from re import findall
from scipy.sparse import coo_matrix
import numpy as np


X=[]
row=[]
col=[]
Lijst=['http://www.boswell-beta.nl/']
domein = 'boswell-beta.nl'
def JoriEnNienkesSuperfunctieEnTinkaIsErNiet(myurl):
    try:
        x = urllib.request.urlopen(myurl)
        for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
            if re.search("css", i) == None and re.search("png$", i) == None and re.search("ico$", i) == None and re.search("/rss/", i) == None and re.search(".pdf$", i) == None and re.search("facebook", i)==None and re.search("twitter", i)==None and re.search("mailto", i)==None and re.search("google", i)==None and re.search(" ", i)==None:
                if (re.search(domein, i) == None) and (re.match('www', i)==None) and (re.match('http', i) == None):
                    if re.match("/", i) == None:
                        i = "/" + i
                    i = "http://www." + domein + i
                    if (i in Lijst) == False:
                        Lijst.append(i)
                    a = (Lijst.index(i),Lijst.index(myurl))
                    if (a in X) == False:
                        X.append(a)
                        row.append(Lijst.index(i))
                        col.append(Lijst.index(myurl))
                        
                elif re.search(domein, i):
                    
                    if (i in Lijst) == False:
                        Lijst.append(i)
                    a = (Lijst.index(i),Lijst.index(myurl))
                    if (a in X) == False:
                        X.append(a)
                        row.append(Lijst.index(i))
                        col.append(Lijst.index(myurl))
                        
    except:
        pass
    
JoriEnNienkesSuperfunctieEnTinkaIsErNiet('http://www.boswell-beta.nl/')

# print(Lijst)
# print(len(Lijst))

for i in Lijst:
    JoriEnNienkesSuperfunctieEnTinkaIsErNiet(i)
    print(i)

data = len(col)*[1]
for i in range(len(col)):
    deel = col.count(col[i]) # i veranderd in col[i]
    if deel != 0:
        data[i] = 1/deel
        
print(data)

# for j in Lijst:
#     print(str(Lijst.index(j))+ " "+ str(j))
# print(len(Lijst))
# print(X)


v = len(Lijst)*[1/len(Lijst)]

matrix = coo_matrix((data, (row, col)), shape=(len(Lijst), len(Lijst))).toarray()

print(matrix)

a = 0.15
n = len(Lijst)
s=(n,n)
P=np.ones(s)


for i in range(10):
    v1=(1-a)*matrix.dot(v)
    v2 =(a/n)*P.dot(v)
    v = v1+v2
    # som = sum(v)
    # v = (1/som)*v

print(v)
    


