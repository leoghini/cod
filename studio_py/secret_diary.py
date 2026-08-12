#Il programma deve:
# Chiedere all'utente di scrivere una nota: nota = input("Scrivi la tua nota segreta di oggi: ")
# Aprire un file di testo in modalità "scrittura" o "aggiunta" usando il comando open().
# Scrivere la nota dentro il file e poi chiuderlo per salvare.
# Il super trucco di Python per gestire i file:
# Per aprire, scrivere e chiudere un file in modo sicuro con una sola riga, i programmatori usano la struttura with open(...):
# 'a' significa 'append' (aggiungi in fondo al file senza cancellare quello che c'era prima)
#with open("diario.txt", "a") as file:
#    file.write(nota + "\n") # Il \n serve per andare a capo nella nota successiva
#Alla fine, stampa un messaggio di successo: "Nota salvata nel diario segreto!"

#nota = input("Scrivi la tua nota segreta di oggi: ")

#with open("diario.txt", "a") as file:
#    file.write(nota + "\n")
#    print("Nota salvata nel diario segreto!")

#with open("diario.txt", "r") as file:
#    contenuto = file.read()
#    print(contenuto)

#Avviare un ciclo infinito while True:.
# Mostrare un menu con 3 opzioni:
# "1. Scrivi una nuova nota""2. Leggi tutte le note""3. Esci"
# Chiedere la scelta all'utente (ricordati il .strip() per evitare spazi vuoti!).
# Usare if, elif ed else per eseguire i blocchi di codice che hai appena scritto:
# Se sceglie 1, chiede la nota e la scrive (usando "a").Se sceglie 2, legge il file e stampa il contenuto (usando "r").
# Se sceglie 3, usa il break per chiudere l'app.

while True:
    user_choice = input("1. Scrivi una nuova nota  2. Leggi tutte le note  3. Esci ").strip()
    if user_choice == "1":
        nota = input("Scrivi la tua nuova nota: ")
        with open("diario.txt", "a") as file:
            file.write(nota + "\n")
            print("Nuova nota salvata nel diario!")
    elif user_choice == "2":
        with open("diario.txt", "r") as file:
            contenuto = file.read()
            print(contenuto)
    elif user_choice == "3":
        print("Alla prossima")
        break
