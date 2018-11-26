# Was können wir denn?
#1. Kommentare schreiben

#2. Variablen
x = 17
lala = "blabla"

#3 Operatoren(Rechen)
x = 12 + 13
y = x - 5
hihi = "huhu" + "haha"

#4. Listen

namen = ["Hans", "Peter", "Klaus"]
x = namen[1] # Peter

# if/elif/else Verzweigung
if x == "Peter":   # == != =
    print("Hallo Peter") # Einrücken
elif x == "Hans":
    print("Hallo Hans")
elif x == 17:
    print("Es sind" + str(x) + " Katzen")
else:
    print("Hallo jemand anders")
print("Hier geht's weiter")  #Ausrücken

# for Schleifen
for x in range(0,10): # für x in 0-10, also 11 mal
    print(x)

for x in [1,2,3,4,9,8,7]: # 7 mal durchlaufen, jeweils mit x
    print(x)
    
# while-Schleifen
while x < 17:
    print("x ist kleiner als 17")
    print("denn x ist",x)
    x= x+1                       # hochzählen muss ich selber

wasauchimmer = True
while wasauchimmer == True:   # True ist ein Wert, kein Text
    print("Die Wahrheit!")
    wasauchimmer = False      # False ist auch ein Wert
    # und wir sind raus

# Funktionen
def meineFunktion():  #Funktionsdefnition bzw. Deklaration
    print("Meine tolle Funktion")
    print("Tut überhaupt nichts")
    print("Aber sie verpackt meinen Quelltext in Blöcke")
    print("Ohne Return ist es eigentlich keine Funktion")
    print("Sondern eine Prozedur")

meineFunktion() #Funktionsaufruf
meineFunktion() #Und gleich nochmal

def mFun():
    return 17 # Rückgabewert

mFun() # Sinnlos, der Wert verschwindet im Nirvana
x = mFun  #Jetzt wird der Wert(17) an x übergeben
print(x)  #Und wir können ihn verwenden

def nochNeFun(hans, klaus):  #Variablen als Parameter
    print("Hans heißt: ", hans)
    print("Peter heißt: ", klaus) #Variablennamen sind beliebig

nochNeFun("Barbara", "Heinz") # Funktionenaufruf mit Werten
x = "Peter"
lala = "Klaus"
nochNeFun(x, lala) #Funktionenaufruf mit Variablen

#import
#y = sqrt(17) # funktioniert nicht

import math # Also brauchen wir Mathe
y = math.sqrt(17) # geht

# Besser nur importieren was wir tatsächlich brauchen
# Und umbenennen wenn wir wollen
from random import randint as rint

y = rint(1,10) #Zufahlszahl 1 und 10

#Programmablaufplan
#https://de.wikipedia.org/wiki/Programmablaufplan