# Esercizio completo: Analisi di un numero intero positivo
# Scrivere un programma che:
# 1. Chieda all'utente di inserire un numero intero positivo (n).
# 2. Utilizzi un ciclo WHILE per assicurarsi che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve chiedere nuovamente l'input.
# 3. Utilizzi un ciclo FOR con RANGE per calcolare la somma di tutti i numeri pari da 1 a n.
# 4. Utilizzi un ciclo FOR per creare una lista di tutti i numeri dispari da 1 a n.
# 5. Utilizzi un'istruzione IF per determinare se n è un numero primo o no. Un numero primo è un numero maggiore di 1 che ha solo due divisori: 1 e se stesso.  
# Infine, il programma deve stampare:
# - Il numero inserito dall'utente.
# - La somma dei numeri pari da 1 a n.
# - La lista dei numeri dispari da 1 a n.   
# - Se n è primo, stampare "n è un numero PRIMO". Altrimenti, stampare "n NON è un numero primo".




# 1. WHILE → assicurarsi che n sia positivo
n = int(input("Inserisci un numero intero positivo: "))

while n <= 0:
    print("Errore: devi inserire un numero POSITIVO!")
    n = int(input("Inserisci un numero intero positivo: "))


# 2. FOR + RANGE → somma dei numeri pari da 1 a n
somma_pari = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        somma_pari += i


# 3. FOR → stampa dei numeri dispari da 1 a n
dispari = []
for i in range(1, n + 1):
    if i % 2 != 0:
        dispari.append(i)


# 4. IF → determinare se n è un numero primo
if n < 2:
    primo = False
else:
    primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break


# 5. STAMPA FINALE
print("\n=== RISULTATI ===")
print("Numero inserito:", n)
print("Somma dei numeri pari da 1 a", n, "=", somma_pari)
print("Numeri dispari da 1 a", n, ":", dispari)

if primo:
    print(n, "è un numero PRIMO")
else:
    print(n, "NON è un numero primo")
