#esercizio 7: Creare una classe Ristorante con i seguenti attributi: nome, tipo_cucina, aperto (booleano) e menu (dizionario). La classe deve avere i seguenti metodi: descrivi_ristorante(), stato_apertura(), apri_ristorante(), chiudi_ristorante(), aggiungi_al_menu(piatto, prezzo), togli_dal_menu(piatto) e stampa_menu(). Il metodo descrivi_ristorante() deve stampare il nome e il tipo di cucina del ristorante. Il metodo stato_apertura() deve stampare se il ristorante è aperto o chiuso. I metodi apri_ristorante() e chiudi_ristorante() devono modificare lo stato di apertura del ristorante. I metodi aggiungi_al_menu() e togli_dal_menu() devono modificare il menu del ristorante, mentre il metodo stampa_menu() deve stampare tutti i piatti presenti nel menu con i loro prezzi.    
# La classe Ristorante rappresenta un ristorante con attributi come nome, tipo di cucina, stato di apertura e menu. I metodi della classe consentono di descrivere il ristorante, verificare lo stato di apertura, aprire o chiudere il ristorante, aggiungere o rimuovere piatti dal menu e stampare il menu completo. La classe utilizza un dizionario per memorizzare i piatti e i loro prezzi, consentendo una gestione flessibile del menu. Infine, viene creata un'istanza della classe Ristorante e vengono chiamati i vari metodi per dimostrare il funzionamento della classe.    

class Ristorante:

    def __init__(self, nome, tipo_cucina): # Il metodo __init__ è il costruttore della classe Ristorante, che accetta due argomenti: nome e tipo_cucina. Questi argomenti vengono utilizzati per inizializzare gli attributi dell'istanza self.nome e self.tipo_cucina, che memorizzano rispettivamente il nome del ristorante e il tipo di cucina offerto. Inoltre, all'interno del costruttore, viene inizializzato l'attributo self.aperto a False, indicando che il ristorante è chiuso all'inizio, e viene creato un dizionario vuoto self.menu per memorizzare i piatti e i loro prezzi. Questo costruttore consente di creare istanze della classe Ristorante con le informazioni di base necessarie per rappresentare un ristorante.    
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}

    def descrivi_ristorante(self):
        print(f"Ristorante: {self.nome}")
        print(f"Tipo di cucina: {self.tipo_cucina}")

    def stato_apertura(self):
        if self.aperto:
            print("Il ristorante è aperto.")
        else:
            print("Il ristorante è chiuso.")

    def apri_ristorante(self):
        self.aperto = True
        print(f"{self.nome} è ora aperto.")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"{self.nome} è ora chiuso.")

    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo
        print(f"{piatto} aggiunto al menu.")

    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"{piatto} rimosso dal menu.")
        else:
            print("Piatto non presente nel menu.")

    def stampa_menu(self):
        if len(self.menu) == 0:
            print("Il menu è vuoto.")
        else:
            print("\n--- MENU ---")
            for piatto, prezzo in self.menu.items():
                print(f"{piatto}: {prezzo} €")
                




# Creazione del ristorante
ristorante = Ristorante("La Bella Napoli", "Italiana")

# Descrizione
ristorante.descrivi_ristorante()

# Stato iniziale
ristorante.stato_apertura()

# Apertura
ristorante.apri_ristorante()
ristorante.stato_apertura()

# Aggiunta piatti
ristorante.aggiungi_al_menu("Pizza Margherita", 8)
ristorante.aggiungi_al_menu("Lasagna", 12)
ristorante.aggiungi_al_menu("Tiramisù", 6)

# Stampa menu
ristorante.stampa_menu()

# Rimozione piatto
ristorante.togli_dal_menu("Lasagna")

# Stampa menu aggiornata
ristorante.stampa_menu()

# Chiusura
ristorante.chiudi_ristorante()
ristorante.stato_apertura()