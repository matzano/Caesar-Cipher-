class Text:
    def __init__(self, textFile):
        self.textFile = textFile

    def read_txt_file(self):
        readFile = open(self.textFile, 'r')
        lsOfText = readFile.readlines()
        print(lsOfText)
        readFile.close()
        return lsOfText

    def write_txt_file(self):
        writeFile = open(self.textFile, 'w')
        writeFile.close()
        return writeFile

test = Text(r"C:\Users\Matthew\Documents\Python_Projects\Caesar-Cipher-\cipher_project\practice.txt")
test.read_txt_file()


