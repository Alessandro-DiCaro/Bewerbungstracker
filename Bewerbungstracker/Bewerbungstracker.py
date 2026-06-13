#Um daten zu speichern und abzurufen.
import json

# Ermöglicht den Zugriff auf aktuelles Datum und Uhrzeit.
from datetime import datetime

try:
    with open("bewerbungen.json", "r") as datei:
        bewerbung = json.load(datei)
except FileNotFoundError:
    bewerbung = []

#Liste/Dictionary
Stellenanzeige = [
    {
        "firma": "Google",
        "beruf": "Softwareentwickler",
        "status": "Offen",
    },
    {
        "firma": "Amazon",
        "beruf": "Datenanalyst",
        "status": "Offen",
    },
    {
        "firma": "Microsoft",
        "beruf": "Projektmanager",
        "status": "Offen",
    }
]

def offene_stellen_anzeigen():
    print("\nOffene Stellen:", end=" ") #end=" " : Gibt die nächste Ausgabe in derselben Zeile aus
    print(len(Stellenanzeige))
    for nummer, job in enumerate(Stellenanzeige, start= 1):     # for durchläuft alle Elemente der Liste Stellenanzeige.
        print("----------------------------")                   # enumerate() liefert dabei zwei Werte:
        print(nummer)                                           # nummer = die Position des Elements (0, 1, 2, ...)
        print(f"Firma: {job['firma']}")                         # job = das aktuelle Dictionary mit Firma, Beruf und Status
        print(f"Beruf: {job['beruf']}")
        print(f"Status: {job['status']}")
        print()

def bewerbung_hinzufügen():
    for nummer, job in enumerate(Stellenanzeige, start= 1):
        print("\n", nummer, job['firma'])
    print("\n Welche Stelle möchtest du auswählen") 

    try:
        # Benutzereingabe in eine Zahl umwandeln.
        auswahl = int(input("\n""Nummer: ")) 

    except ValueError:
        print("\n""Bitte eine Zahl eingeben.")
        return

    # Prüft, ob die eingegebene Nummer gültig ist.
    # Bei 3 Stellen sind also 1, 2 oder 3 erlaubt.  
    if auswahl >= 1 and auswahl <= len(Stellenanzeige):

        #1 wird abgezogen weil Listen bei 0 beginnen.
        firma = Stellenanzeige[auswahl - 1]["firma"]

        # Prüft, ob bereits eine Bewerbung für diese Firma existiert.
        if any(eintrag["firma"] == firma for eintrag in bewerbung):
            print("\n""Bereits Beworben")
            return

        datum = datetime.now().strftime("%d.%m.%Y")

        # Fügt eine neue Bewerbung zur Liste hinzu.
        bewerbung.append({
        "firma": firma,
        "status": "Beworben",
        "datum": datum
        })

        # Speichert die aktualisierte Liste
        # in der JSON-Datei.
        with open("bewerbungen.json", "w") as datei:
            json.dump(bewerbung, datei, indent=4)         
        print("\nBewerbung hinzugefügt.")
    else:
        print("\n""Ungültige Eingabe. Bitte versuche es erneut.")
                
def alle_bewerbungen_anzeigen():
    while True:
        global bewerbung
        print("\nDeine Bewerbungen:")

        for b in bewerbung:
            print("\n"f"Firma: {b['firma']}")
            print(f"Status: {b['status']}")
            print(f"Datum: {b['datum']}")          
            
        # Nur weitermachen, wenn es gespeicherte Bewerbungen gibt
        if len(bewerbung) > 0:
            print("\nMöchtest du eine bewerbung löschen? ja (1) oder nein (2)")
            antwort = input("auswahl: ")

            if antwort == "1":
                firma_loeschen = input("Welche Bewerbung möchtest du löschen? (Gib den Firmennamen ein): ")                       
                bewerbung = [                             
                    b for b in bewerbung                  # Es werden alle Bewerbungen behalten,
                    if b["firma"] != firma_loeschen]      # deren Firmenname NICHT dem eingegebenen Namen entspricht.
                
                # Neue Liste in JSON-Datei speichern.
                with open("bewerbungen.json", "w") as datei:        
                    json.dump(bewerbung, datei, indent=4)
                    print("\nBewerbung gelöscht.")
                    break

            elif antwort =="2":
                break
        else:
            print("\nKeine Bewerbungen")
            break

def beenden():
        print("\nProgramm wird beendet.")
        exit()

while True:
    print("\n===== Bewerbungstracker =====")
    print("1. Offene Stellen anzeigen")
    print("2. Bewerbung hinzufügen")
    print("3. Alle Bewerbungen anzeigen")
    print("4. Beenden")

    auswahl = input("Auswahl: ")

    if auswahl == "1":    
        offene_stellen_anzeigen()

    elif auswahl == "2":
        bewerbung_hinzufügen()

    elif auswahl == "3":
        alle_bewerbungen_anzeigen()
    
    elif auswahl == "4":
        beenden()
    else:
        print("Ungültige Auswahl.")