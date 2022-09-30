'''
Lag et program hvor vi tar inn en stundent som parameter, og antall poeng.
Poengene skal være basert på en nylig prøve.
Programmet skal ta inn et navn og antall poeng, og sjekke om bruker består prøven med 50 poeng(eller mer) av 100, eller ikke.
Hvis under 50 er det ikke bestått.
Returner Bestått hvis godkjent, eller ikke bestått hvis ikke godkjent. 

Lag et objekt og sjekk om dette fungerer. 
'''

class elev: 
    def __init__(self, navn, poeng):
        self._navn = navn
        self._poeng = poeng
    
    def sjekk(self):
        b = self._navn+" fikk bestått"
        ib = self._navn+" fikk ikke bestått"
        if self._poeng >= 50:
            print (b)
        else:
            print(ib)
    
    
elev1 = elev("Gunnar",60)
elev1.sjekk()