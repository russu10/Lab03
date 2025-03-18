import spellchecker
import time

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = int(input("Scegli una lingua o termina: "))
    # Add input control here!

    if int(txtIn) == 1:
        method = input("inserisci il metodo(linear/dichotomic): ")
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        tic = time.time()
        sc.handleSentence(txtIn,"italian",method)
        toc = time.time()
        print(f"tempo : {toc-tic}")
        continue

    if int(txtIn) == 2:
        method = input("inserisci il metodo(linear/dichotomic): ")
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        tic = time.time()
        sc.handleSentence(txtIn, "english", method)
        toc = time.time()
        print(f"tempo : {toc - tic}")
        continue

    if int(txtIn) == 3:
        method = input("inserisci il metodo(linear/dichotomic): ")
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        tic = time.time()
        sc.handleSentence(txtIn, "spanish", method)
        toc = time.time()
        print(f"tempo : {toc - tic}")
        continue

    if int(txtIn) == 4:
        break


