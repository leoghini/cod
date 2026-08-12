#1. Dati Iniziali
#Crea un dizionario servizi con almeno 3 riparazioni e i relativi prezzi in decimale (float). (es. "cambio olio": 70.0, "pasticche freni": 120.0, "revisione": 80.0)
#Importa il modulo random e crea una lista meccanici con 3 nomi (es. ["Mario", "Luigi", "Giovanna"]).
#2. Il Ciclo del Menu (while True)
#Avvia un ciclo infinito while True.
#Chiedi all'utente cosa vuole fare con un input() pulito da .strip().lower():
#Option 1: Richiedi un servizio.
#Option 2: Esci dall'officina.
#Se sceglie 2, stampa un messaggio di saluto e interrompi il ciclo con break.
#3. Mostrare il Listino e Scegliere
#Se sceglie 1, mostra il listino prezzi con un ciclo for usufruendo di .items().
#Chiedi all'utente quale servizio desidera (pulisci sempre l'input!).
#Controlla con in se il servizio esiste nel dizionario servizi.
#4. Lo Scudo e il Calcolo (try / except)
#Se il servizio esiste, chiedi su quante auto deve essere effettuato il lavoro.
#Proteggi la conversione in numero intero (int()) con un blocco try / except ValueError.
#Se l'utente inserisce un numero valido:
#Recupera il prezzo unitario dal dizionario con servizi[scelta].
#Calcola il totale (prezzo * quantita).
#Estrai un meccanico a caso dalla lista usando random.choice(meccanici).
#Stampa il resoconto: "Totale da pagare: [totale]€. Il lavoro sarà affidato a [meccanico]."
#Se inserisce lettere o simboli al posto del numero, cattura l'errore nell'except e mostra un avviso senza far piantare il programma.

import random

servizi = {
    "cambio olio": 70.0,
    "pasticche freni": 120.0,
    "revisione": 80.0
}

meccanici = ["Mario", "Luigi", "Franco"]

while True:
    scelta = input("Opzione 1: Richiedi un servizio. | Opzione 2: Esci dall'officina ")
    if scelta == "2":
        print("Grazie per essere passato, torni a trovarci!")
        break
    elif scelta == "1":
        for elemento, prezzo in servizi.items():
            print(f"- {elemento.capitalize()}: {prezzo:.2f}€")
        scelta_servizio = input("Che servizio desidera tra quelli elencati? ").strip().lower()
        if scelta_servizio in servizi:
            try:
                numero_auto = int(input("Su quante auto deve essere effettuato il servizio? "))
                totale = servizi[scelta_servizio] * numero_auto
                meccanico = random.choice(meccanici)
                print(f"Totale da pagare: {totale}€. Il lavoro è stato affidato a {meccanico}.")
            except ValueError:
                print("Errore! Hai inserito lettere o simboli.")
        else:
            print("Servizio non presente nella lista.")
    else:
        print("Opzione non valida. Scelga 1 o 2.")