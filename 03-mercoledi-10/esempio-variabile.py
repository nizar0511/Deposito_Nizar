# Esempio di variabile
# In questo esempio, definiamo una classe "Studente" con un costruttore che accetta il nome e l'età dello studente. Inoltre, implementiamo il metodo __str__ per fornire una rappresentazione leggibile dell'oggetto quando viene stampato. Infine, creiamo un'istanza della classe Studente e la stampiamo per vedere il risultato.    
# La classe Studente rappresenta uno studente con un nome e un'età. Il metodo __init__ è il costruttore della classe, che viene chiamato quando si crea un'istanza della classe. In questo caso, accetta due argomenti: nome e eta, e li assegna agli attributi dell'istanza. Il metodo __str__ è un metodo speciale che viene chiamato quando si tenta di convertire l'oggetto in una stringa (ad esempio, quando si stampa l'oggetto). In questo caso, restituisce una stringa formattata con il nome e l'età dello studente. 
# Creiamo un'istanza della classe Studente con il nome "Luca" e l'età 20, e poi stampiamo l'istanza per vedere la rappresentazione leggibile dell'oggetto.
# Quando stampiamo l'istanza studente1, il metodo __str__ viene chiamato automaticamente, restituendo la stringa "Studente: Luca, età: 20".
# Output: Studente: Luca, età: 20
# Nota: Il metodo __str__ è utile per fornire una rappresentazione leggibile dell'oggetto, ma non è obbligatorio. Se non viene definito, Python utilizzerà una rappresentazione predefinita che potrebbe non essere molto informativa.  

class Studente:

    def __init__(self, nome, eta): # Il metodo __init__ è il costruttore della classe, che viene chiamato quando si crea un'istanza della classe. In questo caso, accetta due argomenti: nome e eta, e li assegna agli attributi dell'istanza.
        self.nome = nome # Gli attributi self.nome e self.eta sono variabili di istanza che vengono create per ogni istanza della classe Studente. Questi attributi memorizzano il nome e l'età dello studente, rispettivamente. L'uso di self permette di accedere a questi attributi all'interno della classe e di differenziarli da eventuali variabili locali o globali con lo stesso nome.
        self.eta = eta

    def __str__(self): # Il metodo __str__ è un metodo speciale che viene chiamato quando si tenta di convertire l'oggetto in una stringa (ad esempio, quando si stampa l'oggetto). In questo caso, restituisce una stringa formattata con il nome e l'età dello studente.
        return "Studente: " + self.nome + ", età: " + str(self.eta) # La funzione str() viene utilizzata per convertire l'attributo eta, che è un numero intero, in una stringa in modo che possa essere concatenato con le altre stringhe per creare la rappresentazione leggibile dell'oggetto.


studente1 = Studente("Luca", 20)

print(studente1)



# Esempio di metodo speciale __len__
# In questo esempio, definiamo una classe "Squadra" con un costruttore che accetta il nome della squadra e una lista di giocatori. Implementiamo il metodo speciale __len__ per restituire il numero di giocatori nella squadra quando viene chiamata la funzione len() sull'istanza della classe. Infine, creiamo un'istanza della classe Squadra e utilizziamo la funzione len() per ottenere il numero di giocatori.    
# La classe Squadra rappresenta una squadra con un nome e una lista di giocatori. Il metodo __init__ è il costruttore della classe, che accetta due argomenti: nome e giocatori, e li assegna agli attributi dell'istanza. Il metodo __len__ è un metodo speciale che viene chiamato quando si utilizza la funzione len() sull'istanza della classe. In questo caso, restituisce la lunghezza della lista di giocatori, ovvero il numero di giocatori nella squadra.
# Creiamo un'istanza della classe Squadra con il nome "Tigri" e una lista di giocatori ["Luca", "Marco", "Anna"]. Quando chiamiamo len(squadra1), il metodo __len__ viene chiamato automaticamente, restituendo il numero di giocatori nella squadra, che è 3.
# Output: 3
# Nota: Il metodo __len__ è utile per definire il comportamento della funzione len() per le istanze della classe. Se non viene definito, la funzione len() restituirà un errore quando viene chiamata sull'istanza della classe.    


class Squadra:

    def __init__(self, nome, giocatori): # Il metodo __init__ è il costruttore della classe, che accetta due argomenti: nome e giocatori, e li assegna agli attributi dell'istanza. Gli attributi self.nome e self.giocatori sono variabili di istanza che vengono create per ogni istanza della classe Squadra. Questi attributi memorizzano il nome della squadra e la lista dei giocatori, rispettivamente. L'uso di self permette di accedere a questi attributi all'interno della classe e di differenziarli da eventuali variabili locali o globali con lo stesso nome.
        self.nome = nome
        self.giocatori = giocatori

    def __len__(self):
        return len(self.giocatori)


