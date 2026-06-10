# Esercizio 4: Garage
# Crea una classe "Garage" che rappresenta un garage per auto. La classe dovrebbe avere un attributo "capienza" che indica il numero massimo di auto che il garage può contenere, e un attributo "auto_presenti" che è una lista delle targhe delle auto attualmente parcheggiate nel garage. Implementa i seguenti metodi:
# - parcheggia(targa): Aggiunge un'auto con la targa specificata al garage, se c'è spazio disponibile. Se il garage è pieno, stampa un messaggio di errore.
# - rimuovi(targa): Rimuove l'auto con la targa specificata dal garage, se è presente. Se l'auto non è trovata, stampa un messaggio di errore.
# - posti_liberi(): Restituisce il numero di posti liberi disponibili nel garage.
# Esempio di utilizzo:
# garage = Garage(2)
# garage.parcheggia("ABC123")
# garage.parcheggia("XYZ789")
# garage.parcheggia("DEF456")  # Errore: garage pieno.
# print(garage.posti_liberi())  # Output: 0
# garage.rimuovi("ABC123")
# print(garage.posti_liberi())  # Output: 1

# La classe Garage rappresenta un garage per auto con una capacità massima e una lista di auto presenti. Il metodo parcheggia consente di aggiungere un'auto al garage se c'è spazio disponibile, altrimenti stampa un messaggio di errore. Il metodo rimuovi consente di rimuovere un'auto dal garage se è presente, altrimenti stampa un messaggio di errore. Il metodo posti_liberi restituisce il numero di posti liberi disponibili nel garage calcolando la differenza tra la capacità totale e il numero di auto attualmente presenti.   


class Garage:

    def __init__(self, capienza): # Il metodo __init__ è il costruttore della classe, che accetta un argomento capienza e lo assegna all'attributo dell'istanza. L'attributo self.capienza memorizza la capacità massima del garage, mentre l'attributo self.auto_presenti è una lista che memorizza le targhe delle auto attualmente parcheggiate nel garage. L'uso di self permette di accedere a questi attributi all'interno della classe e di differenziarli da eventuali variabili locali o globali con lo stesso nome.   
        self.capienza = capienza # L'attributo self.capienza memorizza la capacità massima del garage, ovvero il numero massimo di auto che il garage può contenere. Questo valore viene specificato quando si crea un'istanza della classe Garage e viene utilizzato nei metodi parcheggia e posti_liberi per determinare se c'è spazio disponibile nel garage e per calcolare il numero di posti liberi.  
        self.auto_presenti = [] # L'attributo self.auto_presenti è una lista che memorizza le targhe delle auto attualmente parcheggiate nel garage. Inizialmente, questa lista è vuota, ma viene aggiornata ogni volta che un'auto viene parcheggiata o rimossa dal garage utilizzando i metodi parcheggia e rimuovi. La lista self.auto_presenti viene utilizzata nei metodi parcheggia, rimuovi e posti_liberi per verificare se un'auto è presente nel garage e per calcolare il numero di posti liberi disponibili.    

    def parcheggia(self, targa): # Il metodo parcheggia consente di aggiungere un'auto al garage se c'è spazio disponibile. Accetta un argomento targa, che rappresenta la targa dell'auto da parcheggiare. Il metodo verifica se il numero di auto attualmente presenti nel garage è inferiore alla capacità massima (self.capienza) e se l'auto con la targa specificata non è già presente nel garage (controllando se targa è in self.auto_presenti). Se entrambe le condizioni sono soddisfatte, l'auto viene aggiunta alla lista self.auto_presenti. Altrimenti, viene stampato un messaggio di errore indicando che il garage è pieno o che l'auto è già presente.
        if len(self.auto_presenti) >= self.capienza: # Il metodo len() viene utilizzato per ottenere il numero di auto attualmente presenti nel garage, che è dato dalla lunghezza della lista self.auto_presenti. Se questo numero è maggiore o uguale alla capacità massima del garage (self.capienza), significa che il garage è pieno e non è possibile parcheggiare un'altra auto, quindi viene stampato un messaggio di errore.
            print("Errore: garage pieno.")
        elif targa in self.auto_presenti: # Il controllo elif targa in self.auto_presenti verifica se l'auto con la targa specificata è già presente nel garage. Se la targa è già nella lista self.auto_presenti, significa che l'auto è già parcheggiata nel garage e non può essere parcheggiata di nuovo, quindi viene stampato un messaggio di errore.
            print("Errore: auto già presente in garage.")
        else:
            self.auto_presenti.append(targa)    # Il metodo append() viene utilizzato per aggiungere la targa dell'auto alla lista self.auto_presenti quando l'auto viene parcheggiata con successo nel garage. Questo metodo modifica la lista self.auto_presenti aggiungendo un nuovo elemento alla fine della lista, che in questo caso è la targa dell'auto appena parcheggiata.
    def rimuovi(self, targa): # Il metodo rimuovi consente di rimuovere un'auto dal garage se è presente. Accetta un argomento targa, che rappresenta la targa dell'auto da rimuovere. Il metodo verifica se l'auto con la targa specificata è presente nel garage (controllando se targa è in self.auto_presenti). Se l'auto è presente, viene rimossa dalla lista self.auto_presenti. Altrimenti, viene stampato un messaggio di errore indicando che l'auto non è trovata nel garage.
        if targa in self.auto_presenti:
            self.auto_presenti.remove(targa)
        else:
            print("Errore: auto non trovata nel garage.")
    
    def posti_liberi(self): # Il metodo posti_liberi restituisce il numero di posti liberi disponibili nel garage calcolando la differenza tra la capacità totale del garage (self.capienza) e il numero di auto attualmente presenti nel garage (len(self.auto_presenti)). La funzione len() viene utilizzata per ottenere il numero di auto attualmente presenti nel garage, che è dato dalla lunghezza della lista self.auto_presenti. Restituendo questa differenza, il metodo fornisce il numero di posti liberi disponibili nel garage.
        return self.capienza - len(self.auto_presenti)
    

garage = Garage(2)

garage.parcheggia("AB123CD")
garage.parcheggia("EF456GH")

print(garage.posti_liberi())

garage.parcheggia("IJ789KL")  # garage pieno

garage.rimuovi("AB123CD")

print(garage.posti_liberi())
