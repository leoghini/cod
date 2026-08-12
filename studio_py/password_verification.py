#Chiedere all'utente di inventare e inserire una password.
# Controllare se la password è abbastanza lunga (usa la funzione len(tua_stringa) per contare le lettere). 
# Deve essere maggiore o uguale a 8 caratteri.
# Controllare se nella password c'è almeno un numero usare il metodo any(char.isdigit() for char in password)).
# Rendiamolo super semplice: Controlla solo se contiene un punto esclamativo ! usando l'operatore if "!" in password:.
# Se la password è lunga almeno 8 caratteri E contiene un !, stampa: "Password accettata e sicura!".
# Altrimenti, stampa un messaggio di errore spiegando cosa manca (es. "La password deve essere di 8 caratteri e contenere un !").

user_password = input("Inserisci una nuova password ")

if len(user_password) >= 8 and "!" in user_password:
    print("Password accettata e sicura")
else:
    print("La password deve essere di minimo 8 caratteri e contenere un !")