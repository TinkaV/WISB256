import urllib
import urllib.request
import re
from re import findall
from scipy.sparse import coo_matrix
import numpy as np


X=[]
row=[]
col=[]
domein = 'madurodam.nl'
Links=['http://www.madurodam.nl/']

def JoriEnNienkesSuperfunctieEnTinkaIsErNiet(myurl):
    try:
        x = urllib.request.urlopen(myurl)
        for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
            if re.search("css", i) == None and re.search("png$", i) == None and re.search("ico$", i) == None and re.search("/rss/", i) == None and re.search(".pdf$", i) == None and re.search("facebook", i)==None and re.search("twitter", i)==None and re.search("mailto", i)==None and re.search("google", i)==None and re.search(" ", i)==None and re.search("jpg", i) == None:
                if (re.search(domein, i) == None) and (re.match('www', i)==None) and (re.match('http', i) == None):
                    if re.match("/", i) == None:
                        i = "/" + i
                    i = "http://www." + domein + i
                    if (i in Links) == False:
                        Links.append(i)
                    a = (Links.index(i),Links.index(myurl))
                    if (a in X) == False:
                        X.append(a)
                        row.append(Links.index(i))
                        col.append(Links.index(myurl))
                        
                elif re.search(domein, i):
                    
                    if (i in Links) == False:
                        Links.append(i)
                    a = (Links.index(i),Links.index(myurl))
                    if (a in X) == False:
                        X.append(a)
                        row.append(Links.index(i))
                        col.append(Links.index(myurl))
                        
    except:
        pass
    
JoriEnNienkesSuperfunctieEnTinkaIsErNiet('http://www.madurodam.nl/')


for i in Links:
    JoriEnNienkesSuperfunctieEnTinkaIsErNiet(i)
    
data = len(col)*[1]
for i in range(len(col)):
    deel = col.count(col[i]) # i veranderd in col[i]
    if deel != 0:
        data[i] = 1/deel
        
n = len(Links)
pagerank = n*[1/n]
matrix = coo_matrix((data, (row, col)), shape=(n,n)).toarray()

a = 0.15
s=(n,n)
P=np.ones(s)

for i in range(10):
    v1=(1-a)*matrix.dot(pagerank)
    v2 =(a/n)*P.dot(pagerank)
    pagerank = v1+v2

text1 = open('Pagerank','w')
text1.write(str(pagerank))
print(str(pagerank))

text2 = open('Links','w')
text2.write(str(Links))
print(str(Links))

# def zoek():
#     print(len(Links))
#     for i in range(len(Links)): #-1 weggehaald
#         if woord in open(str(i)).read():
#             Woorderin.append([i,Links[i],pagerank[i]]) # ipv alleen link, lijstjes met drie elementen
            
#         else:
#             pass

# while True:
#     woord = input("Welk woord wil je zoeken? (Als je klaar bent met zoeken, typ dan 'exit')\n")
#     if woord == "exit":
#         break
#     else:
#         Woorderin = []
#         zoek()
#         Woorderin=sorted(Woorderin, key=lambda x: -1*x[2]) # functie om op pagerank te sorteren, -1* om van groot naar klein te sorteren
#         print(Woorderin)
