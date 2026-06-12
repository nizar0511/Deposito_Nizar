#esercizio 5: Creare una classe Convertitore con due metodi statici: euro_in_dollari(euro) e km_in_miglia(km). Il primo metodo deve convertire un importo in euro in dollari, mentre il secondo metodo deve convertire una distanza in chilometri in miglia. Utilizzare i seguenti tassi di conversione: 1 euro = 1.08 dollari e 1 km = 0.621371 miglia.    
# La classe Convertitore contiene due metodi statici, euro_in_dollari e km_in_miglia, che eseguono le conversioni richieste. I metodi sono decorati con @staticmethod, il che significa che possono essere chiamati direttamente sulla classe senza la necessità di creare un'istanza della classe. Il metodo euro_in_dollari accetta un importo in euro e restituisce il corrispondente importo in dollari utilizzando il tasso di conversione specificato. Il metodo km_in_miglia accetta una distanza in chilometri e restituisce la distanza equivalente in miglia utilizzando il tasso di conversione specificato. Infine, vengono chiamati entrambi i metodi per dimostrare il loro funzionamento.    
# Output: 108.0
#         6.21371

class Convertitore: # La classe Convertitore rappresenta un convertitore con due metodi statici per eseguire le conversioni richieste. I metodi euro_in_dollari e km_in_miglia sono definiti come metodi statici, il che significa che possono essere chiamati direttamente sulla classe senza la necessità di creare un'istanza della classe. Questi metodi accettano i valori da convertire come argomenti e restituiscono i risultati delle conversioni utilizzando i tassi di conversione specificati.  

    @staticmethod # Il decoratore @staticmethod indica che il metodo è un metodo statico, il che significa che può essere chiamato direttamente sulla classe senza la necessità di creare un'istanza della classe. I metodi statici non accettano un parametro self, poiché non operano su istanze specifiche della classe, ma piuttosto su dati forniti come argomenti. In questo caso, i metodi euro_in_dollari e km_in_miglia sono definiti come metodi statici perché eseguono conversioni basate sui valori passati come argomenti e non richiedono l'accesso a dati o attributi specifici dell'istanza della classe.  
    def euro_in_dollari(euro): # Il metodo euro_in_dollari accetta un importo in euro come argomento e restituisce il corrispondente importo in dollari utilizzando il tasso di conversione specificato (1 euro = 1.08 dollari). Poiché è un metodo statico, può essere chiamato direttamente sulla classe Convertitore senza la necessità di creare un'istanza della classe. Ad esempio, Convertitore.euro_in_dollari(100) restituirà 108.0, che è il risultato della conversione di 100 euro in dollari.
        return euro * 1.08 # Il metodo restituisce il risultato della conversione moltiplicando l'importo in euro per il tasso di conversione di 1.08 dollari per euro. Ad esempio, se si chiama Convertitore.euro_in_dollari(100), il metodo restituirà 108.0, che è il risultato della conversione di 100 euro in dollari.    

    @staticmethod
    def km_in_miglia(km):
        return km * 0.621371
    
    
print(Convertitore.euro_in_dollari(200))
print(Convertitore.km_in_miglia(20))