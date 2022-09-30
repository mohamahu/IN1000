
#Lager prosedyre for å gi bruker riktig billett
def brukerinfo():
    #Lager input og ber bruker om alder, setter int for kun heltall
 alder = int(input("Skriv inn alder"))
 billettpris = 0
 billet_type = ""
 #Lager if-sjekk for å gi riktig pris til riktig alder, og skriver alt ut deretter
 if alder <= 17:
     billettpris = 30
     billet_type = "Barnebillett:"
 elif alder >17 and alder<63:
     billettpris = 50
     billet_type = "Ordinær:"
 elif alder >= 63:
     billettpris = 35
     billet_type = "Pensjonsbillett:"
 print(billet_type,billettpris)

 
    

#Skriver ut prosedyren
brukerinfo()


