#Il programma deve:
# Creare una variabile incasso_totale inizializzata a 0.
# Avviare un ciclo infinito scrivendo: while True:
# Dentro il ciclo:Chiedere all'utente: "Inserisci il prezzo della consumazione (o scrivi 'esci' per chiudere): "
# Controllare se l'utente ha scritto "esci". 
# Se sì, usa il comando break per uscire dal ciclo.
# Se non ha scritto esci, 
# trasforma l'input in un numero decimale usando float() (perché i prezzi hanno la virgola, es. 1.50) aggiungilo a incasso_totale.
# Fuori dal ciclo, stampare l'incasso finale.

incasso_totale = 0

while True:
    question =input("Inserisci il prezzo della consumazione o scrivi esci per chiudere: ")
    if question == "esci":
        break
    else:
        incasso_totale = incasso_totale + float(question)

print(incasso_totale)