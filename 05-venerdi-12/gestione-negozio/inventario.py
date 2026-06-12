# Inventario.py

from articolo import Articolo # importa la classe Articolo
from cliente import Cliente # importa la classe Cliente 

class Inventario: # rappresenta l'inventario del negozio    
    def __init__(self): # inizializza l'inventario con una lista vuota di articoli  
        self.articoli = [] # salva la lista degli articoli nell'inventario  

    def aggiungi(self, articolo): # aggiunge un articolo all'inventario 
        self.articoli.append(articolo) # aggiunge l'articolo alla lista degli articoli  

    def mostra(self): # mostra l'inventario stampando ogni articolo presente    
        print("\nINVENTARIO") # stampa l'intestazione dell'inventario     if not self.articoli: # se la lista degli articoli è vuota        print("Inventario vuoto") # stampa un messaggio se l'inventario è vuoto        return # esce dalla funzione         
        for a in self.articoli:
            print(a)

    def cerca(self, nome): # cerca un articolo nell'inventario per nome (case-insensitive)      
        for a in self.articoli: # itera su ogni articolo presente nell'inventario   
            if a.nome.lower() == nome.lower(): # confronta il nome dell'articolo con il nome cercato (ignorando maiuscole/minuscole)    
                return a
        return None