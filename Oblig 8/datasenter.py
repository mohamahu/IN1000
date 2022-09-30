from rack import Rack
from regneklynge import Regneklynge
from node import Node
class Datasenter:

	## Oppretter et datasenter
	#
    def __init__(self):
        self._ordbok = {}

	## Leser inn data om en regneklynge fra fil og legger
	# den til i ordboken
	# @param filnavn filene der dataene for regneklyngen ligger
    def lesInnRegneklynge(self, filnavn):
        regneklynge = open(filnavn)
        maxNode = int(regneklynge.readline())
        fil_navn_liste = filnavn.split(".")
        fil_navn = fil_navn_liste[0]
        RegneklyngeObjekt = Regneklynge(maxNode)



        for linje in regneklynge:
            #ordbok[nøkkel] = innholdsverdi
            biter = linje.split()
            AntallNoder = int(biter[0])
            minnePerNode = int(biter[1])
            AntallProsessorer = int(biter[2])


            for i in range(int(AntallNoder)):
                
                node1 = Node(minnePerNode, AntallProsessorer) 
                RegneklyngeObjekt.settInnNode(node1)
                
    
        self._ordbok[fil_navn] = RegneklyngeObjekt

	

	## Skriver ut informasjon om alle regneklyngene
	#
    def skrivUtAlleRegneklynger(self): 

        for i in self._ordbok:
            print(self._ordbok)

    ## Skriver ut informasjon om en spesifikk regeklynge
    # @param navn navnet på regnekyngen
    
    def skrivUtRegneklynge(self, navn):

        objekt = self._ordbok[navn]

        print("Informasjon om regneklyngen:",navn)
        racks = objekt.antRacks()
        print("Antall rack:",racks)
        prosessorer = objekt.antProsessorer()
        print("Antall prosessorer:",prosessorer)

    
    def nokMinne(self,paakrevd,navn):
        sjekkeMinne = self._ordbok[navn].noderMedNokMinne(paakrevd)
        
        
        print("Noder med minst",paakrevd,"GB:",sjekkeMinne)
       
        
        

        

        
        
