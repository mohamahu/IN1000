'''
Det skal arrangeres en festival. Mat serveres, og derfor trenger vi oversikt
over allergier til deltakerne. Lag et program som sjekker om brukeren bør unngå noen retter som følge av deres allergi.
Brukeren skal oppgi sin allergi, og print ut retter som har innhold av den 
'''
#Lager en en ordbok med allergi som nøkkelverdi, og retten som innholdsverdi
allergier = {"nøtter": "marsipankake","laktose": "milkshake", "fisk":"fiskeburger" }
#Lager input og ber Bruker oppgir sin allergi
brukerallergi = input("Hva er din allergi \n").lower()
#Bruker if-sjekk til å sjekke om brukerens allergi er i ordboken.
#Printer deretter retten som innholder brukerens allergi, hvis den har innhold i retten
if  brukerallergi in allergier:
 print(brukerallergi+" innholder i "+allergier[brukerallergi])
else:
 print(brukerallergi+" har ingen innhold i noen av våre retter")