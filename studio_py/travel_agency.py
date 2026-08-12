#. Dati e Funzioni Iniziali
#All'inizio del file prepara i dati e due funzioni:
#Un dizionario destinazioni con i prezzi in Euro (es. "tokyo": 1200.0, "new york": 950.0, "londra": 300.0).
#Funzione 1: def calcola_preventivo(prezzo_base, persone=1)
#Calcola il prezzo totale (prezzo_base * persone).
#Se le persone sono 4 o più, applica un 10% di sconto sul totale!
#Restituisce (return) il prezzo finale.
#Funzione 2: def converti_valuta(importo, tasso)
#Restituisce (return importo * tasso).
#2. Il Ciclo Principale (while True)
#Crea un menu con 3 opzioni:
#Pianifica un viaggio
#Converti una somma in valuta locale
#Esci
#3. Logica delle Opzioni
#Se sceglie 1 (Viaggio):
#Mostra la lista delle destinazioni col ciclo for e .items().
#Chiedi la destinazione scelta (con .strip().lower()).
#Se esiste nel dizionario, chiedi in quante persone viaggiano. Proteggi l'input con try / except ValueError.
#Chiama calcola_preventivo() passando il prezzo del pacchetto e il numero di persone.
#Stampa il preventivo finale!
#Se sceglie 2 (Cambio Valuta):
#Chiedi l'importo in Euro da convertire (proteggi con try / except).
#Chiedi il tasso di cambio di destinazione (es. 1.08 per USD o 165.0 per YEN).
#Chiama converti_valuta() e stampa il risultato formattato.
#Se sceglie 3 (Esci):
#Stampa un messaggio di saluto e metti il break

destinazioni = {"tokyo": 1200.0, "new york": 950.0, "londra": 300.0}

def calcola_preventivo (prezzo_base, persone = 1):
    prezzo_totale = prezzo_base * persone
    if persone >= 4:
        prezzo_totale = prezzo_totale * 0.90 #10% di sconto
    return prezzo_totale

def converti_valuta (importo, tasso):
    return importo * tasso

while True:
    menu_opzioni = input("\nScegli: 1. Viaggio | 2. Converti Valuta | 3. Esci -> ").strip()

    if menu_opzioni == "1":
        for meta, prezzo_base in destinazioni.items():
            print(f"- {meta.capitalize()}: {prezzo_base:.2f}€")
        destinazione_scelta = input("Quale meta vuoi scegliere? ").strip().lower()
        if destinazione_scelta in destinazioni:
            try:
                persone = int(input("Per quante persone vuole prenotare? "))
                totale = calcola_preventivo(destinazioni[destinazione_scelta], persone)
                print(f"Il totale è di {totale:.2f}€")
            except ValueError:
                print("Per favore si prega di usare numeri.")
        else:
            print("Spiacenti questa destinazione non fa parte dei nostri pacchetti")

    elif menu_opzioni == "2":
        try:
            importo = float(input("Quanti euro vorresti convertire? "))
            tasso_cambio = input("Vorresti convertirli in Dollari o Yen? ").strip().lower()
            
            if tasso_cambio == "dollari":
                euro_dollaro = converti_valuta(importo, tasso=1.08)
                print(f"La cifra in dollari è di {euro_dollaro:.2f}$")
            elif tasso_cambio == "yen":
                euro_yen = converti_valuta(importo, tasso=165.0)
                print(f"La cifra in yen è di {euro_yen:.2f}¥")
            else:
                print("Valuta non disponibile. Scegli tra 'dollari' o 'yen'.")

        except ValueError:
            print("Si prega di inserire un importo numerico valido.")

    elif menu_opzioni == "3":
        print("Le auguriamo una buona giornata. A presto!")
        break

    else:
        print(f"Scelta '{menu_opzioni}' non valida. Digita 1, 2 o 3.")