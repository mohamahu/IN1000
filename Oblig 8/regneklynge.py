from rack import Rack
## Klasse for representasjon av regneklynge i et datasenter.
#
class Regneklynge:
	## Oppretter en regneklynge og setter maks antall
	# det er plass til i et rack
	# @param noderPerRack max antall noder per rack
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._rackListe = []

		

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
    def settInnNode(self, node):
          
            if  len(self._rackListe) == 0:
                nyRack = Rack()
                nyRack.settInn(node)
                self._rackListe.append(nyRack)
        
            elif self._rackListe[len(self._rackListe)-1].getAntNoder() < self._noderPerRack:
                self._rackListe[len(self._rackListe)-1].settInn(node)
            else:
                nyRack = Rack()
                nyRack.settInn(node)
                self._rackListe.append(nyRack)
        

                

	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
    def antProsessorer(self):
        sum = 0
        for i in self._rackListe:
            sum += i.antProsessorer()
        return sum

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        total = 0 
        for i in self._rackListe:
            total += i.noderMedNokMinne(paakrevdMinne)
        
        return total


	## Henter antall racks i regneklyngen
	# @return antall racks
    def antRacks(self):
        return len(self._rackListe)