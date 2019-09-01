""" Der ISBN-Prüfer, eingegeben wird neun stellige Zahl.
        Ausgabe ist eine ISBN Ziffer.
        Autor: Mohamad Shaftar
        01.09.2019 """

eingabe = input("Bitte geben zehn Zahlen ein, zur Prüfung eine isbn Zahl: ") # Eingabe feld
while len(eingabe) != 9: # Eingabe richtig oder falsch?
    print("Bitte versuchen Sie nochmal. Geben Sie 10 Zahlen ein: ") # Eingabe wiederholen!
    eingabe = input('>> ')
    continue # Wenn die Einagabe richtig ist, soll weiter gehen
else:
    summe = 0 # Ein anfang Wert
    for i in range(0, 9): # Schleife zur Rechnung alle eingegbene Zahlen
        digit = int(eingabe[i]) * (i + 1) # i wird um Eins erhöht, vorlaeufige speicher
        summe = summe + digit # Die Summe wird in jedem FOR Ablauf gespeichert.
    mod = summe % 11 # Die Modulo
    isbnNummer = str(mod) # Modulo zu String
print("Die ISBN Ziffer ist: *" + isbnNummer + "*") # Die Ausgabe
