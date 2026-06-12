# main.py

from negozio import Negozio

SCELTA_PROMPT = "Scelta: "
BACK_OPTION = "0. Indietro"

negozio = Negozio()

try:
    while True:
        print("\n=== NEGOZIO ===")
        print("1. Area cliente")
        print("2. Area admin")
        print("0. Esci")

        scelta = input(SCELTA_PROMPT)

        if scelta == "1":
            while True:
                print("\n=== AREA CLIENTE ===")
                print("1. Registrazione")
                print("2. Login")
                print(BACK_OPTION)

                scelta_cliente = input(SCELTA_PROMPT)

                if scelta_cliente == "1":
                    u = input("Username: ")
                    p = input("Password: ")
                    negozio.registra_cliente(u, p)

                elif scelta_cliente == "2":
                    u = input("Username: ")
                    p = input("Password: ")

                    cliente = negozio.login_cliente(u, p)

                    if cliente:
                        print("Login OK - Area cliente")

                        while True:
                            print("\n=== PROFILO CLIENTE ===")
                            print("1. Mostra articoli disponibili")
                            print("2. Acquista")
                            print("0. Logout")

                            s = input(SCELTA_PROMPT)

                            if s == "1":
                                negozio.mostra_articoli_disponibili()

                            elif s == "2":
                                selezione = input("Articolo (numero o nome): ")
                                qta = int(input("Quantità: "))
                                negozio.acquista(cliente, selezione, qta)

                            elif s == "0":
                                break

                    else:
                        print("Login fallito")

                elif scelta_cliente == "0":
                    break

        elif scelta == "2":
            while True:
                print("\n=== AREA ADMIN ===")
                print("1. Login")
                print(BACK_OPTION)

                scelta_admin = input(SCELTA_PROMPT)

                if scelta_admin == "1":
                    u = input("Username admin: ")
                    p = input("Password admin: ")

                    admin = negozio.login_admin(u, p)

                    if admin:
                        print("Login OK - Area admin")

                        while True:
                            print("\n=== MENU ADMIN ===")
                            print("1. Stato inventario")
                            print("2. Gestisci inventario")
                            print("3. Rapporto vendite")
                            print("0. Logout")

                            admin_scelta = input(SCELTA_PROMPT)

                            if admin_scelta == "1":
                                negozio.stato_inventario()

                            elif admin_scelta == "2":
                                while True:
                                    print("\n=== GESTIONE INVENTARIO ===")
                                    print("1. Mostra inventario")
                                    print("2. Aggiungi articolo")
                                    print("3. Aggiorna articolo")
                                    print("4. Rimuovi articolo")
                                    print("0. Indietro")

                                    scelta_inventario = input(SCELTA_PROMPT)

                                    if scelta_inventario == "1":
                                        negozio.mostra_inventario()

                                    elif scelta_inventario == "2":
                                        nome = input("Nome articolo: ")
                                        prezzo = float(input("Prezzo: "))
                                        quantita = int(input("Quantità: "))
                                        negozio.aggiungi_articolo(nome, prezzo, quantita)

                                    elif scelta_inventario == "3":
                                        nome = input("Nome articolo da aggiornare: ")
                                        prezzo_input = input("Nuovo prezzo (invio per lasciare invariato): ")
                                        quantita_input = input("Nuova quantità (invio per lasciare invariato): ")

                                        prezzo = float(prezzo_input) if prezzo_input else None
                                        quantita = int(quantita_input) if quantita_input else None

                                        negozio.aggiorna_articolo(nome, prezzo, quantita)

                                    elif scelta_inventario == "4":
                                        nome = input("Nome articolo da rimuovere: ")
                                        negozio.rimuovi_articolo(nome)

                                    elif scelta_inventario == "0":
                                        break

                            elif admin_scelta == "3":
                                negozio.report_vendite()

                            elif admin_scelta == "0":
                                break

                    else:
                        print("Login admin fallito")

                elif scelta_admin == "0":
                    break

        elif scelta == "0":
            break
except (KeyboardInterrupt, EOFError):
    print("\nUscita dal programma.")