#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Ces fonctions ne tiennent compte des caractères spéciaux

def majuscule(mot):
    tab1 = ['À', 'Â', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ï', 'Î', 'Ù']
    tab2 = ['à', 'â', 'ç', 'è', 'é', 'ê', 'ë', 'ï', 'î', 'ù']
    maj = ''
    for i in range(len(mot)):
        if 97 <= ord(mot[i]) <= 122:
            a = chr((ord(mot[i])-32))
            maj += a
        elif mot[i] in tab2:
            maj += tab1[tab2.index(mot[i])]



    return maj
def minuscule(mot):
    tab1 = ['À', 'Â', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ï', 'Î', 'Ù']
    tab2 = ['à', 'â', 'ç', 'è', 'é', 'ê', 'ë', 'ï', 'î', 'ù']
    min = ''
    for i in range(len(mot)):
        if 65 <= ord(mot[i]) <= 90:
            a = chr((ord(mot[i])+32))
            min += a
        elif mot[i] in tab1:
            min += tab2[tab1.index(mot[i])]
    return min

if __name__ == '__main__':
    mots = [
        'rïëz',
        'couäàrs',
        'voiturée',
        'oiseauè',
        'bonjouàr',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])
    print(mots)

    print(minuscule("BONJOURÉÀÈÖ"))


