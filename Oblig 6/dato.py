#Lager klasse
class dato:
    #Lager konstruktør med argumenter
    def __init__(self,nyDag,nyMaaned,nyttAar):
     #Definerer instansvariabler
     self._nyDag = nyDag
     self._nyMaaned = nyMaaned
     self._nyttAar = nyttAar

    
    #Lager metode som returnerer år
    def lesAar(self):
       return self._nyttAar
    #Lager en metode som gjør om datoen til en streng
    def datoString(self):
        #Tilordner alle opplysningen som ny varibalen, og gjør dem til streng med str()
        dag = str(self._nyDag)
        maaned = str(self._nyMaaned)
        aar = str(self._nyttAar)
        #Ny variabel som setter dem sammen til mer brukervennelig måte
        dato = dag+ "."  +maaned+ "." +aar
      #Returnerer dato, som er datoen i streng
        return dato

#Lager objekt
dato1 = dato(12,1,2021)
#Kaller på datostring med dato1 objekt
print(dato1.datoString())