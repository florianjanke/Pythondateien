spielen = True
#eingabe = ''

print("Mario ist in einer gefährlichen Welt auf der Suche nach Peach. Peach ist in Raum4. \nMario startet in Raum1. Hilf Mario Peach zufinden bevor Bowser Sie vernichtet! \nDu kannst nach oben, unten, rechts oder links laufen.\n")
print("In Welche Richtung soll Mario gehen?\n")
while spielen == True:
    eingabe = input()
    if eingabe == ( "links"):
        spielen = False
        print("Du hast es in Raum2 geschafft!\n")
        break
   # if input() == "hoch":
    elif eingabe == "hoch" :
        print("Du gehst in ein Raum hinein und es ist sehr dunkel. Du schaltest das Licht an \nund siehst einen Orc der dich sofort angreift und tötet. Bitte versuche es \nerneut.") 
    else :
        print("Das war die verkehrte Richtung.")
        
        
        
        
        
        

while True:
    eingabe=input("Wähle zwischen hoch oder rechts\n")
    if eingabe == "hoch" :
       print("Du läufst in Raum 3 rein siehst einen Oger und ziehst dein Schwert. Was tust du?")
    else:
       print("Du läufst in Raum 3 rein siehst einen Oger und ziehst dein Schwert. Was tust du?\n")

    eingabe=input("Wähle zwischen Schwertangriff, rutschen oder fliehen\n")
    if eingabe == "rutschen" :
        print("Du rutscht zwischen den Beinen des Ogers durch und bist erfolgreich in einem sicheren Teil des Raumes angekommen. Du siehst dich um nach kurzer Zeit entdeckst du Peach.\nGame Won.(Dieses Level kannst du endlos wiederholen.)")
    
    elif eingabe == "Schwertangriff":
        print("Du rennst auf den Oger hinzu. Du triffst ihn mit deinem Schwert am linken arm")
        print("Der Oger ist wütend. Er greift dich am Kopf und zerquetscht dich. Dieses Level kann endlos weiter gespielt werden.")
    else:
        print("Du versuchst zu fliehen, doch der Oger zieht sein Pfeil und Bogen und tötet dich.")