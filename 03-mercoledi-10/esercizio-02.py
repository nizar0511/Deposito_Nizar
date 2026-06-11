# Esercizio 2: Creazione di una classe "Libro"
# Crea una classe "Libro" con i seguenti attributi: titolo, autore e pagine. Aggiungi un metodo "descrizione" che restituisce una stringa con le informazioni del libro. Crea un'istanza della classe e stampa la descrizione del libro.    

class Libro:
    def __init__(self, titolo, autore, pagine): 
        # Il metodo __init__ è il costruttore della classe, che viene chiamato quando si crea un'istanza della classe. In questo caso, accetta tre argomenti: titolo, autore e pagine, e li assegna agli attributi dell'istanza.    
        self.titolo = titolo # L'attributo self.titolo viene assegnato al valore del parametro titolo passato al costruttore. Lo stesso vale per autore e pagine.
        self.autore = autore 
        self.pagine = pagine 

    def descrizione(self): 
    # Il metodo descrizione è un metodo della classe Libro che restituisce una stringa con le informazioni del libro. Utilizza gli attributi dell'istanza (self.titolo, self.autore e self.pagine) per creare la stringa di descrizione.
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha {self.pagine} pagine." 
    # Restituisce una stringa formattata con le informazioni del libro.
    
libri = [] # Creiamo una lista vuota per memorizzare le istanze dei libri inseriti dall'utente.

while True:
    titolo = input("Inserisci il titolo del libro (o 'fine' per terminare): ")

    if titolo.lower() == "fine":
        break

    autore = input("Inserisci l'autore: ")
    pagine = int(input("Inserisci il numero di pagine: "))

    libro = Libro(titolo, autore, pagine)
    libri.append(libro)   
  
    
print("\nElenco libri inseriti:\n")

for libro in libri:
    print(libro.descrizione())