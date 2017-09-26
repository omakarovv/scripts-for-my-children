#!/usr/bin/env python3
# -*- coding: utf-8 -*-


### Count symbols in the text ###

def getAllLettersRus():
    for item in range(1072, 1104):
        yield unichr(item)

if __name__ == '__main__':
    with open("text.txt", "r") as f:
        file = f.read().decode('cp1251').lower()
        for rus in getAllLettersRus():
            alaphab = file.count(rus)
            print("%s - %d" % (rus, alaphab))

        for rus in [',', '.', '-', '!', '?', ':', ';']:
            alaphab = file.count(rus)
            print("%s - %d" % (rus, alaphab))
        print(len(file) - file.count(' '))

### Thank you Alexander!!! ###
