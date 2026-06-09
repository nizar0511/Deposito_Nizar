#numeri = [1, 2, 3, 4, 5] # Creiamo una lista di numeri da 1 a 5
#for numero in numeri: # Iteriamo attraverso la lista di numeri
#    if numero == 3: # Se il numero è uguale a 3, saltiamo il resto del ciclo e passiamo al numero successivo
#        break
#print(numero)

#--------------------------------

#numeri = [1, 2, 3, 4, 5] # Creiamo una lista di numeri da 1 a 5
#for numero in numeri:
#    if numero == 3: # Se il numero è uguale a 3, saltiamo il resto del ciclo e passiamo al numero successivo
#        continue
#print(numero)

#--------------------------------

#for i in range(5): # Iteriamo da 0 a 4
#    if i == 3: # Se i è uguale a 3, saltiamo il resto del ciclo e passiamo al numero successivo
#        pass
#print(i)

#--------------------------------

#numeri = [*range(1, 11)] # Creiamo una lista di numeri da 1 a 10 utilizzando range e unpacking
#print(numeri)
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#-------------------------------

#def saluta(nome):
#    print("Ciao,", nome)
#    print("Benvenuto nel nostro programma!")
    
#-------------------------------

#def somma(a, b): # Definiamo una funzione che prende due argomenti, a e b
#    risultato = a + b
#    print("La somma è:", risultato)

#-------------------------------

#def saluta(nome:str, messaggio="Ciao"): # Definiamo una funzione che prende un argomento obbligatorio (nome) e un argomento opzionale (messaggio) con un valore predefinito
#    print(f"{messaggio} {nome}!") # Utilizziamo f-string per formattare il messaggio di saluto
#saluta("Mario") # Chiamata alla funzione
#saluta("Luigi", messaggio="Buongiorno")

#-------------------------------

#def quadrato(numero): # Definiamo una funzione che prende un argomento (numero) e restituisce il suo quadrato
#    return numero * numero
#risultato = quadrato(4)
#print(risultato) # Output: 16

#-------------------------------

#def fibonacci(n): # Definiamo una funzione che genera la sequenza di Fibonacci fino a n
#    a, b = 0, 1 # Inizializziamo i primi due numeri della sequenza di Fibonacci
#    while a < n: # Utilizziamo un ciclo WHILE per generare la sequenza di Fibonacci fino a n
#        yield a # Utilizziamo yield per restituire il numero corrente e mantenere lo stato della funzione
#        a, b = b, a + b # Aggiorniamo i valori di a e b per generare il prossimo numero della sequenza

#-------------------------------

#def decoratore(funzione): # Definiamo un decoratore che prende una funzione come argomento
#    def wrapper(): # Definiamo una funzione wrapper che avvolge la funzione originale
#        print("Prima dell'esecuzione della funzione")
#        funzione()
#        print("Dopo l'esecuzione della funzione")
#    return wrapper

#-------------------------------

#def decoratore_con_argomenti(funzione): # Definiamo un decoratore che prende una funzione come argomento
#    def wrapper(*args, **kwargs): # Definiamo una funzione wrapper che avvolge la funzione originale e accetta qualsiasi numero di argomenti posizionali e keyword
#        print("Prima")

#        risultato = funzione(*args, **kwargs)

#       print("Dopo")

#        return risultato

#    return wrapper


#@decoratore_con_argomenti # Applichiamo il decoratore alla funzione somma
#def somma(a, b):
#    print(a + b)
#    return a + b


#print("Risultato è", somma(3, 4))

#-------------------------------

def logger(funzione): # Definiamo un decoratore che prende una funzione come argomento
    def wrapper(*args, **kwargs): # Definiamo una funzione wrapper che avvolge la funzione originale e accetta qualsiasi numero di argomenti posizionali e keyword
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}") # Stampiamo il nome della funzione chiamata e i suoi argomenti

        risultato = funzione(*args, **kwargs) # Eseguiamo la funzione originale e memorizziamo il risultato

        print(f"Risultato di {funzione.__name__}: {risultato}") # Stampiamo il risultato della funzione originale

        return risultato

    return wrapper


@logger # Applichiamo il decoratore alla funzione moltiplica
def moltiplica(a, b): 
    return a * b


# Chiamata alla funzione decorata
print(moltiplica(3, 4))


#-------------------------------

import time

def calcola_tempo(funzione):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        risultato = funzione(*args, **kwargs)

        end_time = time.time()

        print(f"Tempo di esecuzione: {end_time - start_time} secondi")

        return risultato

    return wrapper


@calcola_tempo
def calcolo_lento():
    time.sleep(2)
    print("Calcolo completato")


# Chiamata alla funzione decorata
calcolo_lento()