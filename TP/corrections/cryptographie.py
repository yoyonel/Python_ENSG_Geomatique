# -*- coding:utf8 -*-

def table_vigenere():
    """
    Méthode retournant une table de Vigenère.
    """
    t = []
    for j in range(26):
        t.append([])
        for i in range(0, 26):
            val = (i+j) % 26
            lettre = chr(97+val)
            t[j].append(lettre)
    return t



def lettre_codee(lettre, lettre_cle, table_vigenere):
    """
    Méthode cryptant une lettre à l'aide de la table de Vigenère et de la
    lettre clé.
    """
    num_lettre = ord(lettre) - 97
    num_cle = ord(lettre_cle) - 97
    return table_vigenere[num_cle][num_lettre]



def lettre_decodee(lettre_codee, lettre_cle, table_vigenere):
    """
    Méthode décryptant une lettre à l'aide de la table de Vigenère et de la
    lettre clé.
    """
    num_cle = ord(lettre_cle) - 97
    num_lettre = table_vigenere[num_cle].index(lettre_codee) + 97
    return chr(num_lettre)



def cryptage_vigenegre(message, cle, tab, mode):
    """
    Fonction effectuant le cryptage/décryptage d'un message selon la méthode de
    Vigenère.

    La méthode de Vigenère est une méthode de chiffrement poly-alphabétique
    (ie. une lettre d'arrivée peut correspondre à plusieurs lettres de départ
    en fonction de sa position).
    Le paramètre mode est utiliser pour indiquer s'il faut utiliser la fonction
    pour crypter (True) ou décrypter (False) un message.

    :param message: texte à crypter
    :type message: string
    :param cle: clé de chiffrement
    :param cle: string
    :param tab: table de Vigenère
    :type tab: string[][]
    :param mode: True=>chiffrage / False=>déchiffrage
    :type mode: booleen
    :return: texte crypté
    :returntype: string
    """
    message_ok = ""
    i = 0  # compteur pour avancer dans la clé
    n = len(cle)

    for lettre in message:
        if 97 <= ord(lettre) <= 123:
            # il s'agit d'une lettre, on la code
            if mode:
                # cryptage
                lettre_ok = lettre_codee(lettre, cle[i], tab)
            else:
                # decryptage
                lettre_ok = lettre_decodee(lettre, cle[i], tab)
            i = (i + 1) % n
        else:
            # il ne s'agit pas d'une lettre
            lettre_ok = lettre

        # dans tous le cas, on ajoute au message_ok
        message_ok += lettre_ok

    return message_ok



def nettoyage_cle(cle):
    """
    Fonction nettoyant une clé pour un cryptage par substitution.

    La clé ne doit pas contenir de caractère en double. Nous ne conservons
    que la première occurence de chaque caractère. Les espaces et signes de
    ponctuation sont également supprimés.
    Par practicité, la clé normalisée est retournée sous forme de liste.

    :param cle: clé de chiffrement
    :type cle: string
    :return: clé normalisée
    :returntype: string

    :Example:
    >>> nettoyage_cle("ensg geomatique")
    ensgomatiqu
    """
    cle_ok = ""
    for lettre in cle:
        if ord(lettre) in range(97, 123) and lettre not in cle_ok:
            # c'est une lettre et elle n'est pas déjà dans la clé normalisée
            cle_ok += lettre
    return cle_ok


