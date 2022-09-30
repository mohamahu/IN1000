from datasenter import Datasenter
from regneklynge import Regneklynge

def hovedprgram():
    regnklynge1 = Datasenter()
    regnklynge1.lesInnRegneklynge("abel.txt")
    regnklynge1.skrivUtRegneklynge("abel")
    

    regnklynge1.nokMinne(32,"abel")
    regnklynge1.nokMinne(64,"abel")
    regnklynge1.nokMinne(128,"abel")

    print("")

    regnklynge2 = Datasenter()
    regnklynge2.lesInnRegneklynge("saga.txt")
    regnklynge2.skrivUtRegneklynge("saga")
    

    regnklynge2.nokMinne(32,"saga")
    regnklynge2.nokMinne(64,"saga")
    regnklynge2.nokMinne(128,"saga")


    
   


hovedprgram()


    