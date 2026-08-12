#Il programma deve:
# Preparare le variabili iniziali: crediti = 20, carburante = 4 e una lista vuota per la stiva: stiva = [].
# Creare un dizionario con i prezzi delle merci sul pianeta attuale: prezzi = {"minerale": 5, "acqua": 3}.
# Avviare un ciclo principale che continua a girare finché hai carburante e finché i crediti sono meno di 100: 
# while carburante > 0 and crediti < 100:
# Dentro il ciclo, mostra lo stato attuale e un menu:
# Stampa quanti crediti hai, quanto carburante ti resta e cosa c'è nella tua stiva.
# Mostra le opzioni: 
# "1. Compra Minerale (5 crediti) | 2. Compra Acqua (3 crediti) | 3. Viaggia e Vendi tutto | 4. Esci"Gestire le scelte con gli if/elif/else:
# Se sceglie 1 o 2 (Comprare): Verifica se hai abbastanza crediti. Se sì, scala i crediti e aggiungi la merce alla lista stiva usando .append(). 
# Se no, stampa "Crediti insufficienti!".
# Se sceglie 3 (Viaggiare e Vendere): Sottrai 1 al carburante. 
# Poi calcola quanti crediti guadagni vendendo tutto quello che hai nella stiva (il minerale raddoppia di valore a 10 crediti, l'acqua a 6!). 
# Svuota la stiva impostandola di nuovo a lista vuota stiva = [] e 
# stampa "Sei arrivato su un nuovo pianeta e hai venduto il carico!".
# Se sceglie 4: Usa il break per uscire dal gioco.
# Fuori dal ciclo (Verdetto finale): 
# Usa gli if per vedere come è finita la partita:
# Se i crediti >= 100, stampa: "Vittoria! Sei diventato un ricco commerciante spaziale!"
# Se il carburante == 0 e hai meno di 100 crediti, stampa: "Game Over! Sei rimasto a secco nello spazio profondo..."

crediti = 20
carburante = 4
stiva =[]

prezzi = {"minerale": 5, "acqua": 3}

while carburante > 0 and crediti < 100:
    print("Possiedi", crediti, "grunken")
    print("Ti restano ancora", carburante, "litri di carburante")
    print("Nella stiva possiedi i seguenti oggetti:", *stiva)
    print("---------------------------------")


    opzioni = input("1. Compra Minerale (5 crediti) | 2. Compra Acqua (3 crediti) | 3. Viaggia e Vendi tutto | 4. Esci ")
    if opzioni == "1" and crediti >= 5:
        crediti = crediti - 5
        stiva.append("minerale")
        print("Perfetto! Hai aggiunto un minerale alla stiva!")
    elif opzioni == "2" and crediti >= 3:
        crediti = crediti - 3
        stiva.append("acqua")
        print("Grande! Così hai la giusta idratazione.")
    elif opzioni == "3":
        carburante = carburante - 1
        guadagno_minerale = stiva.count("minerale") * 10
        guadagno_acqua= stiva.count("acqua") * 6

        crediti = crediti + guadagno_minerale + guadagno_acqua
        stiva = [] 

        print("Sei arrivato su un nuovo pianeta ed hai venduto tutto il carico!")
        print("Hai guadagnato", guadagno_minerale + guadagno_acqua, "crediti")
    elif opzioni == "4":
        print("Grazie di aver giocato!")
        break

if crediti >= 100:
    print("Congratulazioni hai vinto! Sei diventato un ricco commerciante spaziale!")
elif carburante == 0 and crediti <= 100:
    print("Game Over! Sei rimasto a secco nello spazio profondo e sei morto... Riprova.")