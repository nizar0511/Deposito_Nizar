# Amministratore.py
# Questa classe rappresenta un amministratore in un negozio, con username e password.
class Amministratore:
    def __init__(self, username, password): # Il metodo __init__ è il costruttore della classe, che viene chiamato quando si crea un'istanza della classe Amministratore. 
                                            # Accetta due parametri: username e password, che vengono utilizzati per inizializzare gli attributi dell'istanza.  
        self.username = username # L'attributo self.username viene assegnato al valore del parametro username, che rappresenta il nome utente dell'amministratore.  
        self.password = password # L'attributo self.password viene assegnato al valore del parametro password, che rappresenta la password dell'amministratore.