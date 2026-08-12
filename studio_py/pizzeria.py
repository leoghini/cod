#Scrivi un programma che:
#Crea un dizionario chiamato pizze con 3 pizze e i loro prezzi espressi come decimali (es. "margherita": 6.0, "diavola": 7.5, "capricciosa": 8.0).
#Usa un ciclo for per mostrare il menu. Per accedere sia al nome che al prezzo puoi usare .items():
#for nome, prezzo in pizze.items():
#    print(f"- {nome}: {prezzo}€")
#Chiedi all'utente quale pizza vuole ordinare (.strip().lower()).
#Controlla se la pizza è presente nel dizionario (if scelta in pizze:):
#Se c'è, recupera il prezzo con pizze[scelta] e stampa: "Ottima scelta! Il prezzo della [scelta] è [prezzo]€."#
#Se non c'è, stampa "Spiacenti, non abbiamo questa pizza."

pizze = {
    "margherita": 5.0,
    "diavola": 6.5,
    "capricciosa": 7.0
}

print("Benvenut*! Questo è il nostro seguente menu: ")

for nome, prezzo in pizze.items():
    print(f"- {nome}: {prezzo} €")

scelta = input("Che pizza desidera? ").strip().lower()

if scelta in pizze:
    prezzo_scelto = pizze[scelta]
    print(f"Ottima scelta! Il prezzo della {scelta} è {prezzo_scelto}€")
else:
    print("Spiacenti, non abbiamo questa pizza.")