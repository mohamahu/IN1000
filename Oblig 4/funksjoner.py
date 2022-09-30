
#Lager en funksjon med x og y som argument. Bruker return til å gi ut en verdi
def adder(x, y):
 leggerTil = x+y
 return leggerTil


summen_av_tallene= adder(10,40)


#Printer ut funksjonen, som er tilordnet som variabel
print("\nSummen av begge tallene er: ",summen_av_tallene)
print("Summen av begge tallene er: ",summen_av_tallene)
#Tar inn et ord fra bruker, og lager en funksjon 
tekststreng = input("Skriv inn et ord\n")

bokstav = input("Skriv inn en bokstav\n")

ganger = 0

def tellForekomst(tekststreng,bokstav,ganger):
    #Lager for løkke for å sjekke om hvor mange ganger en bokstav er i ordet som ble oppgit fra bruker. Legger deretter 1 for hver gang boktaven er i ordet
    for x in tekststreng:

        if bokstav == x:
            ganger += 1

    return ("Bokstaven ",bokstav,"innholder ",ganger,"i ",tekststreng)

 

#Printer ut
forekomst = tellForekomst(tekststreng,bokstav,ganger)
print(forekomst)
'''
for x in tekststreng:
    if bokstav == x:
        ganger += 1


print("Bokstaven ",bokstav,"innholder ",ganger,"i ordet")

'''
    











 






