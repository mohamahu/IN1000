
def print_prosa(): #3  #10
    print("Melding til alle gaardeiere:") #4 Skriver ut "Melding til alle gaardeiere:" #11 Skriver ut beskjed
    print("Antall dyr paa gaarden: ")     #5 Skriver ut "Antall dyr paa gaarden: "     #12 Skriver ut beskjed


antall_dyr = 4       #1 variabelen antall_dyr er tilordnet verdien 4
print_prosa()        #2 kaller på prodedyren 
print(antall_dyr)    #6 printer variabelen antall_dyr output 4
#7 Input som ber bruker om antall dyr. Int for å gjøre om til heltall. I dette tilfellet er verdien 8
antall_nye_dyr = int(input("Hvor mange nye dyr kommer til gaarden: ")) 
antall_dyr = antall_dyr + antall_nye_dyr #8 legger sammen to verdier, som tilsvarer 12, og definerer det som antall_dyr
print_prosa() #9 kaller på prosedyren 
print(antall_dyr) #13 skriver ut summen av antall dyr på gaarden, som gir output 12

if antall_dyr > 12:     #14 her brukes det if-sjekk for å sjekke om antall_dyr er større enn 12. Denne betingelsen er usann
    print("Det er mer enn ett dusin dyr paa gaarden!") 
elif antall_dyr == 12:  #15 her sjekkes det om antall_dyr er lik 12. Denne betingelsen er sann                             
    print("Det er ett dusin dyr paa gaarden!") #16 printer ut "Det er ett dusin dyr paa gaarden!"
else:                                                  
    print("Det er mindre enn ett dusin dyr paa gaarden!") 




