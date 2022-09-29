#Lag en applikasjon som beregner om tillatelse for oppføring av bygg for rammetillatelse i oslo kommune.
#Altså det er kun lov å oppføre bygg med et areal på 80 kvm. Brukeren skal skrive inn målene på tomten, 
# og applikasjonen skal beregne om det er lov å oppføre bygg på tomten.
#Lag program som tar inn mål av ønskende bygg på tomten
lengde = int(input("Skriv inn lengden av bygget du ønsker oppført \n"))
bredde = int(input("Skriv inn brdden av bygget du ønsker oppført \n"))
areal_grense = 80
areal = lengde*bredde

if areal<= areal_grense:
  print("Ditt ønskende bygg på",areal,"kvm kan oppføres")



else:
   differanse = areal-areal_grense
   print("Du kan ikke oppføre ditt bygg, den er",differanse,"kvm over grensen")


