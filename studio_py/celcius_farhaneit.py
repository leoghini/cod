#Il programma deve solo:
# Chiedere all'utente la temperatura in Celsius (usa float() per i decimali).
# Fare il calcolo: fahrenheit = (celsius * 1.8) + 32
# Stampare il risultato.

celsius = float(input("Inserisci la temperatura in Celsius per convertirla in Fahrenheit: "))

fahrenheit = (celsius * 1.8) + 32

print("Ci sono", fahrenheit, "gradi Fahrenheit")

fahrenheit = float(input("Inserisci la temperatura in Fahrenheit per convertirla in Celsius: "))

celsius = (fahrenheit - 32) / 1.8

print("Ci sono", celsius," gradi Celsius")