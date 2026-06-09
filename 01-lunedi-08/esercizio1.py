#-------------------------------------
# Esercizio 1: Accesso a livelli di sicurezza

# Scrivi un programma che simuli un sistema di accesso a tre livelli di sicurezza.
# Il programma chiederà all'utente di inserire una password per il primo livello.
# Se la password è corretta, chiederà un codice per il secondo livello.
# Se anche il codice è corretto, chiederà una chiave per il terzo livello.
# Se tutte e tre le credenziali sono corrette, stamperà un messaggio di benvenuto.


livello1 = input("Inserisci la password di livello 1: ")

if livello1 == "admin":
    livello2 = input("Inserisci il codice di livello 2: ")
    
    if livello2 == "1234":
        livello3 = input("Inserisci la chiave di livello 3: ")
        
        if livello3 == "XYZ":
            print("Accesso COMPLETO. Benvenuto!")
        else:
            print("Livello 3 fallito. Accesso negato.")
    else:
        print("Livello 2 fallito. Accesso negato.")
else:
    print("Livello 1 fallito. Accesso negato.")


