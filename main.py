#### Imports et définition des variables globales

import sys
sys.setrecursionlimit(1050)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
       en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    c = [s[0]]
    o = [1]

    for k in range(1, len(s)):
        if s[k] == s[k-1]:
            o[-1] += 1
        else:
            c.append(s[k])
            o.append(1)


    return list(zip(c,o))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de 
       caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    k = 0

    if s == "":
        return []

    for c in s:
        if c != s[0]:
            break
        k = k+1

    return [(s[0], k)] + artcode_r(s[k:])


#### Fonction principale


def main():

    print("Here is the iterative version :")
    for i in artcode_i('MMMMaaacXolloMM'):
        print(i)

    print("Here is the recursive version :")
    #for i in print(artcode_r('MMMMaaacXolloMM')):
    #    print(i)

    #print(artcode_r('M'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
