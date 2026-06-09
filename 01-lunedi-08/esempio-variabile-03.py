"""esempio-variabile-03.py

Esempi e spiegazioni approfondite di tipi primitivi e operazioni base in Python.

Contenuto:
- esempi di `int` e `float`
- esempi di `str` e metodi utili (`len`, `upper`, `split`, `replace`)
- esempi di operatori di confronto e operatori logici

Note d'uso:
- Le righe commentate mostrano come provare i singoli esempi in REPL o decommentandole
- Alcune variabili vengono ridefinite in questo file a scopo dimostrativo; evitare
	di riutilizzare lo stesso nome in codice di produzione per chiarezza.
"""

# -----------------------------------
# Interi (int)
# In Python gli interi (`int`) possono essere positivi o negativi senza limiti fissi
# oltre la memoria disponibile.
#x = 10   # esempio: valore positivo
#y = -5   # esempio: valore negativo

# -----------------------------------
# Numeri in virgola mobile (float)
# Rappresentano numeri reali e usano la precisione doppia (double) standard
#a = 3.14
#b = -1.0

# -----------------------------------
# Stringhe (str)
# In Python le stringhe sono sequenze immutabili di caratteri; si possono usare
# sia apici singoli che doppi per delimitarle.
#nome = 'Alice'
#msg = "Ciao!"

# Esempi utili (decommenta per provarli):
# print(nome)         # stampa il contenuto della variabile 'nome'
# print(msg)          # stampa 'Ciao!'

# Operazioni su stringhe (s: esempio)
#s = "Ciao, mondo!"

# len(s): restituisce la lunghezza (numero di caratteri)
#print(len(s))        # Output atteso: 12

# upper(): converte in maiuscolo senza modificare la stringa originale
#print(s.upper())     # Output atteso: 'CIAO, MONDO!'

# split(sep): divide la stringa in una lista di sottostringhe usando il separatore
#print(s.split(','))  # Output atteso: ['Ciao', ' mondo!']

# replace(old, new): restituisce una nuova stringa con le sostituzioni effettuate
#print(s.replace('mondo', 'universo'))  # Output atteso: 'Ciao, universo!'

# -----------------------------------
# Operatorii di confronto (restituiscono valori booleani: True/False)
# Esempi: ==, !=, <, >, <=, >=
#v1 = 5
#v2 = 10
#v3 = 7

#print(v1 == v2)  # uguale? False
#print(v1 != v2)  # diverso? True
#print(v1 < v2)   # minore? True

# -----------------------------------
# Operatori logici: and, or, not (operano su valori booleani)
#print(v1 < v2 and v2 > v3)  # True se entrambe le condizioni sono True
#print(v1 < v2 or v3 > v2)   # True se almeno una condizione è True
#print(not(v1 < v2))         # not inverte il valore booleano (False)

#------------------------------------

#numeri = [1, 2, 3, 4, 5]
#nomi = ["Alice", "Bob", "Charlie"]
#misto = [1, "due", True, 4.5]

#print(numeri[0]) # Output: 1
#print(numeri[2]) # Output: 3

#-------------------------------------

#numeri = [3, 1, 4, 2, 5]
#print(len(numeri)) # Output: 5
#numeri.append(6)
#print(numeri) # Output: [3, 1, 4, 2, 5, 6]
#numeri.insert(2, 10)
#print(numeri) # Output: [3, 1, 10, 4, 2, 5, 6]
#numeri.remove(4)
#print(numeri) # Output: [3, 1, 10, 2, 5, 6]
#numeri.sort()
#print(numeri) # Output: [1, 2, 3, 5, 6, 10]

#-------------------------------------

#numero = 10
#if numero > 0:
#    print("Il numero è positivo")


#-------------------------------------

#numero = 10
#if numero > 0:
#    print("Il numero è positivo")
#else:
#    print("Blocco Else")
    
#-------------------------------------

from unittest import case


comando = input("Inserisci un comando: ")
match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")