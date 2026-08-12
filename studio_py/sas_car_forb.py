#tu scegli sempre Sasso, e il computer sceglie una mossa a caso tra Sasso, Carta o Forbici.
# Il programma deve:Far scegliere al computer una mossa a caso tra "Sasso", "Carta" e "Forbici".
# Stampare cosa ha scelto il computer.
# Usare gli if ed else per capire chi vince, sapendo che tu hai giocato Sasso:
# Se il computer ha scelto "Carta", stampa: "Hai perso! La carta avvolge il sasso."
# Se il computer ha scelto "Forbici", stampa: "Hai vinto! Il sasso rompe le forbici."
# In tutti gli altri casi (se esce Sasso), stampa: "Pareggio!"

import random

ia_choice = random.choice(["Sasso", "Carta", "Forbici"])
print(ia_choice)

if ia_choice == "Carta":
    print("Hai perso! La carta avvolge il sasso.")

elif ia_choice == "Forbici":
    print("Hai vinto! Il sasso rompe le forbici.")

else:
    print("Pareggio!")