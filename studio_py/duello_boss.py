#Il programma deve:
# Creare una variabile boss_hp inizializzata a 50.
# Avviare un ciclo while che continua a girare finché i punti vita del boss sono maggiori di 0 (while boss_hp > 0:).
# Dentro il ciclo:
# Stampare quanti HP rimangono al boss (es. "Il Boss ha 50 HP").
# Chiedere all'utente quanto danno vuole fare: danno = int(input("Quanto danno fai? "))
# Sottrare il danno dagli HP del boss: boss_hp = boss_hp - danno.
# Fuori dal ciclo (quando il boss finalmente finisce la vita ed esce dal while), 
# stampare: "Il Boss è stato sconfitto! Hai vinto!".

boss_hp = 100

while boss_hp > 0:
    print("Il boss ha ",boss_hp, " HP")
    danno = int(input("Quanto danno fai? "))
    boss_hp = boss_hp - danno
    if boss_hp <= 0:
        print("Il boss è stato sconfitto! Hai vinto!")
        break

#Il programma deve:
# Definire una funzione chiamata assegna_bottino() usando la parola chiave def (es. def assegna_bottino():)
# Dentro la funzione:
# Crea una lista di premi: premi = ["Spada di Fuoco", "Pozione Magica", "Scudo di Legno"]
# Scegli un premio a caso usando random.choice(premi).
# Stampa il premio a schermo (es. "Hai trovato: Spada di Fuoco!").
# Fuori dalla funzione (sotto), prova a chiamarla due volte di fila scrivendo semplicemente assegna_bottino() per vedere se ti dà due premi diversi!

import random

def assegna_bottino():
    premi = ["Spada di Fuoco Potenziata", "Pozione Curativa", "Scudo del Re"]
    print("Hai trovato: ",random.choice(premi))

assegna_bottino()
assegna_bottino()