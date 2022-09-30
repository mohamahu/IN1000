#Henter klassen Motorsykkel fra filen motorsykkel
from motorsykkel import Motortsykkel
#Lager prosedyre
def hovedprogram():
    #Lager 3 objekter
    eier1 = Motortsykkel("Honda", 56789,20)
    eier2 = Motortsykkel("Harley Davidson",45664,50)
    eier3 = Motortsykkel("bmw", 395854,90)
    #Kaller på metoden skrivUt i klassen med de tre objektene ovenfor.
    eier1.skrivUt()
    eier2.skrivUt()
    eier3.skrivUt()
    #Kaller på metoden kjør på objektet eier3, som skal legge til 10km i kilometerstanden
    eier3.kjør(10)
    #Printer ut den endelige kilometerstanden
    print(eier3.hentKilometerstand())

#Kallet på prosedyren
hovedprogram()