def cryptage_substitution(message, cle, mode):
    """
    Fonction permettant de crypter/decrypter une chaine de caractères en
    utilisant un algorithme de substitution.

    Le message en entrée est crypté à l'aide de la clé également fournie.
    L'algorithme utilisé consiste à remplacer dans le message, chaque
    caractère de la clé par le caractère suivant.
    Pour que le cryptage soit réversible, la clé ne peut pas contenir deux
    fois le même caractère. L'algorithme commence donc par nettoyer la clé
    des lettres en double.

    :param message: texte à crypter
    :type message: string
    :param cle: clé de chiffrement
    :param cle: string
    :param mode: True=>chiffrage / False=>déchiffrage
    :type mode: booleen
    :return: texte crypté
    :returntype: string

    :Example:
    >>> crypter("Message à crypter", "cle", True)
    Mcssagc à lryptcr
    """
    # Préparation de la clé : on supprime les caractères en double
    cle_ok = nettoyage_cle(cle)

    # Cryptage
    message_ok = "" # message crypté initialisé par une chaîne vide
    for lettre in message:
        if lettre in cle_ok:
            # On remplace la lettre par la suivante de la clé
            pos = cle_ok.index(lettre) # indice de la lettre dans la clé
            if mode:
                pos_ok = (pos + 1) % len(cle_ok) # indice de la lettre de remplacement dans la clé
            else:
                pos_ok = (pos - 1) % len(cle_ok) # indice de la lettre de remplacement dans la clé
            lettre_ok = cle_ok[pos_ok]

        else:
            # On conserve la lettre d'origine
            lettre_ok = lettre
        message_ok += lettre_ok

    return message_ok



def cryptage_cesar(message, decalage, mode):
    """
    Fonction permettant de crypter/décrypter une chaîne de caractère en
    utilisant la méthode de César.

    La méthode de césar consiste à appliquer un décalage constant aux caractères
    du message à crypter.
    Le paramètre mode est utiliser pour indiquer s'il faut utiliser la fonction
    pour crypter (True) ou décrypter (False) un message.

    :param message: message à chiffrer
    :type message: string
    :param decalage: décalage à appliquer
    :type decalage: int
    :param mode: True=>chiffrage / False=>déchiffrage
    :type mode: booleen
    :return: clé normalisée
    :returntype: string

    :Example:
    >>> cryptage_cesar("ensg", 5, True)
    jsxl
    """
    message_ok = ""
    for lettre in message:
        if 97 <= ord(lettre) <= 123:
            # il s'agit d'une lettre, on la décale
            code = ord(lettre)
            if mode:
                # cryptage
                code += decalage
            else:
                # décryptage
                code -= decalage
            # on s'assure que le code correspond toujours à un caractère
            code = 97 + (code - 97) % 26
            # lettre correspondante
            lettre_ok = chr(code)

        else:
            # il ne s'agit pas d'une lettre
            lettre_ok = lettre

        # dans tous les cas, on ajoute la caractère au message code
        message_ok += lettre_ok

    return message_ok



def analyse_frequentielle(texte):
    dico = {}
    dico.clear()
    for lettre in texte:
        if 97 <= ord(lettre) <= 123:
            # Il s'agit d'une lettre
            if lettre in dico.keys():
                # La lettre a deja  été rencontrée, on ajoute 1
                dico[lettre] += 1
            else:
                # La lettre n'a jamais été rencontrée, on initialise à 1
                dico[lettre] = 1
    return dico


def cassage_code(message_code, dico_freq):
    lettres_frequentes = [cle for cle,valeur in dico.items() if valeur == max(dico.values())]
    for lettre in lettres_frequentes:
        decalage = ord(lettre) - ord('e')
        message_ok = cryptage_cesar(message_code, decalage, False)
        print(message_ok)



if __name__ == "__main__":
    message = "l'informatique c'est de la balle!"

    message_code = cryptage_cesar(message, 4, True)
    print(message_code)

    cle = "ensg"
    tab = table_vigenere()
    message_code2 = cryptage_vigenegre(message, cle, tab, True)
    print(message_code2)

    cle = "ensg geomatique"
    cle_ok = nettoyage_cle(cle)
    message_code3 = cryptage_substitution(message, cle, True)
    print(message_code3)

    a = "p'vflseegxviai p'wyx qw re osrpr. gt c ssox qwy xemiw cjgxviaif egmf xgyg soqrj rif egxuéegxviaif."
    b = "r'otluxsgzowak i'kyz jk rg hgrrk. ut e lgoz jky zxaiy vxgzowaky sgoy lgaz goskx rky sgznksgzowaky."
    c = "l'qsfmratiquen c'ngi dn lt btlln. ms y cmdn dng irecg prtiqueng atqg ftei tqanr lng atihéatiqueng."
    dico = analyse_frequentielle(b)
    print(dico)
    cassage_code(b, dico)
