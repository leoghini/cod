#Il programma deve:
# Creare un dizionario chiamato inventario con 3 armi e il loro rispettivo valore di attacco, scritto esattamente così:
# pythoninventario = {"Spada": 15, "Arco": 12, "Bastone": 8}
#Usa il codice con cautela.
# Chiedere all'utente quale arma vuole equipaggiare: 
# scelta = input("Quale arma vuoi usare? ")
# Usare un controllo if per verificare se l'arma scelta esiste nell'inventario (puoi usare if scelta in inventario:).
# Cosa fare nel controllo:
# Se l'arma esiste, recupera il suo valore e stampalo (es. punti_danno = inventario[scelta], poi stampa il danno).
# Se non esiste, stampa un messaggio di errore (es. "Arma non trovata!").

inventario = {"Spada": 15, "Arco": 12, "Bastone": 8}

choose_weapon = input("Quale arma vuoi usare? Spada, Arco o Bastone? ")

if choose_weapon in inventario:
    punti_danno = inventario[choose_weapon]
    print(choose_weapon, punti_danno)

else:
    print("Arma non trovata!")

for arma in inventario:
    inventario[arma] = inventario[arma] +5

print(inventario)