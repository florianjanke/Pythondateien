texteins=input("Wie heißt du?: ")
laengeeins=len(texteins)
textzwei=" Frohe Weihnachten "
laengezwei=len(textzwei)
sternchen="*"
laengedrei=int((laengezwei-laengeeins)/2)
print(sternchen*laengezwei+(2*sternchen))
print(sternchen+textzwei+sternchen)
print(sternchen+" "*laengedrei+texteins+" "*laengedrei+sternchen)
print(sternchen*laengezwei+(2*sternchen))