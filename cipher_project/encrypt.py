import thetext
from thetext import Text



class Ciper:
    def __init__(self, filename):
        self.dictionary = {0: 'a', 1 : 'b', 2:'c', 3: 'd',
        4:'e', 5: 'f', 6:'g', 7: 'h', 8:'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
        13: 'n', 14:'o', 15: 'p', 16: 'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w',
        23: 'x', 24:'y', 25:'z', 26: ' '}

        self.decryptionDictionary = {'a':0 , 'b':1, 'c':2, 'd':3,
        'e':4 , 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12,
        'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22,
        'x':23, 'y':24, 'z':25, ' ': 26}

        #encryption lists
        self.numWordLis = []
        self.encryptionList = []
        self.txtListLines = []
        self.aFile = Text(filename)

        #decryption lists
        self.decryptionNumbers = []
        self.decryptedWord = []
        



    def text_file_words(self):
        self.LinesOfWords = self.aFile.read_txt_file()
        return self.LinesOfWords



    def encryption(self):
        for line in self.LinesOfWords:
            self.newWord = line.lower()
            self.txtListLines.append(self.newWord)
        for newWord in self.txtListLines:
            for char in newWord:
                for key in self.dictionary:
                    if self.dictionary[key] == char:
                        self.numWordLis.append(key)
        for index in self.numWordLis:
            newChar = (index + 3) % 27
            letter = self.dictionary[newChar]
            self.encryptionList.append(letter)
        nospace = ''
        self.encyrptedWord = nospace.join(self.encryptionList)
        print(self.encyrptedWord)
        return self.encyrptedWord


    def decryption(self):
        for char in self.encyrptedWord:
            for key in self.decryptionDictionary:
                if key == char:
                    self.decryptionNumbers.append(self.decryptionDictionary[key])
        print(self.decryptionNumbers)
        for i,letter in enumerate(self.decryptionNumbers):
            newValue = letter - 3
            if newValue < 0:
                newValue += 27
            self.decryptionNumbers[i] = newValue
        for j, number in enumerate(self.decryptionNumbers):
            for char in self.dictionary:
                if char == number:
                    self.decryptionNumbers[j] = self.dictionary[char]
        print(self.decryptionNumbers)
        nospc = ''
        self.decryptedWord = nospc.join(self.decryptionNumbers)
        print(self.decryptedWord)
        return self.decryptedWord


        

                
                

            
        



test = Ciper(r"C:\Users\Matthew\Documents\Python_Projects\Caesar-Cipher-\cipher_project\practice.txt")
test.text_file_words()
test.encryption()
test.decryption()



