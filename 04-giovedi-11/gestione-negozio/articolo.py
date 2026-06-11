# Articolo.py
# Questa classe rappresenta un articolo in un negozio, con nome, prezzo e quantità.
class Articolo:
    def __init__(self, nome, prezzo, quantita): # Il metodo __init__ è il costruttore della classe, che viene chiamato quando si crea un'istanza della classe Articolo. 
                                                #Accetta tre parametri: nome, prezzo e quantita, che vengono utilizzati per inizializzare gli attributi dell'istanza.    
        self.nome = nome # L'attributo self.nome viene assegnato al valore del parametro nome, che rappresenta il nome dell'articolo.
        self.prezzo = prezzo
        self.quantita = quantita

    def __str__(self): # Il metodo __str__ è un metodo speciale che viene chiamato quando si tenta di convertire un'istanza della classe in una stringa, ad esempio quando si stampa l'istanza. 
                       # In questo caso, il metodo __str__ restituisce una stringa formattata che include il nome dell'articolo, il prezzo e la quantità.  
        return f"{self.nome} - €{self.prezzo} - Quantità: {self.quantita}" # La stringa restituita dal metodo __str__ utilizza la sintassi f-string per formattare i valori degli attributi dell'istanza in modo leggibile. 