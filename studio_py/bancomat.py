#Il programma deve:
# Avviare un ciclo infinito while True:.
# Dentro il ciclo, inserire il blocco try ed except che hai appena scritto.
# Il trucco logico:
# Se l'operazione nel try va a buon fine (quindi l'utente inserisce un numero corretto), 
# metti il comando break subito dopo il print di successo per uscire dal ciclo.
# Se l'utente inserisce del testo, il blocco except ValueError: 
# intercetta l'errore, stampa il messaggio di avviso e il ciclo while ricomincia automaticamente da capo!

while True:
    try:
        cifra = float(input("Quanti euro vuoi prelevare? "))
        print("Operazione riuscita. Arrivederci.")
        break
    except ValueError:
        print("Errore. Inserire formato valido, non lettere")