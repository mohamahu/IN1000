#1. Jeg tror koden ikke vil kjøre pga if-setningen er ikke komplett. En if-sjekk består av if betingelse og else(eller elif)
#2. Koden kjører input og bruker skriver inn et tall, og deretter definerer vi tallet oppgitt som int i variabelen b. 
# Når den går til if-sjekken kontrollerer den om betingelsen er sann eller usann. 
# Men siden if-sjekken er ufullstending vil den ikke kjøre if-sjekken


a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")

