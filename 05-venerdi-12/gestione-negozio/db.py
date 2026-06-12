# db.py
from pymongo import MongoClient # importa MongoClient per connettersi a MongoDB 

client = MongoClient("mongodb://localhost:27017/") # crea un client MongoDB con l'URL di connessione al server locale   

db = client["negozio_db"] # seleziona il database "negozio_db" (verrà creato se non esiste)

clienti_col = db["clienti"] # crea una collezione "clienti" per memorizzare i dati dei clienti (verrà creata se non esiste)
inventario_col = db["inventario"] # crea una collezione "inventario" per memorizzare i dati degli articoli (verrà creata se non esiste)
vendite_col = db["vendite"] # crea una collezione "vendite" per memorizzare i dati delle vendite (verrà creata se non esiste)
admin_col = db["admin"] # crea una collezione "admin" per memorizzare i dati degli amministratori (verrà creata se non esiste)