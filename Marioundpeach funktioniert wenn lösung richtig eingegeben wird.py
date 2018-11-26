Raum1=["links","hoch"]
Raum2=["hoch","rechts"]
Raum3=["runter","links"]
Schloss=["Raum1","Raum2","Raum3",]

print("Mario ist in einer gefährlichen Welt auf der Suche nach Peach. Peach ist in Raum3.\nMario startet in Raum1. Hilf Mario Peach zufinden bevor Bowser Sie vernichtet! \nDu kannst nach oben, unten, rechts oder links laufen.\n")
eingabe=input("In Welche Richtung soll Mario gehen?\n")
if eingabe == "links" :
    print("Du hast es in Raum2 geschafft!\n")
    print("Bitte wähle erneut in Welche Richtung du gehen möchtest.")
   
elif eingabe == "hoch":
    print("Du wurdest von einem bösen Orc getötet. bitte starte das Spiel erneut")
else :
    print("Das war die verkehrte Richtung, bitte starte das Spiel erneut")
eingabe=input("Wähle zwischen hoch oder rechts\n")
if eingabe == "hoch" :
    print("Du läufst in Raum 3 rein siehst einen Oger und ziehst dein Schwert. Was tust du?")
else:
    print("Du läufts zurück in Raum 1. Bitte starte das Spiel neu und denke nach wolang du läufst!\n")

oger=input("Wähle zwischen Schwertangriff, rutschen oder fliehen\n")
if oger == "rutschen" :
    print("Du rutscht zwischen den Beinen des Ogers durch und bist erfolgreich in einem sicheren Teil des Raumes angekommen. Du schaust dich um. Nach kurzer Zeit entdeckst du Peach \nin der Ecke gefesselt. Du hast es geschafft glückwunsch.")
    
elif oger == "Schwertangriff":
    print("Du rennst auf den oger hinzu. Du triffst ihn mit deinem Schwert am linken arm")
    print("Der Oger ist wütend. Er greift dich am Kopf und zerquetscht dich")
    print("Bitte starte das Spiel erneut")
else:
    print("Du versuchst zu fliehen, doch der Oger zieht sein Pfeil und Bogen und tötet dich.") 