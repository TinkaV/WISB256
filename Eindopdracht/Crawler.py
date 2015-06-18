import urllib
import urllib.request
import re
from re import findall

myurl = "http://www.a-eskwadraat.nl"
#input("@> ")
x = urllib.request.urlopen(myurl)
for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
    print(i)
    try:
        for j in re.findall('''href=["'](.[^"']+)["']''', str(urllib.request.urlopen(str(i)).read()), re.I):
            print(j)
    except:
        pass
    