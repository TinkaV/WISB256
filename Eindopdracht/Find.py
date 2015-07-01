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


GelezenLinks = open('Links').read()
Links = (GelezenLinks[2:-2]).split("', '")
GelezenPagerank = open('Pagerank').read()
GelezenPagerank = (GelezenPagerank[2:-1]).split()
Pagerank=[]
for i in GelezenPagerank:
    Pagerank.append(float(i))
    
def zoek():
    for i in range(len(Links)):
        if woord in open(str(i)).read():
            Woorderin.append([i,Links[i],Pagerank[i]]) # ipv alleen link, lijstjes met drie elementen
            
        else:
            pass

while True:
    woord = input("Welk woord wil je zoeken? (Als je klaar bent met zoeken, typ dan 'exit')\n")
    if woord == "exit":
        print("Bedankt voor het gebruiken van onze superzoekmachine, groetjes Jori en Nienke, Tinka was helaas afwezig")
        break
    else:
        Woorderin = []
        zoek()
        Woorderin=sorted(Woorderin, key=lambda x: -1*x[2]) # functie om op pagerank te sorteren, -1* om van groot naar klein te sorteren
        print(Woorderin)
