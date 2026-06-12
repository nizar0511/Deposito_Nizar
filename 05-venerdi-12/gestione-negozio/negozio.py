from db import admin_col, clienti_col, inventario_col, vendite_col
from amministratore import Amministratore
from articolo import Articolo
from cliente import Cliente

ARTICOLO_NON_TROVATO = "Articolo non trovato"

class Negozio:

    def _stampa_tabella(self, intestazioni, righe):
        larghezze = [len(str(intestazione)) for intestazione in intestazioni]

        for riga in righe:
            for indice, valore in enumerate(riga):
                larghezze[indice] = max(larghezze[indice], len(str(valore)))

        def formatta_riga(valori):
            parti = []
            for indice, valore in enumerate(valori):
                parti.append(str(valore).ljust(larghezze[indice]))
            return " | ".join(parti)

        separatore = "-+-".join("-" * larghezza for larghezza in larghezze)

        print(formatta_riga(intestazioni))
        print(separatore)

        for riga in righe:
            print(formatta_riga(riga))

    # ---------- CLIENTI ----------
    def registra_cliente(self, u, p):
        if clienti_col.find_one({"username": u}):
            print("Cliente già esistente")
            return

        clienti_col.insert_one({
            "username": u,
            "password": p
        })

        print("Cliente registrato")

    def login_cliente(self, u, p):
        data = clienti_col.find_one({"username": u, "password": p})
        if data:
            return Cliente(u, p)
        return None

    def login_admin(self, u, p):
        data = admin_col.find_one({"username": u, "password": p})
        if data:
            return Amministratore(u, p)
        return None

    def registra_admin(self, u, p):
        if admin_col.find_one({"username": u}):
            print("Admin già esistente")
            return

        admin_col.insert_one({
            "username": u,
            "password": p
        })

        print("Admin registrato")

    # ---------- INVENTARIO ----------
    def aggiungi_articolo(self, nome, prezzo, quantita):
        if inventario_col.find_one({"nome": nome}):
            print("Articolo già presente in inventario")
            return

        inventario_col.insert_one({
            "nome": nome,
            "prezzo": prezzo,
            "quantita": quantita
        })

        print("Articolo aggiunto")

    def mostra_inventario(self):
        self.stato_inventario()

    def stato_inventario(self):
        articoli = list(inventario_col.find())

        print("\nSTATO INVENTARIO")

        if not articoli:
            print("Inventario vuoto")
            return

        totale_quantita = 0
        righe = []

        for a in articoli:
            righe.append([
                a["nome"],
                f"€{a['prezzo']:.2f}",
                a["quantita"]
            ])
            totale_quantita += a["quantita"]

        self._stampa_tabella(["Nome", "Prezzo", "Quantità"], righe)

        print(f"\nARTICOLI TOTALI IN MAGAZZINO: {totale_quantita}")

    def articoli_disponibili(self):
        return list(inventario_col.find({"quantita": {"$gt": 0}}))

    def aggiorna_articolo(self, nome, prezzo=None, quantita=None):
        aggiornamenti = {}

        if prezzo is not None:
            aggiornamenti["prezzo"] = prezzo

        if quantita is not None:
            aggiornamenti["quantita"] = quantita

        if not aggiornamenti:
            print("Nessun dato da aggiornare")
            return

        risultato = inventario_col.update_one(
            {"nome": nome},
            {"$set": aggiornamenti}
        )

        if risultato.matched_count == 0:
            print(ARTICOLO_NON_TROVATO)
            return

        print("Articolo aggiornato")

    def rimuovi_articolo(self, nome):
        risultato = inventario_col.delete_one({"nome": nome})

        if risultato.deleted_count == 0:
            print(ARTICOLO_NON_TROVATO)
            return

        print("Articolo rimosso")

    def mostra_articoli_disponibili(self):
        print("\nARTICOLI DISPONIBILI")
        for indice, articolo in enumerate(self.articoli_disponibili(), start=1):
            print(f"{indice}- {articolo['nome']} {articolo['prezzo']} {articolo['quantita']}")

    def cerca_articolo(self, nome):
        return inventario_col.find_one({"nome": nome})

    def risolvi_articolo(self, selezione):
        articoli = self.articoli_disponibili()

        if selezione.isdigit():
            indice = int(selezione) - 1
            if 0 <= indice < len(articoli):
                return articoli[indice]

        for articolo in articoli:
            if articolo["nome"].lower() == selezione.lower():
                return articolo

        return None

    # ---------- ACQUISTO ----------
    def acquista(self, cliente, selezione, qta):

        art = self.risolvi_articolo(selezione)

        if not art:
            print(ARTICOLO_NON_TROVATO)
            return

        if art["quantita"] < qta:
            print("Quantità non disponibile")
            return

        totale = art["prezzo"] * qta

        # aggiorna inventario
        inventario_col.update_one(
            {"nome": art["nome"]},
            {"$inc": {"quantita": -qta}}
        )

        # salva vendita
        vendite_col.insert_one({
            "cliente": cliente.username,
            "articolo": art["nome"],
            "quantita": qta,
            "totale": totale
        })

        print(f"Acquisto completato: €{totale}")

    # ---------- ADMIN ----------
    def report_vendite(self):
        print("\n--- REPORT VENDITE ---")

        vendite = list(vendite_col.find())

        if not vendite:
            print("Nessuna vendita registrata")
            print("\nGUADAGNO TOTALE: €0")
            return

        righe = []

        for v in vendite:
            righe.append([
                v["cliente"],
                v["articolo"],
                v["quantita"],
                f"€{v['totale']:.2f}"
            ])

        self._stampa_tabella(["Cliente", "Articolo", "Qta", "Totale"], righe)

        print(f"\nGUADAGNO TOTALE: €{self.totale_guadagni()}")

    def totale_guadagni(self):
        totale = 0

        for vendita in vendite_col.find():
            totale += vendita.get("totale", 0)

        return totale