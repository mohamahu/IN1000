#Lager tom liste og brukerinput 1, og starter while løkken som kjører helt til bruker taster inn 0
liste = []
brukerInput = 1
while brukerInput != 0:
    brukerInput = int(input("Skriv inn et heltall\n"))
    #Legger til tallene i listen 
    liste.append(brukerInput)

#Hvis bruker taster null, printer dette ut
print("Du tastet 0")
minSum = 0

#Lager for løkke, som legger til alle tallene i listen
for x in liste:
    minSum += x
 
print(minSum)


størst = 0
minst = 0

for z in liste:
    if z<minst:
        minst=z

print(minst)


for y in liste:
 if y > størst:
     størst=y

print(størst)








