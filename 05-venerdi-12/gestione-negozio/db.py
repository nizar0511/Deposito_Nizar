
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["negozio_db"]

clienti_col = db["clienti"]
inventario_col = db["inventario"]
vendite_col = db["vendite"]
admin_col = db["admin"]