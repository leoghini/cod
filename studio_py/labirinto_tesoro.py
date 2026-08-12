#Il programma deve:
# Creare una variabile monete = 0.
# Avviare un ciclo while monete < 3:. 
# Questo significa che il gioco continua finché non hai accumulato 3 monete.
# Dentro il ciclo, presentare una scelta all'utente: 
# "Ti trovi davanti a due porte. Vuoi andare a 'destra' o 'sinistra'?".
# Usare gli if / else per gestire la scelta:
# Se sceglie "destra": Trova una moneta! Stampa un messaggio felice e aumenta la variabile monete di 1 (es. monete = monete + 1). 
# Stampa anche quante monete ha in totale.
# Se sceglie "sinistra": 
# C'è un mostro! Il gioco finisce subito. Per farlo, stampa "Un mostro ti ha catturato! Game Over!" e usa il comando break 
# Fuori dal ciclo (se l'utente riesce a raccogliere 3 monete senza mai prendere la porta con il mostro), stampa: 
# "Complimenti! Hai trovato l'uscita con 3 monete d'oro! Vittoria!".

import random 

monete = 0

while monete < 3:
    porta_vincente = random.choice(["destra", "sinistra"])
    user_choice = input("Ti trovi davanti a due porte. Scegli quella a destra o quella a sinistra? ")

    if user_choice == porta_vincente:
        monete = monete + 1
        print("Grandeee! Hai guadagnato una moneta continua così!")
        print("Monete totali: ",monete)
    elif user_choice == "destra" or user_choice == "sinistra":
        print("Un mostro ti ha catturato! GAME OVER!")
        print("Hai preso solo: ", monete)
        break
    else:
        print("Opzione non valida! Scegli 'destra' o 'sinistra'.")
   
if monete == 3:
    print("Complimenti! Hai trovato l'uscita con 3 monete d'oro! VITTORIA!")