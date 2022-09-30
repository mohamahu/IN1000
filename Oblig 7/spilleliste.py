from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []   
        self._navn = listenavn

    def lesFraFil(self,filnavn):
        fil = open(filnavn)

        for x in fil:
            alleData = x.strip().split(';') 
            tittel = alleData[0]
            artist = alleData[1]
            self._sanger.append(Sang(artist, tittel))
     
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)
    
    def fjernSang(self,sang):
        self._sanger.remove(sang)
        
    def spillSang(self,sang):
        sang.spill()

    def spillAlle(self):
        for i in self._sanger:
            i.spill()
    
    def finnSang(self,tittel):
        for x in self._sanger:
            if x.sjekkTittel(tittel):
                return x
        return None

    def hentArtistUtvalg(self,artistnavn):
        sangliste = []
        for x in self._sanger:
            if x.sjekkArtist(artistnavn):
                sangliste.append(x)
        return sangliste