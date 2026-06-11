# Importare il modulo mio_modulo e utilizzare le sue funzioni e classi. 
# Il modulo mio_modulo contiene una funzione saluta che accetta un nome come argomento e stampa un messaggio di saluto, e una classe Cerchio con un metodo area che calcola l'area di un cerchio dato il suo raggio. 
# In questo esempio, importiamo il modulo mio_modulo, chiamiamo la funzione saluta per salutare "Alice", creiamo un'istanza della classe Cerchio con un raggio di 2 e stampiamo l'area del cerchio calcolata dal metodo area. 
# Questo dimostra come importare e utilizzare un modulo in Python per accedere a funzioni e classi definite in un altro file.
import mio_modulo
mio_modulo.saluta("Alice") # Stampa "Ciao, Alice"
raggio = 2
cerchio = mio_modulo.Cerchio(raggio)
print(cerchio.area()) # Stampa l'area del cerchio con raggio 2