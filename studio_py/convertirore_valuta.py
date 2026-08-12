#Scrivi un programma che:
# Crea una funzione converti_valuta(euro, tasso_cambio=1.08) (di default converte in Dollari $USD$ con tasso 1.08).
# La funzione deve restituire (return) il valore convertito: euro * tasso_cambio.
# Nel codice principale:
# Chiedi all'utente quanti Euro vuole convertire.
# Fai una prima chiamata usando il valore di default (converti in Dollari).
# Fai una seconda chiamata inserendo un tasso di cambio manuale (es. per gli Yen giapponesi, usa 165.0).
# Stampa entrambi i risultati!

def converti_valuta(euro, tasso_cambio = 1.08):
    valore_convertito = euro * tasso_cambio

    return valore_convertito

euro_dollari = float(input("Quanti euro desideri convertire in dollari? "))
risultato_dollari = converti_valuta(euro_dollari)

euro_yen = float(input("Quanti euro desideri convertire in yen? "))
risultato_yen = converti_valuta(euro_yen, tasso_cambio= 165.0)

print(f"In dollari sarebbero {risultato_dollari}$")
print(f"In yen sarebbero {risultato_yen}¥")