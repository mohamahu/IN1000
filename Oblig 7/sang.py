class Sang:
   def __init__(self,artist,tittel):
      self._tittel = tittel
      self._artist = artist

   def spill(self):
      print("Spiller",self._tittel,self._artist)
   
   def sjekkArtist(self,navn):
      navnList = navn.split()
      artistList = self._artist.split()

      for x in navnList:
         if x in artistList:
            return True
         else:
            return False
   
   def sjekkTittel(self,tittel):
      tittel = tittel.lower()
      self._tittel = self._tittel.lower()

      if tittel == self._tittel:
         return True
      else:
         return False

   def sjekkArtistOgTittel(self,artistnavn,sang_tittel):
      if self.sjekkArtist(artistnavn) and self.sjekkTittel(tittel):
         return True
      else:
         return False

    
   
   



   


      



      

