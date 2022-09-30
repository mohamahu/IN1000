#Lager en funksjon kalt minFuksjon
def minFunksjon():
 for x in range(2): #Lager for løkker som går gjennom 0 og 1
     c=2 #tilordner veriden 2 til variabel c
     print(c) #printer ut c
     c+=1 #Her legger vi til 1 i variabelen c, som gir tallet 3
     b = 10#tilordner verdien 10 til variabelen b
     b += a #her tilordner vi b+a til variabelen b. a er ikke tilordnet noen verdi, dermed vil det oppstå error
     print(b)#printer ut b, men siden b ikke kan regnes ut, vil det ikke gi resultat
 return(b)#returnerer verdien b, men vil igjen vil det ikke ha noen hendelse pga ulovlig operasjon i linje 8

#Lager prosedyre kalt hovedprogram
def hovedprogram(): 
    a=42 #Tilordner verdien 42 til variabelen a
    b=0 #Tilordner verdien 0 til variabelen b
    print(b)#Printer b, som vil 0 i output
    b=a #Her definerer vi b lik a, altså 42
    a=minFunksjon()#Vi tilordner funksjonen "minFunksjon" til variabelen a. Dette vil gi feilmelding pga a er definert lik b.
    print(b) #printer b variabel 2 ganger 
    print(b)
#kaller prosedyren, men vil ikke kjøre pga error
hovedprogram()

