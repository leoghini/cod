#Cosa deve fare il programma:
#Catalogo Film e Prezzi (Dizionario):
#Prepara un dizionario con i film in programmazione e il prezzo del biglietto (es. "avatar": 8.50, "batman": 7.50, "inside out": 6.00).
#Menu e Selezione Film:
#Mostra i film disponibili con i prezzi.
#Chiedi all'utente quale film vuole vedere (con .strip().lower()).
#Controlla se il film esiste nel dizionario con in.
#Chiedi quanti biglietti vuole acquistare (try/except per evitare errori!).
#Integrazione Popcorn (if / else):
#Chiedi all'utente se vuole aggiungere il "Menu Popcorn & Drink" a 5.00€.
#Se risponde "sì" o "si", aggiungi 5.00€ per ogni biglietto acquistato.
#Estrazione Premio Fortuna (random.choice):
#All'acquisto, fai estrarre al sistema un piccolo regalo casuale da una lista: ["Nessun premio", "Poster in omaggio", "Buono sconto 2€", "Adesivo esclusivo"].
#Se esce il "Buono sconto 2€", sottrai 2€ dal totale!
#Scontrino Finale e Pagamento (while + try/except):
#Calcola e stampa il totale da pagare.
#Chiedi all'utente con quanti euro intende pagare.
#Attenzione: Usa un ciclo while per il pagamento! Se l'utente inserisce una cifra inferiore al totale o inserisce del testo sbagliato, chiedi di nuovo il pagamento finché non inserisce una somma sufficiente.
#Calcola e mostra il resto da consegnare

import random

catalogo = {"avatar": 8.50, "batman": 7.50, "iron man": 9.50, "deadpool": 10}
for film, prezzo in catalogo.items():
    print(f"- {film.capitalize()}: {prezzo:.2f}€")

scelta = input("Quale film tra questi gradirebbe vedere? ").strip().lower()