squadra1 = Squadra("Tigri", ["Luca", "Marco", "Anna"])

print(len(squadra1))



# Esempio di metodo speciale __call__
# In questo esempio, definiamo una classe "Moltiplicatore" con un costruttore che accetta un numero. Implementiamo il metodo speciale __call__ per consentire all'istanza della classe di essere chiamata come una funzione, moltiplicando un valore dato per il numero specificato nel costruttore. Infine, creiamo un'istanza della classe Moltiplicatore e la chiamiamo con un valore per vedere il risultato.    
# La classe Moltiplicatore rappresenta un moltiplicatore con un numero specificato nel costruttore. Il metodo __init__ è il costruttore della classe, che accetta un argomento numero e lo assegna all'attributo dell'istanza. Il metodo __call__ è un metodo speciale che viene chiamato quando si tenta di chiamare l'istanza della classe come una funzione. In questo caso, accetta un argomento valore e restituisce il risultato della moltiplicazione del valore per il numero specificato nel costruttore.
# Creiamo un'istanza della classe Moltiplicatore con il numero 2. Quando chiamiamo doppio(10), il metodo __call__ viene chiamato automaticamente, restituendo il risultato della moltiplicazione di 10 per 2, che è 20.
# Output: 20    
# Nota: Il metodo __call__ è utile per consentire a un'istanza della classe di essere chiamata come una funzione, il che può essere particolarmente utile in contesti come la programmazione funzionale o quando si desidera creare oggetti che si comportano come funzioni. Se non viene definito, l'istanza della classe non potrà essere chiamata come una funzione e restituirà un errore se si tenta di farlo. 



class Moltiplicatore:

    def __init__(self, numero):
        self.numero = numero

    def __call__(self, valore):
        return valore * self.numero


doppio = Moltiplicatore(2)

print(doppio(10))




# Esempio di metodo speciale __eq__
# In questo esempio, definiamo una classe "Prodotto" con un costruttore che accetta il nome e il prezzo del prodotto. Implementiamo il metodo speciale __eq__ per consentire la comparazione tra due istanze della classe Prodotto, restituendo True se il nome e il prezzo sono uguali, altrimenti False. Infine, creiamo alcune istanze della classe Prodotto e le confrontiamo utilizzando l'operatore di uguaglianza (==) per vedere i risultati.    
# La classe Prodotto rappresenta un prodotto con un nome e un prezzo. Il metodo __init__ è il costruttore della classe, che accetta due argomenti: nome e prezzo, e li assegna agli attributi dell'istanza. Il metodo __eq__ è un metodo speciale che viene chiamato quando si utilizza l'operatore di uguaglianza (==) per confrontare due istanze della classe. In questo caso, restituisce True se il nome e il prezzo di entrambe le istanze sono uguali, altrimenti restituisce False.
# Creiamo tre istanze della classe Prodotto: prodotto1 e prodotto2 con lo stesso nome "Mouse" e lo stesso prezzo 20, e prodotto3 con un nome diverso "Tastiera" e un prezzo diverso 35. Quando confrontiamo prodotto1 con prodotto2 utilizzando l'operatore ==, il metodo __eq__ viene chiamato automaticamente, restituendo True perché entrambi hanno lo stesso nome e prezzo. Quando confrontiamo prodotto1 con prodotto3, il metodo __eq__ restituisce False perché hanno nomi e prezzi diversi.
# Output:
# True
# False
# Nota: Il metodo __eq__ è utile per definire il comportamento dell'operatore di uguaglianza (==) per le istanze della classe. Se non viene definito, l'operatore == confronterà solo gli indirizzi di memoria delle istanze, restituendo True solo se si tratta dello stesso oggetto in memoria, e non considererà i valori degli attributi. Definendo __eq__, possiamo personalizzare la logica di confronto in base ai valori degli attributi dell'istanza.  


class Prodotto:

    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def __eq__(self, altro):
        return self.nome == altro.nome and self.prezzo == altro.prezzo


prodotto1 = Prodotto("Mouse", 20)
prodotto2 = Prodotto("Mouse", 20)
prodotto3 = Prodotto("Tastiera", 35)

print(prodotto1 == prodotto2)
print(prodotto1 == prodotto3)