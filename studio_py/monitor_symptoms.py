#Il programma deve:
# Creare una variabile punteggio_totale inizializzata a 0.
# Avere una lista fissa con 3 domande (es. ["Ti senti stanco oggi?", "Hai dormito meno di 7 ore?", "Hai mal di testa?"]).
# Usare un ciclo for per mostrare una domanda alla volta all'utente.
# Dentro il ciclo, l'utente deve rispondere "si" o "no".Se l'utente risponde "si", aggiungi 1 al punteggio_totale. 
# Se risponde "no", non aggiungere nulla.
# Alla fine del ciclo, controlla il punteggio:
# Se il punteggio è uguale a 3, stampa: "Livello di stress alto. Hai bisogno di riposo!"
# Se il punteggio è 1 o 2, stampa: "Livello di stress moderato."
# Se il punteggio è 0, stampa: "Sei in ottima forma!

punteggio_totale = 0

stress_questions = ["Ti senti stanco oggi? ", "Hai dormito meno di 7 ore? ", "Hai mal di testa? "]

for question in stress_questions:
    answer = input(question).strip().lower()

    if answer == "si":
        punteggio_totale = punteggio_totale + 1

print("Il tuo punteggio è di: ",punteggio_totale)

if punteggio_totale == 3:
    print("Livello di stress alto. Hai bisogno di riposo!")
elif punteggio_totale in [1,2]:
    print("Livello di stress moderato.")
elif punteggio_totale == 0:
    print("Sei in ottima forma! Congratulazioni!")