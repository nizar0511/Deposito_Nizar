# Articolo.py

class Articolo:
    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def to_dict(self):
        return {
            "nome": self.nome,
            "prezzo": self.prezzo,
            "quantita": self.quantita
        }