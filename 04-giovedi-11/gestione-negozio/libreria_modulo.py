# Creare un modulo chiamato libreria_modulo.py che contiene due classi: Libro e Libreria. 


class Libro: # La classe Libro rappresenta un libro con attributi per il titolo, l'autore e l'ISBN, e un metodo per restituire una descrizione del libro. 
             # Il costruttore __init__ accetta i valori per titolo, autore e ISBN e li assegna agli attributi dell'istanza. 
             # Il metodo descrizione restituisce una stringa formattata che include il titolo, l'autore e l'ISBN del libro. 
             # Questa classe può essere utilizzata per creare oggetti libro che rappresentano libri specifici con le loro informazioni dettagliate.  

    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    def descrizione(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}"


class Libreria:

    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)

    def rimuovi_libro(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                return
        print("Libro non trovato.")

    def cerca_per_titolo(self, titolo):
        risultati = []
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                risultati.append(libro)
        return risultati

    def mostra_catalogo(self):
        if not self.catalogo:
            print("Catalogo vuoto.")
        else:
            for libro in self.catalogo:
                print(libro.descrizione())