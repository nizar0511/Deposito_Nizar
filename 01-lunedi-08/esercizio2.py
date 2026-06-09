#-------------------------------------
# Esercizio 2: Menu CRUD
# Scrivi un programma che mostri un menu con le opzioni CRUD (Create, Read, Update, Delete).
# L'utente deve selezionare un'opzione e il programma deve stampare un messaggio corrispondente all'opzione scelta. 
# Se l'utente inserisce un'opzione non valida, il programma deve stampare un messaggio di errore. 

print("=== MENU CRUD ===")
print("1 - Aggiungi")
print("2 - Modifica")
print("3 - Elimina")

scelta = input("Seleziona un'opzione: ")

if scelta == "1":
    print("Hai scelto: AGGIUNGI")
elif scelta == "2":
    print("Hai scelto: MODIFICA")
elif scelta == "3":
    print("Hai scelto: ELIMINA")
else:
    print("Opzione non valida.")



