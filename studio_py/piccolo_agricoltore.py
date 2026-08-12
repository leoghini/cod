#Il programma deve:
# Creare due variabili iniziali: soldi = 10 e giorno = 1.
# Creare un dizionario con i prezzi dei semi: prezzi_semi = {"carota": 2, "pomodoro": 3}.
# Creare un dizionario con i prezzi di vendita del raccolto: valore_raccolto = {"carota": 5, "pomodoro": 8}.
# Avviare un ciclo while giorno <= 3: (il gioco dura 3 giorni).
# Dentro il ciclo (Ogni giorno):
# Stampare il giorno attuale e quanti soldi hai.
# Chiedere all'utente: "Cosa vuoi piantare oggi? (carota/pomodoro): ".
# Usare gli if per verificare se l'utente ha abbastanza soldi per comprare quel seme.
# Se ha abbastanza soldi: scala il prezzo del seme dai soldi, 
# poi calcola subito la crescita e aggiungi il guadagno del raccolto ai soldi (es. soldi = soldi - prezzo + guadagno). 
# Stampa un messaggio del tipo: "Hai piantato e venduto! Ora hai X soldi".
# Se non ha abbastanza soldi: stampa "Fondi insufficienti!".
# Alla fine del turno, aumenta il giorno di 1 (giorno = giorno + 1).
# Fuori dal ciclo (dopo il giorno 3), 
# stampa il bilancio finale: "La stagione è finita! Hai totalizzato un patrimonio di X soldi!".

soldi = 10
giorno = 1

prezzi_semi = {"carota": 2, "pomodoro": 3}
valore_raccolto = {"carota": 6, "pomodoro": 8}

while giorno <= 3:
    print("Oggi è il giorno", giorno, "e hai", soldi, "euro")
    user_choice = input("Cosa vuoi piantare oggi? carota o pomodoro? ").strip().lower()
    
    if user_choice == "carota" and soldi >= 2:
        soldi = soldi - prezzi_semi[user_choice] + valore_raccolto[user_choice]
        print("Hai piantato e venduto! Ora hai", soldi, "euro")
        giorno = giorno + 1 
        
    elif user_choice == "pomodoro" and soldi >= 3:
        soldi = soldi - prezzi_semi[user_choice] + valore_raccolto[user_choice]
        print("Hai piantato e venduto! Ora hai", soldi, "euro")
        giorno = giorno + 1 
        
    elif user_choice in ["carota", "pomodoro"]:
        print("Fondi insufficienti!")
        giorno = giorno + 1 
    else:
        print("Scelta non valida! Riprova.")