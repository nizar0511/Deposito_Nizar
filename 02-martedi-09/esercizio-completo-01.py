# Esercizio Completo: Menu con IF, WHILE e FOR
# Scrivi un programma che presenta un menu all'utente con le seguenti opzioni:
# 1. Pari o Dispari (IF)
# 2. Conta da n a 0 (WHILE + range)
# 3. Quadrato dei numeri (FOR)
# 4. Analisi lista (IF + WHILE + FOR)
# 5. Esci
# Per ogni opzione, implementa la funzionalità richiesta utilizzando le strutture di controllo appropriate. Il programma deve continuare a mostrare il menu finché l'utente non sceglie di uscire.
# Dettagli:
# - Per l'opzione 1, chiedi all'utente di inserire un numero e determina se è pari o dispari.
# - Per l'opzione 2, chiedi all'utente di inserire un numero intero positivo e conta da quel numero a 0, stampando ogni numero.
# - Per l'opzione 3, chiedi all'utente di inserire una lista di numeri separati da spazio e stampa il quadrato di ciascun numero.
# - Per l'opzione 4, chiedi all'utente di inserire una lista di numeri separati da spazio e:
#   - Usa un IF per verificare se la lista è vuota e stampa "Lista Vuota" se è il caso.
#   - Usa un FOR per trovare il numero massimo nella lista.
#   - Usa un WHILE per contare quanti elementi ci sono nella lista e stampa il conteggio.
# - Per l'opzione 5, esci dal programma.

while True:
    print("\n=== MENU PRINCIPALE ===")
    print("1 - Pari o Dispari (IF)")
    print("2 - Conta da n a 0 (WHILE + range)")
    print("3 - Quadrato dei numeri (FOR)")
    print("4 - Analisi lista (IF + WHILE + FOR)")
    print("5 - Esci")

    scelta = input("Scegli un'opzione: ")

    # -------------------------------
    # PUNTO 1 — IF (Pari o Dispari)
    # -------------------------------
    if scelta == "1":
        numero = int(input("Inserisci un numero: "))

        if numero % 2 == 0:
            print("Pari")
        else:
            print("Dispari")

    # -----------------------------------------------
    # PUNTO 2 — WHILE + range (conta da n a 0)
    # -----------------------------------------------
    elif scelta == "2":
        n = int(input("Inserisci un numero intero positivo: "))

        for i in range(n, 0 - 1, -1):
            print(i)

    # -----------------------------------------------
    # PUNTO 3 — FOR (quadrato dei numeri)
    # -----------------------------------------------
    elif scelta == "3":
        lista = input("Inserisci numeri separati da spazio: ").split()
        lista = [int(x) for x in lista]

        print("Quadrati:")
        for numero in lista:
            print(numero ** 2)

    # ---------------------------------------------------------
    # PUNTO 4 — IF + WHILE + FOR (massimo, conteggio, lista)
    # ---------------------------------------------------------
    elif scelta == "4":
        lista = input("Inserisci numeri separati da spazio: ").split()
        lista = [int(x) for x in lista]

        # IF → lista vuota?
        if len(lista) == 0:
            print("Lista Vuota")
        else:
            # FOR → trovare il massimo
            massimo = lista[0]
            for num in lista:
                if num > massimo:
                    massimo = num

            # WHILE → contare gli elementi
            conteggio = 0
            i = 0
            while i < len(lista):
                conteggio += 1
                i += 1

            print("Numero massimo:", massimo)
            print("Numero di elementi:", conteggio)

    # -------------------------------
    # USCITA
    # -------------------------------
    elif scelta == "5":
        print("Uscita dal programma...")
        break

    else:
        print("Scelta non valida.")





