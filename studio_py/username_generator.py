#Il programma deve:
# Chiedere all'utente il suo colore preferito (es. "Rosso").
# Avere una lista di animali (es. ["Lupo", "Drago", "Gatto"]).
# Usare un ciclo for per prendere ogni animale della lista e unirlo al colore dell'utente
# aggiungendo anche un numero casual (es. "LupoRosso77").
# Stampare a schermo tutte le combinazioni possibili generate, così l'utente può scegliere la sua preferita!

import random

user_color = input("Qual è il tuo colore preferito? ")

animal_list = ["Lupo", "Gatto", "Drago"]
casual_num = random.randint(10, 99)

for i in animal_list:
    username = i+ user_color + str(casual_num)
    print(username)
