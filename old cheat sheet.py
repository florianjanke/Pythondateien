# Ausgabe mit print()
print("Hello")
print(1+3)
print("Hello" + " " + "World!")
print("1+3=",1+3)

#Variablen zuweisen
meinName="Florian"
print(meinName)
print("meinName" + "\t" + meinName)

#Eingabe verarbeiten
print("Geben Sie Ihren Namen ein: ")
meinName= input()
print("Hallo", meinName)
deinName=input("Wie heißt du? ")
print("Hallo", "deinName")
      
#Liste
Liste1=["Wert","Wer2", "Wert3"]
print(liste1[0]) # ersten Wert abrufen

# if
bedingung = True # Bedingung muss wahr sein sonst wird sie nicht ausgeführt
if bedingung:
    #tu was
    print("Bedingun ist Wahr")
else:
    #sonst was anderes
    print("Bedingung ist Falsch")
    
#if/elif/else
vergleich="Wasauchimmer":
    #tu was wenn's stimmmt
    print(vergleich)
elif vergleich== "Wasanderes":
    #tu was wenn's stimmt
    print(vergleich)
else:
    #tu was wenn keins zutrifft
    print(vergleich)
# in
liste=[1,2,4]
if 2 in liste:
    print("Ja, 2 steht in der Liste")

# for in
for i in liste:
    #gebe jeden Wert in der Liste aus
    print(i)
#while
zaehler=0
while zaehler < 10:
    print(zaehler)
    zaehler=zaehler+ 1

#def
def sag_was(text):
    print(text)
sag_was("Hi")

#return
t=3
def sternchen(t):
    return t*3
print("t ist gleich",sternchen(t))

#Module (Bibliotheken) 
from math import sqrt
y = sqrt(2)
print(y)
