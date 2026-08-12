import random       #generates random numbers for this code

numero_casuale = random.randint(1, 10)
print("Ho pensato ad un numero tra 1 e 10. Prova ad indovinarlo!")

while True:         #inizio ciclo infinito finchè giocatore non indovina
    tentativo = int(input("Inserisci un numero: "))

    if tentativo < numero_casuale:
        print("Sbagliato! Devi ALZARE il numero. ⬆️")

    elif tentativo > numero_casuale:
        print("Sbagliato! Devi DIMINUIRE il numero. ⬇️")

    else:
        print("Grande! Hai indovinato il numero! 🎉")
        break           #chiude il ciclo appena indovina