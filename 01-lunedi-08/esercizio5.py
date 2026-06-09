#-------------------------------------
# Esercizio 5: Calcolatrice semplice
# Scrivi un programma che chieda all'utente di inserire due numeri e un'operazione (somma, sottrazione, moltiplicazione, divisione).
# Il programma deve eseguire l'operazione scelta sui due numeri e stampare il risultato.
# Se l'utente inserisce un'operazione non valida, il programma deve stampare un messaggio di errore.

num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
operazione = input("Scegli l'operazione (+, -, *, /): ")

if operazione == "+":
    print("Risultato:", num1 + num2)

elif operazione == "-":
    print("Risultato:", num1 - num2)

elif operazione == "*":
    print("Risultato:", num1 * num2)

elif operazione == "/":
    if num2 == 0:
        print("Errore: Divisione per zero")
    else:
        print("Risultato:", num1 / num2)

else:
    print("Operazione non valida")





