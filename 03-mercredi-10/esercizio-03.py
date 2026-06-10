# Esercizio 3: Conto Corrente
# Crea una classe "ContoCorrente" con i seguenti attributi: intestatario e saldo. Aggiungi i metodi "deposita" e "preleva" per modificare il saldo, e un metodo "stampa_saldo" per visualizzare il saldo attuale. Crea un'istanza della classe e dimostra l'utilizzo dei metodi.    
# La classe ContoCorrente rappresenta un conto bancario con un intestatario e un saldo. Il metodo __init__ è il costruttore della classe, che inizializza l'intestatario e il saldo (con un valore predefinito di 0). Il metodo deposita consente di aggiungere denaro al saldo, mentre il metodo preleva consente di sottrarre denaro dal saldo, con controlli per importi non validi e saldo insufficiente. Il metodo stampa_saldo visualizza il saldo attuale del conto. 

class ContoCorrente:
    def __init__(self, intestatario, saldo=0):# Il metodo __init__ è il costruttore della classe, che viene chiamato quando si crea un'istanza della classe. In questo caso, accetta due argomenti: intestatario e saldo (con un valore predefinito di 0). Assegna questi valori agli attributi dell'istanza.
        self.intestatario = intestatario # L'attributo self.intestatario viene assegnato al valore del parametro intestatario passato al costruttore. Lo stesso vale per saldo.
        self.saldo = saldo

    def deposita(self, importo): # Il metodo deposita è un metodo della classe ContoCorrente che consente di aggiungere denaro al saldo. Accetta un argomento importo, che rappresenta la quantità di denaro da depositare. Il metodo verifica se l'importo è valido (maggiore di zero) prima di aggiungerlo al saldo.
        if importo <= 0:
            print("Errore: l'importo deve essere maggiore di zero.")
        else:
            self.saldo += importo

    def preleva(self, importo):
        if importo <= 0:
            print("Errore: l'importo deve essere maggiore di zero.")
        elif importo > self.saldo:
            print("Errore: saldo insufficiente.")
        else:
            self.saldo -= importo

    def stampa_saldo(self):
        print(f"Il saldo di '{self.intestatario}' è: {self.saldo} €")
        

conto = ContoCorrente("Mario Rossi", 100)

conto.stampa_saldo()

conto.deposita(50)
conto.stampa_saldo()

conto.preleva(30)
conto.stampa_saldo()

conto.preleva(200)
conto.deposita(-10)