#Oppretter en klasse 
class Motortsykkel:
    #Definerer konstruktør 
    def __init__(self,merke,reg,km):
        #Definerer instansvariabler
        self._merke = merke
        self._reg = reg
        self._km = km
    #Lager metode kjør som legge til km til kilometerstanden
    def kjør(self, km):
        self._km += km
    #Lager metode som skal returnere den utregnende kilomerstanden etter kjør
    def hentKilometerstand(self):
        return self._km
    #Lager metode som skriver ut alle opplysningene 
    def skrivUt(self):
        print(self._merke)
        print(self._reg)
        print(self._km)

mtr = Motortsykkel("ferrari",1234,10)
mtr.kjør(20)
mtr.skrivUt()


