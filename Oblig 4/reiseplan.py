#Lager lister for hver enkelt av de tre tingene
steder = []
klesplagg = []
avreisedatoer = []
#Lager for løkke med range 5, pga vi skal spørre bruker noe om 5 ganger
for x in range(5):
 steder.append(input("Skriv inn et sted\n"))
 klesplagg.append(input("Skriv inn klesplagg\n"))
 avreisedatoer.append(input("Skriv inn et din avreisedato\n"))

 
#Legger alt til i listen reiseplan
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)
#Lager for løkke for å la bruker skrive ut fra listene. 
for x in reiseplan:
 print(x)
#liste_indeks1 er nr. bruker skriver for å hente en spesifikk liste
liste_indeks1 = int(input("Skriv inn et helttall 0-2"))
#liste_indeks2 er nr. bruker oppgir for å hente spesifikt element i listen
liste_indeks2 = int(input("Skriv inn et helttall 0-4"))
#If sjekk for å sjekke om tallet oppgitt er innenfor rekkeviden
if liste_indeks1 <= 2 and liste_indeks1 >= 0 and liste_indeks2 <= 4 and liste_indeks2 >= 0:
    print(reiseplan[liste_indeks1][liste_indeks2])
else: 
    print("Ugyldig input")


