'''
Les inn en fil med oppgitte mål fra en skredder. Disse målene er i tommer og skal gjøres om til cm. 
Lag en funksjon som beregner fra tommer til cm. 

Sett dermed alt dette i en ordbok og print dette ut til brukeren.


'''


#Lager funksjon for formel for ommkalkulering fra tommer til cm
def tommerTilCm(antallTommer):
    cm = antallTommer*2.54
    return cm
#Lager ny funksjon med filnavn som parameter
def tester(filnavn):
 #Henter filen og tilordnes variabelen min_fil
    min_Fil = open(filnavn)
    ordbok = {}
    #For løkke som går gjennom filen 
    for x in min_Fil:
        #splitter og setter dette i en ordbok med variabelene vi definerer som maal og tall, bruker strip til å unngå mellomrom.
        biter = x.strip().split()
        maal = biter[0]
        tall = tommerTilCm(float(biter[1]))

        ordbok[maal] = tall
 #Returnerer ordboken 
    return ordbok
#Printer funksjonen med filen vår
print(tester('test.txt'))
