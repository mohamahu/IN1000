#Legger beboer og retter i en ordbok
måltid = {"ola gunnar":["Brød, baguett, fisk"], "petter petterson":["Egg, ris, suppe"]}
#Lager en prosedyre 
def matplan():
 #skriver ut beboer bruker kan velge mellom, og ber bruker om å velge en beboer
 beboer = måltid.keys()
 print(beboer)
 velgBeboer = input("Skriv inn en beboer \n").lower()
 #Lage if-sjekk til å sjekke om beboer finnes i ordboken.
 #Deretter skriver den ut innholdsverdiene til nøkkelverdien
 
 if velgBeboer in måltid:
     print(måltid[velgBeboer])
 else:
     print("Beboer ikke registrert")
    

#Kjører prosedyren
matplan()

'''
a. Jeg ville ha brukt liste for å lagre brukenavn til elevene i in1000.
Det er fordi det er en gitt verdi, som kan lagres i en liste. 
Den har ingen innholdsverdi, og kan derfor bare settes i en liste.

b. For å brukenavn og poeng ville jeg ha brukt ordbok, og settet brukenavn som nøkkelverdi og poeng som innholdsverdi.
Grunnen til dette er fordi hver bruker har egen/unike poeng som kan bare forholdet seg til den ene brukeren.

c. For alle vinnerne i lotto ville jeg brukt liste. Det er bare antall vinnere som skal nevnes, og ingen tilknyttet verdi.

d. For allergi ville jeg brukt mengde. Dette fordi flere kan ha samme allergi.
Derfor kan vi skrive ut allergien en gang, selv om det er flere som har det. 


'''

