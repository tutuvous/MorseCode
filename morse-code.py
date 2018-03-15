#assignment#8 w/ classes

#OBJECT = VARIABLES
#DATATYPE = CLASSES

class Morse(object): #inherited from base class object, #(object) is optional; default superclass for ALL classes
    def __init__(self, key, value):
        self.key = key
        self.value = value

class morseDict(object):
    def __init__(self):
        self.dictionary = {}

    def insert(self, morseCode):
        self.dictionary[morseCode.key] = morseCode.value


def readInputFile(mDict):
    csv_file = open("MorseCode.csv", "r")       #update file path if doc is not in same dir
    for line in csv_file:
        line = line.strip()
        split_line = line.split(",")
        MorseObj = Morse(split_line[1],split_line[0])
        mDict.insert(MorseObj)
    csv_file.close()
    
def translateFile(mDict, file):
    morseFile = open(file, "r")
    content = morseFile.read()                  #put all doc content into var
    words = content.split("  ")                 #separate all words w/ two spaces
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            if letter in mDict.dictionary.keys():
                print(mDict.dictionary[letter], end="") #end = "" replaces default\n end with nothing
        print(" ", end = "")
    morseFile.close()

morseDictObj = morseDict()
readInputFile(morseDictObj)
translateFile(morseDictObj, "MorseCodeText.txt")    ##update file path if doc is not in same dir
