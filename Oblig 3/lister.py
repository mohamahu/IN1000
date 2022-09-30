#Lager liste med tre verdier, og bruker append til å legge til verdien 6.
#Printer ut tilslutt

liste = [2,5,7]
liste.append(6)
print(liste[0], liste[2])

#Ber bruker om 4 navn
brukernavn1 = input("Skriv inn et navn \n").lower()
brukernavn2 = input("Skriv inn et navn \n").lower()
brukernavn3 = input("Skriv inn et navn \n").lower()
brukernavn4 = input("Skriv inn et navn \n").lower()

#Lager en liste av alle navn fra bruker, og printer ut 
list1=[brukernavn1,brukernavn2,brukernavn3,brukernavn4]

print(list1)


#Bruker if-sjekk for sjekke "amir" blir nevnt. Bruker count for å telle om navnet er i listen
mitt_navn = "amir"

if list1.count(mitt_navn) >= 1:
    print("Du husker meg")

else:
    print("Du glemte meg")

#Henter verdiene via index, og legger dem sammen
sum = liste[0]+liste[1]+liste[2]+liste[3]
#Henter verdiene fra listen og multipliserer dem
produkt = liste[0]*liste[1]*liste[2]*liste[3]
#printer alt ut
print("Sum: ",sum,"Produkt: ",produkt)
