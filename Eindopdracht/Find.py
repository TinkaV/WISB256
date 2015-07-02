# def zoek():
#     Woorderin = []
#     GelezenRanking = open('Ranking').read()
#     for i in range(len(GelezenRanking)-2):
#         if woord in open(str(i)).read():
#             Woorderin.append(GelezenRanking[i])
                
#         else:
#             pass

# while True:
#     woord = input('Welk woord wil je zoeken?\n')
#     zoek()
import urllib
import urllib.request
import re
from re import findall
from scipy.sparse import coo_matrix
import numpy as np

GelezenLinks = open('Links').read()
Links = (GelezenLinks[2:-2]).split("', '")
GelezenPagerank = open('Pagerank').read()
GelezenPagerank = (GelezenPagerank[2:-1]).split()
Pagerank=[]
for i in GelezenPagerank:
    Pagerank.append(float(i))
    
def zoek(woord):
    for i in range(len(Links)):
        InhoudBestand=open(str(i)).read()
        if woord in InhoudBestand:
            # zoek eerst titel op
            titel = re.search(r'<title>(.*)</title>', InhoudBestand)
            # kijk of woord in titel
            if woord.lower() in titel.group(1).lower():
                # print("zit in titel")
                Pagerank[i]=Pagerank[i]*2 # Als woord in titel dan wordt pagerank vedubbeld
            # zoek hoe vaak het woord voorkomt
            aantal = InhoudBestand.count(woord)
            print(aantal)
            #Pagerank[i]=Pagerank[i]*aantal
            
            Woorderin.append([i,Links[i],Pagerank[i]]) # ipv alleen link, lijstjes met drie elementen
            
        else:
            pass

while True:
    woord = input("Welk woord wil je zoeken? (Als je klaar bent met zoeken, typ dan 'exit')\n")
    if woord == "exit":
        print("Bedankt voor het gebruiken van onze superzoekmachine, groetjes Jori en Nienke, Tinka was helaas afwezig.")
        break
    else:
        Woorderin = []
        zoek(woord)
        Woorderin=sorted(Woorderin, key=lambda x: -1*x[2]) # functie om op pagerank te sorteren, -1* om van groot naar klein te sorteren
        print(Woorderin)
