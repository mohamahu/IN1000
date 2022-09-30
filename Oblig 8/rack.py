from node import Node

class Rack:
	## oppretter et rack der det senere kan plasseres noder
	#
 def __init__(self):
     self._liste = []

	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
 def settInn(self, node):
     self._liste.append(node)

	## Henter antall noder i racket
	# @return antall noder
 def getAntNoder(self):
     return len(self._liste)

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
 def antProsessorer(self):
    sum = 0
    for i in self._liste:
        sum += i.antProsessorer()
    return sum

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
 def noderMedNokMinne(self, paakrevdMinne):
    total = 0 
    for i in self._liste:
       if i.nokMinne(paakrevdMinne) == True:
           total+=1 
    return total
