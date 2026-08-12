#Il programma deve:
# Importare due moduli all'inizio: import random e import time.
# Avere una funzione chiamata 
# genera_otp() che sceglie un numero casuale a 6 cifre tra 100000 e 999999 e lo restituisce (oppure lo stampa).
# Mostrare la password all'utente dicendo: "La tua password temporanea è: [NUMERO]".
# Usare il comando time.sleep(5) per far congelare il programma e aspettare esattamente 5 secondi.
# Dopo l'attesa, stampare: "Tempo scaduto! La password è scaduta.

import random
import time

def genera_otp():
    codice = random.randint(100000, 999999)
    print("La tua password temporanea è:", codice)
    time.sleep(20)
    print("Tempo scaduto! La password è scaduta. Riprovare.")

genera_otp()