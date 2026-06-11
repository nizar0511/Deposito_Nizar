# Esempio di variabile con tuple
# Una tupla è una collezione ordinata e immutabile di elementi. 
# Le tuple sono utili quando si desidera memorizzare un insieme di valori che non devono essere modificati.
# Le tuple possono contenere elementi di tipi diversi, come numeri, stringhe o altre tuple.
# Le tuple sono definite utilizzando le parentesi tonde ().
punto = (3, 4) # Rappresenta un punto in un piano cartesiano
colore_rgb = (255, 128, 0) # Rappresenta un colore in formato RGB
informazioni_persona = ("Alice", 25, "Femmina") # Rappresenta le informazioni di una persona

print(punto[0])  # Output: 3
print(punto[1])  # Output: 4
print(colore_rgb[0])  # Output: 255
print(colore_rgb[1])  # Output: 128
print(colore_rgb[2])  # Output: 0
print(informazioni_persona[0])  # Output: Alice
print(informazioni_persona[1])  # Output: 25
print(informazioni_persona[2])  # Output: Femmina


#-----------------------------------

# Esempio di variabile con set
# Un set è una collezione non ordinata di elementi unici. 
# I set sono utili quando si desidera memorizzare elementi senza preoccuparsi dell'ordine o dei duplicati.  

set1 = set([1, 2, 3, 4, 5])
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2, 3, 3, 4, 4, 5}
print(set1) # Output: {1, 2, 3, 4, 5}
print(set3) # Output: {1, 2, 3, 4, 5}

#-----------------------------------
# I set supportano operazioni matematiche come l'unione, l'intersezione, la differenza e la differenza simmetrica.
# L'unione di due set contiene tutti gli elementi presenti in entrambi i set, senza duplicati.
# L'intersezione di due set contiene solo gli elementi presenti in entrambi i set.
# La differenza di due set contiene gli elementi presenti in un set ma non nell'altro.
# La differenza simmetrica di due set contiene gli elementi presenti in uno dei set ma non in entrambi.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}

#------------------------------------
# Esempio di variabile con dizionario
# Un dizionario è una collezione non ordinata di coppie chiave-valore.
# I dizionari sono utili quando si desidera memorizzare dati associati a chiavi uniche.
# Le chiavi in un dizionario devono essere uniche e immutabili, mentre i valori possono essere di qualsiasi tipo.
# I dizionari sono definiti utilizzando le parentesi graffe {} e le coppie chiave-valore sono separate da due punti :.  
# I dizionari supportano operazioni come l'accesso ai valori tramite le chiavi, l'aggiunta di nuove coppie chiave-valore e la rimozione di coppie chiave-valore.    

studente = {
"nome": "Alice",
"età": 20,
"sesso": "Femmina"
}
print(studente["nome"]) # Output: "Alice"
print(studente["età"]) # Output: 20
print(studente["sesso"]) # Output: "Femmina"

#------------------------------------
# Aggiunta di nuove coppie chiave-valore a un dizionario
# Per aggiungere una nuova coppia chiave-valore a un dizionario, è sufficiente assegnare un valore a una nuova chiave utilizzando la sintassi dizionario[nuova_chiave] = nuovo_valore.  
# Se la chiave esiste già nel dizionario, il valore associato a quella chiave verrà sovrascritto con il nuovo valore.
# Ad esempio, se vogliamo aggiungere la città di residenza dello studente al dizionario, possiamo farlo nel seguente modo:  
# Se vogliamo aggiornare l'età dello studente, possiamo farlo assegnando un nuovo valore alla chiave "età" nel dizionario.

studente = {
"nome": "Alice",
"età": 20,
"sesso": "Femmina"
}
studente["città"] = "Roma"
print(studente)
# Output:{'nome': 'Alice','età': 21,'sesso':'Femmina', 'città': 'Roma'}

#-------------------------------------
# Rimozione di coppie chiave-valore da un dizionario
# Per rimuovere una coppia chiave-valore da un dizionario, è possibile utilizzare la parola chiave del per rimuovere una chiave specifica e il suo valore associato.

studente = {
"nome": "Alice",
"età": 20,
"sesso": "Femmina"
}
print(studente.keys()) # Output: dict_keys(['nome', 'età', 'sesso'])
print(studente.values()) # Output: dict_values(['Alice', 20, 'Femmina'])