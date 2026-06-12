# main.py

from negozio import Negozio # importa la classe Negozio per gestire le funzionalità del negozio     

SCELTA_PROMPT = "Scelta: " # definisce una costante per il prompt di input delle scelte dell'utente 
BACK_OPTION = "0. Indietro" # definisce una costante per l'opzione di tornare indietro nei menu     

negozio = Negozio() # crea un'istanza del negozio per accedere alle sue funzionalità        

try: # avvia un ciclo infinito per mostrare il menu principale del negozio e gestire le interazioni con l'utente    
    while True: # mostra il menu principale del negozio con le opzioni per accedere all'area cliente, all'area admin o uscire dal programma 
        print("\n=== NEGOZIO ===")
        print("1. Area cliente")
        print("2. Area admin")
        print("0. Esci")

        scelta = input(SCELTA_PROMPT) # legge la scelta dell'utente per accedere all'area cliente, all'area admin o uscire dal programma        

        if scelta == "1": # se l'utente sceglie di accedere all'area cliente, mostra il menu dell'area cliente con le opzioni per registrarsi, fare login o tornare indietro    
            while True: # mostra il menu dell'area cliente con le opzioni per registrarsi, fare login o tornare indietro    
                print("\n=== AREA CLIENTE ===")
                print("1. Registrazione")
                print("2. Login")
                print(BACK_OPTION)

                scelta_cliente = input(SCELTA_PROMPT) # legge la scelta dell'utente per registrarsi, fare login o tornare indietro nell'area cliente        

                if scelta_cliente == "1": # se l'utente sceglie di registrarsi, chiede username e password e chiama il metodo registra_cliente del negozio per registrare un nuovo cliente      
                    u = input("Username: ")
                    p = input("Password: ")
                    negozio.registra_cliente(u, p) # chiama il metodo registra_cliente del negozio per registrare un nuovo cliente con username e password forniti dall'utente      

                elif scelta_cliente == "2":
                    u = input("Username: ")
                    p = input("Password: ")

                    cliente = negozio.login_cliente(u, p) # chiama il metodo login_cliente del negozio per verificare le credenziali di login del cliente e ottenere un oggetto Cliente se il login è riuscito, altrimenti None     

                    if cliente: # se il login è riuscito, mostra il menu del profilo cliente con le opzioni per mostrare gli articoli disponibili, acquistare o fare logout     
                        print("Login OK - Area cliente")

                        while True: # mostra il menu del profilo cliente con le opzioni per mostrare gli articoli disponibili, acquistare o fare logout     
                            print("\n=== PROFILO CLIENTE ===")
                            print("1. Mostra articoli disponibili")
                            print("2. Acquista")
                            print("0. Logout")

                            s = input(SCELTA_PROMPT) # legge la scelta dell'utente per mostrare gli articoli disponibili, acquistare o fare logout nel profilo cliente      

                            if s == "1": # se l'utente sceglie di mostrare gli articoli disponibili, chiama il metodo mostra_articoli_disponibili del negozio per visualizzare gli articoli presenti nell'inventario del negozio        
                                negozio.mostra_articoli_disponibili() # chiama il metodo mostra_articoli_disponibili del negozio per visualizzare gli articoli presenti nell'inventario del negozio     

                            elif s == "2": # se l'utente sceglie di acquistare, chiede il nome o numero dell'articolo e la quantità da acquistare, poi chiama il metodo acquista del negozio per effettuare l'acquisto      
                                selezione = input("Articolo (numero o nome): ")
                                qta = int(input("Quantità: "))
                                negozio.acquista(cliente, selezione, qta)

                            elif s == "0": # se l'utente sceglie di fare logout, esce dal menu del profilo cliente e torna al menu dell'area cliente        
                                break

                    else: # se il login fallisce, mostra un messaggio di errore al cliente  
                        print("Login fallito")

                elif scelta_cliente == "0": # se l'utente sceglie di tornare indietro, esce dal menu dell'area cliente e torna al menu principale del negozio     
                    break

        elif scelta == "2": # se l'utente sceglie di accedere all'area admin, mostra il menu dell'area admin con le opzioni per fare login o tornare indietro       
            while True:
                print("\n=== AREA ADMIN ===")
                print("1. Login")
                print(BACK_OPTION)

                scelta_admin = input(SCELTA_PROMPT) # legge la scelta dell'utente per fare login o tornare indietro nell'area admin     

                if scelta_admin == "1": # se l'utente sceglie di fare login, chiede username e password admin e chiama il metodo login_admin del negozio per verificare le credenziali di login dell'admin e ottenere un oggetto Admin se il login è riuscito, altrimenti None    
                    u = input("Username admin: ")
                    p = input("Password admin: ")

                    admin = negozio.login_admin(u, p) # chiama il metodo login_admin del negozio per verificare le credenziali di login dell'admin e ottenere un oggetto Admin se il login è riuscito, altrimenti None  

                    if admin: # se il login è riuscito, mostra il menu del menu admin con le opzioni per visualizzare lo stato dell'inventario, gestire l'inventario, visualizzare il rapporto vendite o fare logout        
                        print("Login OK - Area admin")

                        while True: # mostra il menu del menu admin con le opzioni per visualizzare lo stato dell'inventario, gestire l'inventario, visualizzare il rapporto vendite o fare logout      
                            print("\n=== MENU ADMIN ===")
                            print("1. Stato inventario")
                            print("2. Gestisci inventario")
                            print("3. Rapporto vendite")
                            print("0. Logout")

                            admin_scelta = input(SCELTA_PROMPT) # legge la scelta dell'utente per visualizzare lo stato dell'inventario, gestire l'inventario, visualizzare il rapporto vendite o fare logout nel menu admin        

                            if admin_scelta == "1": # se l'utente sceglie di visualizzare lo stato dell'inventario, chiama il metodo stato_inventario del negozio per mostrare lo stato attuale dell'inventario del negozio     
                                negozio.stato_inventario()

                            elif admin_scelta == "2": # se l'utente sceglie di gestire l'inventario, mostra il menu di gestione dell'inventario con le opzioni per mostrare l'inventario, aggiungere un articolo, aggiornare un articolo, rimuovere un articolo o tornare indietro          
                                while True:
                                    print("\n=== GESTIONE INVENTARIO ===")
                                    print("1. Mostra inventario")
                                    print("2. Aggiungi articolo")
                                    print("3. Aggiorna articolo")
                                    print("4. Rimuovi articolo")
                                    print("0. Indietro")

                                    scelta_inventario = input(SCELTA_PROMPT)# legge la scelta dell'utente per mostrare l'inventario, aggiungere un articolo, aggiornare un articolo, rimuovere un articolo o tornare indietro nella gestione dell'inventario        

                                    if scelta_inventario == "1": # se l'utente sceglie di mostrare l'inventario, chiama il metodo mostra_inventario del negozio per visualizzare tutti gli articoli presenti nell'inventario del negozio        
                                        negozio.mostra_inventario()# chiama il metodo mostra_inventario del negozio per visualizzare tutti gli articoli presenti nell'inventario del negozio    

                                    elif scelta_inventario == "2": # se l'utente sceglie di aggiungere un articolo, chiede il nome, il prezzo e la quantità dell'articolo da aggiungere, poi chiama il metodo aggiungi_articolo del negozio per aggiungere un nuovo articolo all'inventario del negozio     
                                        nome = input("Nome articolo: ")
                                        prezzo = float(input("Prezzo: "))
                                        quantita = int(input("Quantità: "))
                                        negozio.aggiungi_articolo(nome, prezzo, quantita)

                                    elif scelta_inventario == "3": # se l'utente sceglie di aggiornare un articolo, chiede il nome dell'articolo da aggiornare e le nuove informazioni (prezzo e quantità) per l'articolo, poi chiama il metodo aggiorna_articolo del negozio per aggiornare le informazioni dell'articolo nell'inventario del negozio          
                                        nome = input("Nome articolo da aggiornare: ")
                                        prezzo_input = input("Nuovo prezzo (invio per lasciare invariato): ")
                                        quantita_input = input("Nuova quantità (invio per lasciare invariato): ")

                                        prezzo = float(prezzo_input) if prezzo_input else None
                                        quantita = int(quantita_input) if quantita_input else None

                                        negozio.aggiorna_articolo(nome, prezzo, quantita)

                                    elif scelta_inventario == "4": # se l'utente sceglie di rimuovere un articolo, chiede il nome dell'articolo da rimuovere e chiama il metodo rimuovi_articolo del negozio per rimuovere l'articolo dall'inventario del negozio       
                                        nome = input("Nome articolo da rimuovere: ")
                                        negozio.rimuovi_articolo(nome)

                                    elif scelta_inventario == "0": # se l'utente sceglie di tornare indietro, esce dal menu di gestione dell'inventario e torna al menu admin       
                                        break

                            elif admin_scelta == "3": # se l'utente sceglie di visualizzare il rapporto vendite, chiama il metodo report_vendite del negozio per mostrare un rapporto delle vendite effettuate nel negozio      
                                negozio.report_vendite()

                            elif admin_scelta == "0": # se l'utente sceglie di fare logout, esce dal menu admin e torna al menu principale del negozio      
                                break

                    else: # se il login admin fallisce, mostra un messaggio di errore all'utente        
                        print("Login admin fallito")

                elif scelta_admin == "0": # se l'utente sceglie di tornare indietro, esce dal menu dell'area admin e torna al menu principale del negozio       
                    break

        elif scelta == "0": # se l'utente sceglie di uscire dal programma, esce dal ciclo principale e termina il programma 
            break
except (KeyboardInterrupt, EOFError): # gestisce le eccezioni di interruzione da tastiera (Ctrl+C) o fine file (Ctrl+D) per uscire dal programma in modo pulito     
    print("\nUscita dal programma.")