# Inventario.py

from articolo import Articolo

class Inventario:
    def __init__(self):
        self.articoli = []

    def aggiungi(self, articolo):
        self.articoli.append(articolo)

    def mostra(self):
        print("\nINVENTARIO")
        for a in self.articoli:
            print(a)

    def cerca(self, nome):
        for a in self.articoli:
            if a.nome.lower() == nome.lower():
                return a
        return None