# Questo modulo contiene una funzione per salutare e una classe per rappresentare un cerchio con un metodo per calcolare l'area. La funzione saluta accetta un nome come argomento e stampa un messaggio di saluto. La classe Cerchio ha un costruttore che accetta il raggio del cerchio e un metodo area che calcola e restituisce l'area del cerchio utilizzando la formula A = π * r^2, dove π è approssimato a 3.14159. Questo modulo può essere importato in altri file Python per utilizzare la funzione di saluto e la classe Cerchio.  

def saluta(nome): # La funzione saluta accetta un nome come argomento e stampa un messaggio di saluto. Ad esempio, se si chiama saluta("Alice"), la funzione stamperà "Ciao, Alice". Questa funzione può essere utilizzata per salutare qualsiasi persona passando il loro nome come argomento. 
    print("Ciao,", nome)


PI = 3.14159


class Cerchio:

    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return PI * self.raggio ** 2