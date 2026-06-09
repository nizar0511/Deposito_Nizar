#-------------------------------------
# Esercizio 3: Simulazione di un sistema di registrazione e login
# Scrivi un programma che simuli un sistema di registrazione e login.
# Il programma deve chiedere all'utente se vuole creare un nuovo account o accedere a un account esistente.
# Se l'utente sceglie di creare un nuovo account, il programma deve chiederere un nome, una password e assegnare un ID univoco (incrementale).
# Se l'utente sceglie di accedere, il programma deve chiedere il nome e la password e verificare se corrispondono a un account registrato (puoi simulare questa parte senza implementare una vera registrazione).   
# In entrambi i casi, il programma deve stampare un messaggio di benvenuto o di errore a seconda del risultato dell'operazione.
[
    {"id": 1, "nome": "nizar", "password": "1234"},
    {"id": 2, "nome": "luca", "password": "abcd"}
]

id_corrente = 0

azione = input("Vuoi creare un nuovo account? (si/no): ")

if azione == "si":
    nome = input("Inserisci il nome: ")
    password = input("Inserisci la password: ")

    id_corrente += 1  # L'ID cresce automaticamente

    print("\n=== ACCOUNT CREATO ===")
    print("Nome:", nome)
    print("Password:", password)
    print("ID assegnato:", id_corrente)

else:
    print("Controllo account...")
    print("Se esistesse un account, qui verrebbe verificato.")
    print("Script concluso.")





