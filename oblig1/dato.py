#Ber bruker om å oppgi to datoer
dato1 = input("Velg en dato, og oppgi det i heltall \n")
måned1 = input("Velg måned, oppgi det i heltall \n")
dato2 = input("Velg en dato, og oppgi det i heltall \n")
måned2 = input("Velg måned, oppgi det i heltall \n")

#Her lager jeg if-sjekk for å sjekke om dato (dag) og måned er i riktig rekkefølge 
if dato1 < dato2 and måned1 <= måned2:
    #skriver ut hvis "riktig rekkefølge" hvis rekkefølgen er korrekt
    print("riktig rekkefølge")
    #sjekker her om andre oppgitte datoen er tidligere enn den første oppgitte
elif dato1 > dato2 and måned1 >= måned2:
    #printer ut resultat
    print("Feil rekkefølge")
    #Hvis ingen overnevnte stemmer, er det lik dato
else:
    #skriver ut samme dato
    print("Samme dato!")
