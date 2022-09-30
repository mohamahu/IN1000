#Lage en program som skal ta inn retter, og lag en liste med valgte retter. Be bruker om å oppgi en rett, og sjekk om det blir servert. 
#Gi bruker beskjed på begge hendelsene

#Lage input og liste med retter
matrett = input("Hvilken rett vil du ha? ")
liste = ["pizza", "taco","lasagne", "fiskerett","burger"]

tilgjengelig = False
#Lager for løkke med if sjekker. og if sjekk igjen for å gi bruker beskjed 
for i in liste:
    if matrett == i:
       tilgjengelig = True
    
if tilgjengelig:
    print("Her er " + matrett)
else:
    print("Denne matretten serverer vi ikke")

