#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Ces fonctions ne tiennent compte des caractères spéciaux
def majuscule(mot):
    maj = ''
    for i in range(len(mot)):
        if 97 <= ord(mot[i]) <= 122:
            a = chr((ord(mot[i])-32))
            maj += a
    return maj
def minuscule(mot):
    min = ''
    for i in range(len(mot)):
        if 65 <= ord(mot[i]) <= 90:
            a = chr((ord(mot[i])+32))
            min += a
    return min

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])
    print(mots)

    print(minuscule("BONJOUR"))


