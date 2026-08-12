#Scrivi un programma che:
#Crea una lista chiamata frutta con almeno 3 frutti (es. ["mela", "banana", "pera"]).
#Usa un ciclo for per stampare a schermo tutti i frutti presenti nella lista, uno per riga.
#Chiedi all'utente quale frutto vuole acquistare (ricordati .strip().lower()).
#Controlla con l'operatore in se il frutto scelto è presente nella lista:
#Se c'è, stampa "Perfetto, abbiamo la tua [frutto]!"
#Se non c'è, stampa "Mi spiace, [frutto] non è disponibile."

frutta = ["mela", "banana", "pera"]

#lista
print("Frutta disponibile:")
for elemento in frutta:
    print("- " + elemento) #frutto su una riga nuova

# scelta utente
scelta = input("Quale di questi desidera? ").strip().lower()

if scelta in frutta:
    print(f"Perfetto, ecco la tua {scelta}!")
else:
    print("Mi dispiace, non è disponibile.")