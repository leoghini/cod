#Il programma deve:
# Avere una lista iniziale con 3 nomi di ospiti VIP.
# Chiedere all'utente di inserire il proprio nome.
# Verificare se il nome inserito è presente nella lista VIP:
# Se è presente, rimuovere quel nome dalla lista (usa il metodo .remove(nome)) e stampare un messaggio di benvenuto personalizzato.
# Se non è presente, aggiungere il nome in fondo alla lista (usa il metodo .append(nome)) e stampare un messaggio che dice che è stato messo in coda.
# Alla fine, stampare la lista VIP aggiornata per vedere come è cambiata

vip_names = ["Federica", "Leonardo", "Oliver", "Ciccio", "Simba"]

guest_name = input("Per favore inserire il proprio nome per la verifica  ")

if guest_name in vip_names:
    vip_names.remove(guest_name)
    print("Ti diamo un caloroso benvenuto ",guest_name)
else:
    vip_names.append(guest_name)
    print("Gentile è stato messo in coda, la preghiamo di attendere.")

print(*vip_names)