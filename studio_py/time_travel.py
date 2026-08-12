#Il programma deve:Chiedere all'utente in che anno vuole viaggiare (un numero).
# Verificare l'anno con gli if:
# Se l'anno è minore del 2026, il computer capisce che vuoi andare nel Passato e stampa: "Viaggio nel passato avviato..."
# Se l'anno è maggiore del 2026, capisce che vai nel Futuro e stampa: "Salto nel futuro avviato..."
# Se l'anno è esattamente il 2026, stampa: "Sei rimasto nel presente!"
# L'effetto sorpresa (Casualità):Subito dopo aver stabilito la direzione, il computer deve lanciare un imprevisto a caso da una lista. 
# Crea una lista con 3 imprevisti 
# (es. "La macchina del tempo ha finito il plutonio", "Hai incontrato un dinosauro", "Tutto è andato liscio").
# Stampare l'imprevisto che è uscito.

import random

year = int(input("In che anno vorresti andare? "))

if year < 2026:
    print("Viaggio nel passato avviato...")

elif year > 2026:
    print("Salto nel futuro avviato...")

elif year == 2026:
    print("Sei nel presente!")

imprevisti = random.choice(["La macchina del tempo ha finito il plutonio", "Hai incontrato un alieno", "Tutto è andato liscio"])
print(imprevisti)