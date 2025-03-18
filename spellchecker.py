import time
import richWord as rw
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDictionary = md.MultiDictionary()

    def handleSentence(self, txtIn, language,method ):

        incorrect_words = []
        txtIn = replaceChars(txtIn).lower()
        words = txtIn.split()
        for word in words:
            rich_word = rw.RichWord(word)
            if method =="linear":
                rich_word.corretta = self.multiDictionary.search_word_linear(word, language)
            else:
                rich_word.corretta = self.multiDictionary.search_word_dichotomic(word, language)

            if not rich_word.corretta:
                incorrect_words.append(word)
        if incorrect_words:
            print("Parole errate:", ", ".join(incorrect_words))
            print(f"Ci sono {len(incorrect_words)} parole errate.")
        else:
            print("Tutte le parole sono corrette!")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
        return text