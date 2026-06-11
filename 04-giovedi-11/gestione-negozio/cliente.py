# cliente.py
# Questa classe rappresenta un cliente in un negozio, con username, password e una lista di acquisti.
class Cliente:
    def __init__(self, username, password): # Il metodo __init__ è il costruttore della classe, che viene chiamato quando si crea un'istanza della classe Cliente. 
                                            # Accetta due parametri: username e password, che vengono utilizzati per inizializzare gli attributi dell'istanza.  
        self.username = username # L'attributo self.username viene assegnato al valore del parametro username, che rappresenta il nome utente del cliente.  
        self.password = password
        self.acquisti = []

    def aggiungi_acquisto(self, articolo, quantita): # Il metodo aggiungi_acquisto accetta due parametri: articolo e quantita, che rappresentano l'articolo acquistato e la quantità acquistata.    
        self.acquisti.append((articolo.nome, quantita)) # Il metodo aggiungi_acquisto utilizza il metodo append per aggiungere una tupla contenente il nome dell'articolo e la quantità acquistata alla lista degli acquisti del cliente.   

    def mostra_acquisti(self): # Il metodo mostra_acquisti stampa gli acquisti del cliente.
        print(f"\nAcquisti di {self.username}:") # Il metodo mostra_acquisti utilizza una f-string per stampare un'intestazione che include il nome utente del cliente. 
        for articolo, quantita in self.acquisti: # Il ciclo for itera attraverso la lista degli acquisti del cliente, estraendo il nome dell'articolo e la quantità acquistata da ogni tupla.   
            print(f"{articolo} x {quantita}") # Il metodo mostra_acquisti utilizza una f-string per stampare il nome dell'articolo e la quantità acquistata in un formato leggibile.    