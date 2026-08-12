#Il programma deve:
# Chiedere un anno all'utente (es. 2024 o 2026) e convertirlo in numero intero.
# Controllare se l'anno è divisibile per 4.
# Aiuto sul simbolo: 
# In Python, per sapere se un numero è perfettamente divisibile per un altro si usa l'operatore resto della divisione % (chiamato modulo). 
# Se il resto è zero (anno % 4 == 0), significa che è divisibile!
# Se è divisibile per 4, stampa: "L'anno è bisestile!"
# Altrimenti, stampa: "L'anno non è bisestile."

user_choice = int(input("Inserisci un anno: "))

if (user_choice % 400 == 0) or (user_choice % 4 == 0 and user_choice % 100 != 0):
    print("L'anno", user_choice, "è un anno bisestile!")
else:
    print("L'anno non è bisestile.")
