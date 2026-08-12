#Il programma deve:Chiedere all'utente la sua età.
# Controllare se l'età è maggiore o uguale a 18.
# Se è maggiorenne, stampare: "Prego, puoi entrare!"
# Se è minorenne (quindi in tutti gli altri casi), stampare: "Mi dispiace, sei troppo giovane."

person_age = int(input("Quanti anni hai? "))

if person_age >= 18:
    print("Prego, puoi entrare")
else:
    print("Mi dispiace, sei troppo giovane.")

