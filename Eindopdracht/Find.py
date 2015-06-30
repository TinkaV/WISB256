import Crawler.py

woord = input('Welk woord wil je zoeken?\n')

# def check():
#     for i in range(len(Lijst)):
#         files = file(i)
#         if woord in files:
#             return True
#         return False

Woorderin = []
      
def check():
    for i in range(len(Lijst)):
        if woord in open(str(i)).read():
            Woorderin.append(Lijst[i])
            
        else:
            pass


check()

        
