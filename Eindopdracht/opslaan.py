import urllib
import urllib.request
import re
from re import findall
from scipy.sparse import coo_matrix
import numpy as np

domein = 'boswell-beta.nl'
Lijst=['http://www.boswell-beta.nl/']
def Schrijffunctie(myurl):
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
                        
                elif re.search(domein, i):
                    
                    if (i in Lijst) == False:
                        Lijst.append(i)
                        
    except:
        pass

for i in Lijst:
    Schrijffunctie(i)


for i in range(len(Lijst)):
    try:
        text = open(str(i),'w')
        text.write(str(urllib.request.urlopen(Lijst[i]).read()))
    except:
        open(str(i),'w')