

from libreria_modulo import Libro, Libreria

# Creazione libreria
libreria = Libreria()

# Creazione libri
libro1 = Libro("1984", "George Orwell", "ISBN001")
libro2 = Libro("Il Nome della Rosa", "Umberto Eco", "ISBN002")
libro3 = Libro("1984", "Altro Autore", "ISBN003")

# Aggiunta libri
libreria.aggiungi_libro(libro1)
libreria.aggiungi_libro(libro2)
libreria.aggiungi_libro(libro3)

# Mostra catalogo
print("CATALOGO:")
libreria.mostra_catalogo()

# Ricerca per titolo
print("\nRISULTATI RICERCA:")
risultati = libreria.cerca_per_titolo("1984")
for libro in risultati:
    print(libro.descrizione())

# Rimozione libro
libreria.rimuovi_libro("ISBN002")

print("\nCATALOGO DOPO RIMOZIONE:")
libreria.mostra_catalogo()