class Dictionary:
    def __init__(self):
        self.dictionary = []

    def loadDictionary(self,path):
        with open(path,'r',encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                self.dictionary.append(line)



    #def contains(self,word):
        #return word in self.dictionary



    def contains_linear(self, word):
        for w in self.dictionary:
            if w == word:
                return True
        return False

    def contains_dichotomic(self, word):
        left, right = 0, len(self.dictionary) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.dictionary[mid] == word:
                return True
            elif self.dictionary[mid] < word:
                left = mid + 1
            else:
                right = mid - 1
        return False