import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       self.dictionary = d.Dictionary()

    def printDic(self, language):

        if language == "english":
            self.dictionary.loadDictionary("resources/English.txt")
        if language == "italian":
            self.dictionary.loadDictionary("resources/Italian.txt")
        if language == "spanish":
            self.dictionary.loadDictionary("resources/Spanish.txt")


    #def searchWord(self, word, language):
        #self.printDic(language)
        #return self.dictionary.contains(word)
    def search_word_linear(self, word, language):
        self.printDic(language)
        return self.dictionary.contains_linear(word)

    def search_word_dichotomic(self, word, language):
        self.printDic(language)
        return self.dictionary.contains_dichotomic(word)



