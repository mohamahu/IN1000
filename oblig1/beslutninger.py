#Lager input og spør bruker vil ha brus, og bruker ".lower()" komandoen for å oversette alt til små bokstaver 

brus = input("Vil du ha drikke (Ja/Nei) \n").lower()

#lager if-test for å gi riktig beksjed til brukeren, lager to if-sjekker som sjekker om bruker svarer ja eller nei, og skriver ut riktig beskjed 
if brus == "ja":
    print("Her har du en brus")

if brus == "nei":
    print("Den er grei")