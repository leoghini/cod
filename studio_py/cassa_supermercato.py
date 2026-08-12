#Cosa deve fare il programma:
#Listino Prezzi: Un dizionario iniziale con almeno 5 prodotti e i relativi prezzi (es. "pane": 1.50, "latte": 1.20, ecc.).
#Mostrare il Menu: Stampare a schermo i prodotti disponibili con i loro prezzi.
#Il Carrello (Ciclo while):
#Chiedi all'utente cosa vuole comprare (usando .strip().lower()).
#Se il prodotto è presente nel listino, chiedi la quantità e aggiungi il costo al totale.
#Se non è presente, avvisa l'utente.
#Se l'utente scrive "fine", il ciclo si interrompe (break).
#Sorpresa della Giornata (random):
#Genera un numero casuale tra 5 e 20 con random.randint(). Sarà la percentuale di sconto della giornata!
#Calcola il totale scontato.
##Pagamento sicuro (try / except):
#Chiedi con quanti euro paga il cliente.
#Gestisci l'eventuale errore se inserisce testo invece di un numero.
#Calcola il resto da restituire.

import random

listino = {"pane": 1.50, "latte": 1.20, "cereali": 2.25, "olio": 5.12, "sale": 1.15}

print("Nel nostro negozio sono disponibili i seguenti articoli:")
for prodotto, prezzo in listino.items():
    print(f"- {prodotto.capitalize()}: {prezzo:.2f}€")

totale = 0.0
carrello = []

while True:
    scelta = input("\nCosa vorresti comprare? (scrivi 'fine' per terminare): ").strip().lower()
    
    if scelta == "fine":
        print("\nGrazie per aver fatto la spesa da noi!")
        break
    elif scelta in listino: 
        try:
            quantita = int(input(f"Quanti/e {scelta} vorresti prendere? "))
            
            if quantita <= 0:
                print("Inserisci una quantità maggiore di zero!")
                continue

            prezzo_unita = listino[scelta]
            costo_articolo = prezzo_unita * quantita
            totale += costo_articolo
            
            carrello.append(f"{scelta} x{quantita} ({costo_articolo:.2f}€)")
            
            print(f"Aggiunto! Subtotale attuale: {totale:.2f}€")
        except ValueError:
            print("Errore: Inserisci un numero intero valido per la quantità!")
    else:
        print("Spiacente, prodotto non disponibile.")

print("\n" + "="*30)
print("SCONTRINO FISCALE")
print("="*30)
for voce in carrello:
    print(f"• {voce}")
print(f"\nTOTALE DA PAGARE: {totale:.2f}€")
