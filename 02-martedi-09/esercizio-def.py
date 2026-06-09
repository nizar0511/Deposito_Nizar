# Esercizio: Indovina il numero
# Scrivi un programma che:  
# 1. Genera un numero casuale tra 1 e 100 (inclusi).
# 2. Chiede all'utente di indovinare il numero. 
# 3. Fornisce un feedback all'utente se il tentativo è troppo basso, troppo alto o corretto.
# 4. Permette all'utente di continuare a indovinare fino a quando non indovina il numero o decide di uscire digitando "esci".
# Dettagli:
# - Utilizza la libreria `random` per generare il numero casuale.
# - Assicurati di gestire i casi in cui l'utente inserisce un input non valido (ad esempio, lettere invece di numeri).
# Esempio di output:
# Ho scelto un numero tra 1 e 100. Prova a indovinare!
# Scrivi 'esci' per terminare.
# Inserisci un numero: 50
# Troppo basso!
# Inserisci un numero: 75
# Troppo alto!
# Inserisci un numero: 63
# Complimenti! Hai indovinato!

import random # Importiamo la libreria random per generare numeri casuali
def indovina_numero(): # Definiamo una funzione per il gioco dell'indovina il numero
    
    numero_segreto = random.randint(1, 100) # Generiamo un numero casuale tra 1 e 100 (inclusi)
    print("Ho scelto un numero tra 1 e 100. Prova a indovinare!")
    print("Scrivi 'esci' per terminare.")

    while True: # Iniziamo un ciclo infinito che continuerà finché l'utente non indovina il numero o decide di uscire
        tentativo = input("Inserisci un numero: ")

        if tentativo.lower() == "esci": 
            print("Hai deciso di uscire dal gioco.")
            break

        if not tentativo.isdigit(): # Verifichiamo se l'input dell'utente è un numero valido (composto solo da cifre)
            print("Inserisci un numero valido!")
            continue

        tentativo = int(tentativo) # Convertiamo l'input dell'utente in un numero intero

        if tentativo < numero_segreto:
            print("Troppo basso!")
        elif tentativo > numero_segreto:
            print("Troppo alto!")
        else:
            print("Complimenti! Hai indovinato!")
            break

# Avvio del gioco
indovina_numero()





# Esercizio: Sequenza di Fibonacci
# Scrivi un programma che:  
# 1. Chiede all'utente di inserire un numero intero positivo (n).
# 2. Utilizza un ciclo WHILE per generare la sequenza di Fibonacci fino a n. La sequenza di Fibonacci è una serie di numeri in cui ogni numero è la somma dei due precedenti, a partire da 0 e 1. La sequenza inizia così: 0, 1, 1, 2, 3, 5, 8, 13, ...
# 3. Stampa la sequenza di Fibonacci generata.  
# Dettagli:
# - Assicurati di gestire i casi in cui l'utente inserisce un input non valido (ad esempio, lettere invece di numeri).
# Esempio di output:
# Inserisci un numero intero positivo: 10
# Sequenza di Fibonacci fino a 10:
# [0, 1, 1, 2, 3, 5, 8]
# Inserisci un numero intero positivo: -5
# Errore: devi inserire un numero POSITIVO! 
# Inserisci un numero intero positivo: abc
# Errore: devi inserire un numero POSITIVO!
# Inserisci un numero intero positivo: 15
# Sequenza di Fibonacci fino a 15:
# [0, 1, 1, 2, 3, 5, 8, 13]


def fibonacci_fino_a_n(n): # Definiamo una funzione che genera la sequenza di Fibonacci fino a n
    sequenza = [] # Inizializziamo una lista vuota per memorizzare la sequenza di Fibonacci
    a, b = 0, 1 # Inizializziamo i primi due numeri della sequenza di Fibonacci

    while a <= n: # Utilizziamo un ciclo WHILE per generare la sequenza di Fibonacci fino a n
        sequenza.append(a) # Aggiungiamo il numero corrente alla sequenza
        a, b = b, a + b

    return sequenza

# Uso della funzione
N = int(input("Inserisci un numero N per la sequenza di Fibonacci: "))
risultato = fibonacci_fino_a_n(N)

print("Sequenza di Fibonacci fino a", N, ":")
print(risultato)
