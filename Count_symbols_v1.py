#!/usr/bin/env python3

def getAllLettersRus():
    for item in range(1072, 1104):
        yield chr(item)


def getAllSymbolsRus():
    for symb in range(33, 64):
        yield chr(symb)


if __name__ == '__main__':
    for rus in getAllLettersRus():
        with open("text.txt", "r", encoding="cp1251") as f:
            file = f.read().lower()
            alaphab = file.count(rus)
        print("%s - %d" % (rus, alaphab))

    for sym in getAllSymbolsRus():
        with open("text.txt", "r", encoding="cp1251") as f:
            file = f.read().lower()
            symbols = file.count(sym)
            print("%s - %d" % (sym, symbols))

    print("Total:", len(file) - file.count(' '))
