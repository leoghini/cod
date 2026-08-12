#Scrivi un programma che:
#Crea una lista chiamata giochi con 3 o 4 titoli di videogiochi in minuscolo (es. ["zelda", "mario", "pokemon"]).
#Usa un ciclo for per stampare a schermo l'elenco dei giochi disponibili.
#Fuori dal ciclo, chiedi all'utente a quale gioco vuole giocare (con .strip().lower()).
#Controlla con l'operatore in se il gioco è presente nella lista:
#Se c'è, stampa "Avvio di [nome gioco] in corso..."
#Se non c'è, stampa "Errore: [nome gioco] non è installato."

giochi = ["zelda", "mario", "pokemon"]

print("Giochi disponibili: ")

for elemento in giochi:
    print("- " + elemento)

scelta_utente = input("A che gioco vorresti giocare oggi? ").strip().lower()

if scelta_utente in giochi:
    print(f"Avvio di {scelta_utente} in corso...")
else:
    print(f"Errore! {scelta_utente} non è installato.")
