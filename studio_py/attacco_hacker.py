import random

tentativi_rimasti = 3
file_criptati = ["Database_Utenti", "Conti_Bancari", "Codici_Lancio"]
chiavi_decrittazione = {"Database_Utenti": 101, "Conti_Bancari": 202, "Codici_Lancio": 303}

while tentativi_rimasti > 0 and len(file_criptati) > 0:
    print("\n-------------------------------------------")
    print(f"Tentativi rimasti: {tentativi_rimasti}")
    print("File ancora criptati:", *file_criptati)
    print("-------------------------------------------")
    
    file_scelto = input("Quale file vuoi provare a decrittare? ").strip()
    
    if file_scelto in file_criptati:
        try:
            chiave_utente = int(input(f"Inserisca la chiave numerica di sblocco per {file_scelto}: "))

            if chiave_utente == chiavi_decrittazione[file_scelto]:  
                file_criptati.remove(file_scelto)
                print("File decrittato con successo!")
            else:
                tentativi_rimasti = tentativi_rimasti - 1
                print("Chiave errata! Il firewall ti ha respinto.")
                print(f"Hai ancora {tentativi_rimasti} tentativi.")
        except ValueError:
            tentativi_rimasti = tentativi_rimasti - 1
            print("Input non valido! Inserisca numeri, non lettere.")
            print(f"Hai ancora {tentativi_rimasti} tentativi.")
    else:
        print("Questo file non esiste o è già stato decrittato!")


if len(file_criptati) == 0:
    print("\nVITTORIA! Hai salvato il server e rimosso il malware! Sei un hacker leggendario!")
elif tentativi_rimasti == 0:
    print("\nGAME OVER... Il server si è autodistrutto. I dati sono persi per sempre.")
