# cliente.py

class Cliente: # rappresenta un cliente del negozio
    def __init__(self, username, password): # inizializza il cliente con username e password        
        self.username = username # salva l'username del cliente
        self.password = password # salva la password del cliente