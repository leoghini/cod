#Scrivi un programma che:
#Definisce in alto una funzione chiamata calcola_sconto(prezzo, percentuale):
#Calcola l'importo dello sconto: importo_sconto = prezzo * (percentuale / 100)
#Restituisce (return) il prezzo scontato finale (prezzo - importo_sconto).
#Fuori dalla funzione (nel codice principale):
#Chiedi all'utente il prezzo originale (convertilo in float).
#Chiedi la percentuale di sconto da applicare (es. 20 per il 20%).
#Chiama la funzione calcola_sconto passando i due dati scritti dall'utente.
#Stampa a schermo il prezzo finale formattato (es. 15.00€).

def calcola_sconto(prezzo, percentuale):
    importo_sconto = prezzo * (percentuale / 100)
    prezzo_finale = prezzo - importo_sconto

    return prezzo_finale    

prezzo = float(input("Che prezzo vuoi scontare? "))
percentuale = float(input("Che sconto vuoi applicare? "))

risultato = calcola_sconto(prezzo, percentuale)
print(f"Il prezzo finale è: {risultato:.2f}€")