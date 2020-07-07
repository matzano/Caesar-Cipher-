
class Ciper:
    def __init__(self):
        self.dictionary = {0: 'a', 1 : 'b', 2:'c', 3: 'd',
        4:'e', 5: 'f', 6:'g', 7: 'h', 8:'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
        13: 'n', 14:'o', 15: 'p', 16: 'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w',
        23: 'x', 24:'y', 25:'z'}

        self.decryptionDictionary = {'a':0 , 'b':1, 'c':2, 'd':3,
        'e':4 , 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12,
        'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22,
        'x':23, 'y':24, 'z':25}

        self.numWordLis = []
        self.encryptionList = []
        self.decryptListNum = []
        self.decryptListWord = []



    def encryption(self, word):
        newWord = word.lower()
        for char in newWord:
            for key in self.dictionary:
                if self.dictionary[key] == char:
                    char = key
            self.numWordLis.append(char)
        for index in self.numWordLis:
            if index ==' ':
                letter = '*'
            elif index == 23:
                letter = 'a'
            elif index == 24:
                letter = 'b'
            elif index == 25:
                letter ='c'
            else:
                newChar = index + 3
                letter = self.dictionary[newChar]
            self.encryptionList.append(letter)
        nospace = ''
        encyrptedWord = nospace.join(self.encryptionList)
        print(encyrptedWord)
        return encyrptedWord


    def decryption(self):
        for char in self.encryptionList:
            if char == 'x':
                value = 0
                self.decryptListNum.append(value)
            elif char == 'y':
                value = 1
                self.decryptListNum.append(value)
            elif char == 'z':
                value = 2
                self.decryptListNum.append(value)
            elif char =='*':
                value = ' '
                self.decryptListNum.append(value)
            elif char == 'a':
                value = 23
                self.decryptListNum.append(value)
            elif char == 'b':
                value = 24
                self.decryptListNum.append(value)
            elif char == 'c':
                value = 25
                self.decryptListNum.append(value)
            else:
                value = self.decryptionDictionary[char]
                newLetter = value - 3
                self.decryptListNum.append(newLetter)
        for number in self.decryptListNum:
            for index in self.dictionary:
                if index == number:
                    character = self.dictionary[index]
                    self.decryptListWord.append(character)
        nospaces = ''
        decryptedWord = nospaces.join(self.decryptListWord)
        print(decryptedWord)
        return decryptedWord




test = Ciper()

test.encryption('xyz')
test.decryption()



