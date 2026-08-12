#Il programma deve:
# Chiedere all'utente di scegliere un ruolo tra "Scienziato" o "Artista".
# Avere due liste di città diverse:
# Una lista per i laboratori segreti (es. "Ginevra", "Tokyo", "Los Alamos").
# Una lista per le capitali dell'arte (es. "Parigi", "Firenze", "New York").
# Usare gli if per controllare la scelta dell'utente:
# Se ha scelto Scienziato, il computer sceglie una città a caso dalla lista dei laboratori.
# Se ha scelto Artista, il computer sceglie una città a caso dalla lista dell'arte.
# Alla fine, il computer deve scegliere anche un nome in codice casuale da una terza lista generica (es. "Spettro", "Volpe", "Falco").
# Stampare l'identità finale, ad esempio: "La tua copertura è pronta. Nome in codice: Falco. Destinazione segreta: Ginevra."

import random

player_choice = input("Scegli un ruolo tra Scienziato o Artista: ").capitalize()
secret_name = random.choice(["Spettro", "Volpe", "Falco"]) 

if player_choice == "Scienziato":
    secret_lab = random.choice(["Ginevra", "Tokyo", "Kiev"])
    print("La tua copertura è pronta. Nome in codice:", secret_name, ". Destinazione segreta:", secret_lab, ".")

elif player_choice == "Artista":
    art_capitals = random.choice(["Parigi", "Firenze", "New York"])
    print("La tua copertura è pronta. Nome in codice:", secret_name, ". Destinazione segreta:", art_capitals, ".")

flessioni_giornaliere = [10, 15, 20, 25]

for numero in flessioni_giornaliere:
    print(numero * 2)
