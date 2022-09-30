
#Funksjon for addisjon med x og y som paramatere
def addisjon(x,y):
   return x + y
 
#bruker assert til å sjekke tallene nedenfor stemmer.
#Dermed kan vi være sikre på at funksjonen fungerer på riktig måte
assert addisjon(20,30) == 50
assert addisjon(-10,-10) == -20
assert addisjon(-10,40) == 30
#Tilordner funksjonen addisjon variabelen sum
sum = addisjon(10,10)

print(sum)

#lager funksjon substraksjon 
def substraksjon(x,y):
    return y-x
#Tester funksjonen fungerer med assert
assert substraksjon(30,50) == 20
assert substraksjon(-40,-40) == 0
assert substraksjon(-30,40) == 70
#Printer med to gitt verider
print(substraksjon(10,50))

#lager funksjon divisjon
def divisjon(x,y):
    return x/y

#Tester med assert om funksjonen fungerer

assert divisjon(15,3) == 5
assert divisjon(-100,10) == -10
assert divisjon(-36,-6) == 6

#printer med to gitt verdier

print(divisjon(20,5))
#Funksjon for å regne fra tommer til cm, setter inn formel inn og returnerer i cm
x = float(input("Skriv inn antall i tommer\n"))
def tommerTilCm(anallTommer):
    assert anallTommer> 0
    cm = anallTommer*2.54
    return cm
    
print(tommerTilCm(x))
#Lager prosedyre for svar setningene
def skrivBeregninger():
 brukertall = float(input("Skriv inn et tall: \n"))
 brukertall1 = float(input("Skriv inn et tall: \n"))
 add = addisjon(brukertall,brukertall1)
 sub = substraksjon(brukertall,brukertall1)
 div = divisjon(brukertall,brukertall1)
 print("Resultat av summering:",add)
 print("Resultat av substraksjon:",sub)
 print("Resultat av divisjon:",div)

 print("Konvertering fra tommer til cm:\n")
 brukerTommer = float(input("Skriv inn et tall:\n"))
 cm = tommerTilCm(brukerTommer)
 print("Resultat:",cm)


skrivBeregninger()

