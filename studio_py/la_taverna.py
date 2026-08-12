import random

monete = 20
reputazione = 0
dispensa = []
prezzi_cibo = {"carne": 8, "idromele": 4}

print("Parti con 20 monete e 0 di reputazione, scegli una delle opzioni: ")
while monete > 0 and reputazione < 30:
    menu_azioni = input("1 Compra Carne (8 monete) | 2. Compra Idromele (4 monete) | 3. Apri le Porte ai Clienti | 4. Chiudi la Locanda (Esci) ")

    if menu_azioni == "1" and monete >= 8:
        monete = monete - 8
        dispensa.append("carne")
        print("Hai aggiunto la carne alla tua dispensa!")
        print("Ti sono rimeste", monete, "monete")
        if monete < 8:
            print("Non hai abbastanza monete!")

    elif menu_azioni == "2" and monete >= 4:
        monete = monete - 4
        dispensa.append("idromele")
        print("Hai aggiunto idromele alla tua dispensa")
        print("Ti sono rimeste", monete, "monete")
        if monete < 4:
            print("Non hai abbastanza monete!")

    elif menu_azioni == "3":
        cliente = random.choice(["Guerriero", "Mago"])
        if cliente == "Guerriero":
            if "carne" in dispensa:
                dispensa.remove("carne")
                monete = monete + 15
                reputazione = reputazione + 5
                print("Il Guerriero ti ringrazia per la deliziosa carne")
                print("Hai guadagnato", monete, "monete", "e", reputazione, "di reputazione")
            else: 
                reputazione = reputazione - 3
                print("Il Guerriero si guarda intorno e con fare arrabbiato e deluso esce dalla locanda. Grande errore..")
                print("Hai perso", reputazione, "di reputazione")
        elif cliente == "Mago":
            if "idromele" in dispensa:
                dispensa.remove("idromele")
                monete = monete + 10
                reputazione = reputazione + 4
                print("Il potente Mago ha gradito l'idromele e ti ringrazia")
                print("Hai guadagnato", monete, "monete", "e", reputazione, "di reputazione")
            else:
                reputazione = reputazione - 2
                print("Il potente Mago ti lancia una maledizione e se ne va dalla locanda. Abbi timore.")
                print("Hai perso", reputazione, "di reputazione")

    elif menu_azioni == "4":
        print("Per oggi la Locanda chiude.")
        break

if reputazione >= 30:
    print("La tua locanda è diventata la più famosa del regno! Vittoria!")
elif monete <= 0:
    print("Sei andato in bancarotta e hai dovuto chiudere la locanda.. Game Over!")
