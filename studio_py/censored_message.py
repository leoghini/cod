#Il programma deve:
# Chiedere all'utente di inserire un messaggio: messaggio = input("Scrivi un messaggio: ")
# Avere una lista di parole vietate, ad esempio: parole_vietate = ["segreto", "password", "spia"]
# Usare un ciclo for per controllare ogni singola parola vietata dentro la lista.
# Cosa fare nel ciclo: 
# Usare il metodo dei testi .replace(vecchio, nuovo) per sostituire la parola vietata con degli asterischi "***".
# Suggerimento: 
# Puoi fare messaggio = messaggio.replace(parola, "***") dentro il ciclo per aggiornare il messaggio ogni volta che trova una parola vietata.
# Fuori dal ciclo, stampare il messaggio finale censurato.

messaggio = input("Scrivi un messaggio: ")

parole_vietate = ["password", "spia", "segreto"]

for parola in parole_vietate:
    messaggio = messaggio.replace(parola, "****")

print(messaggio)