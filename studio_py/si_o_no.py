#Il programma deve:
# Avere una lista di voti già pronta, ad esempio: voti = ["Sì", "No", "Sì", "Sì", "No"].
# Creare due variabili contatore inizializzate a 0: voti_si = 0 e voti_no = 0.
# Usare un ciclo for per esaminare ogni voto dentro la lista voti.
# Dentro il ciclo: Usare un if per controllare il valore del voto:
# Se il voto è "Sì", aumenta voti_si di 1 (si fa con voti_si = voti_si + 1).
# Altrimenti (se è "No"), aumenta voti_no di 1.
# Alla fine di tutto, fuori dal ciclo, stampare il totale dei "Sì" e il totale dei "No".

vote_list = ["Si", "No", "Si", "Si", "No"]

voti_si = 0
voti_no = 0

for risultato in vote_list:
    if risultato == "Si":
        voti_si = voti_si + 1
    elif risultato == "No":
        voti_no = voti_no + 1

print("Voti Positivi: ",voti_si, "Voti Negativi: ",voti_no)