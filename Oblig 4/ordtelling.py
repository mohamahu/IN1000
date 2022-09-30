#Lager input og ber bruker om ord
streng = input("Skriv inn et ord\n")
#Deretter lager jeg en funksjon, og bruker return til å returnere lengden av ordet
def bokstavteller(streng):
    return len(streng)

print(bokstavteller(streng))

#Lager input og ber bruker om en setning, og lager en tom ordbok
input = input("Skriv inn en setning")

ordbok = {}
#Lager en funksjon som skal sjekke ut antall ord i en setning 
def ordteller(string):
    #Deler opp alle ordene med split(), slik at alle ordene er separert i listen antall_ord
    antall_ord = string.split()
    #Lager dobbel for løkke, hvor "i" går gjennom i listen, og samtidig tilorder jeg sum_ord lik 0 
    for i in antall_ord:
        sum_ord = 0
       #Lager ny for løkke for å sjekke om hvor mange ganger ordet "i" er gjentatt i listen. i == j , legger vi til 1 i sum_ord som er innholdsverdien. 
        for j in antall_ord:
            if i == j:
                sum_ord += 1
      
        #Setter inn i ordboken, og printer ut
        ordbok[i] = sum_ord
     
    print(ordbok)
      


#Kaller på funksjonen 
print(ordteller(input))