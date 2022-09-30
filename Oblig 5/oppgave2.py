#Lager input for navn
navn1 = input("Navn\n")

#Lager funksjonen med navn som parameter
def lagBrukernavn(navn):
    #Splitter navn som inneholder fornavn og etternavn
    navnListe = navn.split()
    #tilornder fornavn lik navnListe[0] , fordi det er kun to elementer i listen, fornavn og etternavn.
    fornavn = navnListe[0]
    #Tilordner etternavn lik andre elementet i listen som er etternavnet
    etternavn = navnListe[1]
    #Definerer brukernavn hvor vi kombinerer fornavn med siste bokstav av etternavnet
    brukernavn = fornavn + etternavn[:1]
    #Returnerer brukernavn
    return brukernavn

#Tilordner variabelen brukernavn funksjonen lagBrukernavn, med navn1 som parameter (input helt øverst)
brukernavn = lagBrukernavn(navn1)
#Ber om suffix fra bruker
suffix = input("Skriv inn suffix\n")
#Funksjon for å lage epost, tar brukernavn og suffix som parameter
def lagEpost(brukernavn, suffix):
    epost_tegn = "@"
    #Setter sammen brukernavn, @ og suffix
    epost = brukernavn+epost_tegn+suffix
    #returnerer eposten
    return epost
#Skriver ut eposten med brukernavn og suffix som argument 
print(lagEpost(brukernavn, suffix))
#Lager en ordbok med brukernavn og suffix
ordbok = {"olan":"ifi.uio.no","karin":"student.matnat.uio.no"}
#Lager funksjon som skriver ut epost for overnevnte ordboken (i prinsippet hvilken som helst, men vi bruker den over)
def skrivUtEposter(ordbok_tester):
    #Bruker for løkke til å kjøre gjennom ordboken
    for x in ordbok_tester:
        #vi henter funksjonen lagEpost med x som brukernavn (nøkkelverdi i ordbok) og ordbok_tester[x] som suffix(innholdsverdien i ordboken)
        print(lagEpost(x,ordbok_tester[x]))
#Kaller på prosedyren
skrivUtEposter(ordbok)

#Lager en tom ordbok og variabelen true
dict1 ={}
random = True
#Vi lager while løkke som kjører hele tiden, med unntak av bruker stopper den
while random != False:
    #Lager input for brukeren til å skrive inn noe, bruker lower for å gjøre dette enklere å lese inn i if-sjekken
    brukerinput = input("\nSkriv inn noe: ").lower()
   #Lager if-sjekk for bruker taster inn i,p og s
    if brukerinput == "i":
        #Ber bruker om navn(lager brukernavn med funksjonen)  og suffix, og deretter legger vi dette inn i den tomme ordboken
        brukernavn = lagBrukernavn(input("Skriv inn ditt navn: "))
        suffix = input("Skriv inn epost suffix: ")

        dict1[brukernavn] = suffix
    elif brukerinput == 'p':
        #Hvis bruker taster p skal den ta ordboken som argument og kjøre funksjonen skrivUtEposter
        skrivUtEposter(dict1)
        #Stopper programmet hvis bruker taster s
    elif brukerinput == 's':
        random = False

    

print("Du stoppa programmet")
