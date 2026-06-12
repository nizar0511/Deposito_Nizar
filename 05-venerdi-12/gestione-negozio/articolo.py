# Articolo.py

class Articolo: # rappresenta un articolo del negozio
    def __init__(self, nome, prezzo, quantita):# inizializza l'articolo con nome, prezzo e quantità     
        self.nome = nome # salva il nome dell'articolo
        self.prezzo = prezzo # salva il prezzo dell'articolo
        self.quantita = quantita # salva la quantità dell'articolo

    def to_dict(self): # converte l'articolo in un dizionario per l'inserimento nel database    
        return {
            "nome": self.nome,
            "prezzo": self.prezzo,
            "quantita": self.quantita
        }