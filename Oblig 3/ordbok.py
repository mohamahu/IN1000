#Legger inn ordboken som gitt i oppgaven, og printer det ut
varerlinjer = {"melk":14.9, "brød": 24.9, "yogurt":12.9, "pizza": 29.9}

print(varerlinjer)
#Ber bruker om å skrive inn en vare og pris. Bruker float for desimaltall. 
#Legger deretter info inn i ordbokenm og skriver ut
varerprodukt = input("Skriv inn vare \n")
varepris = float(input("Skriv inn pris(bruke komma med punktum) \n"))
varerlinjer[varerprodukt] = varepris

print(varerlinjer)