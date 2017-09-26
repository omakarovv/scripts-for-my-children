#!/usr/bin/env python

### Count symbols in the text ###
def getAllLettersRus():
    for item in range(1072, 1104):
        yield unichr(item)

def getAllSymbolsRus():
    for symb in range(33, 64):
        yield unichr(symb)

if __name__ == '__main__':
    for rus in getAllLettersRus():

        with open("text.txt", "r") as f:
            file = f.read().decode('cp1251').lower()
            alaphab = file.count(rus)
        print("%s - %d" % (rus, alaphab))

    for sym in getAllSymbolsRus():
        with open("text.txt", "r") as f:
            file = f.read().decode('cp1251').lower()
            symbols = file.count(sym)
            print("%s - %d" % (sym, symbols))
    
    print("Total:", len(file) - file.count(' '))

### My version ###
