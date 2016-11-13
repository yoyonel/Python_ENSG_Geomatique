# -*- coding:utf8 -*-
from operator import itemgetter
import collections


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


def table_vigenere_lc():
    """
    Méthode retournant une table de Vigenère.

    >>> table_vigenere_lc() == table_vigenere()
    True
    """
    return [[chr(97 + (i+j) % 26) for i in range(26)] for j in range(26)]


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


def accumulate(iterator, element_neutre=0):
    """
    """
    total = element_neutre
    for item in iterator:
        total += item
        yield total


def est_une_lettre(lettre):
        """
        """
        return 97 <= ord(lettre) <= 123


def cryptage_vigenegre_avec_lambdas(message, cle, tab, mode):
    """
    Pareil que 'cryptage_vigenegre' mais avec l'utilisation de lambda expression.

    >>> message = "l'informatique c'est de la balle!"    
    >>> cle = "ensg"
    >>> tab = table_vigenere()
    >>> cryptage_vigenegre(message, cle, tab, True) == cryptage_vigenegre_avec_lambdas(message, cle, tab, True)
    True
    """
    message_ok = ""
    i = 0  # compteur pour avancer dans la clé
    n = len(cle)

    list_func = [lambda args: (args[0], 0),
                 lambda args: (lettre_decodee(*args), 1),
                 lambda args: (lettre_codee(*args), 1)]

    for lettre in message:
        lettre_ok, incr_i = list_func[
            est_une_lettre(lettre) * (1 + mode)]((lettre, cle[i], tab))
        i = (i + incr_i) % n
        # print lettre, lettre_ok, i
        message_ok += lettre_ok

    return message_ok


def cryptage_vigenegre_avec_lc(message, cle, tab, mode):
    """
    Pareil que 'cryptage_vigenegre' mais avec l'utilisation de list comphreension.

    Version plus dure à lire mais intéressante dans la construction et les mécanismes d'itérations mise en place.
    
    Le drawback de cette méthode est le double calcul des lettres "valides" dans le message,
    1 fois pour le calcul des indices 'i' et sa progression, 
    et une seconde fois pour choisir quelle méthode on utilise pour traiter une lettre dans le message.
    
    Il y aurait une possibilité d'éviter ce doublon, en fusionnant les listes des indices 'i' avec un décalage pour
    comparer le current et le previous (une différence indiquerait qu'on est sur une lettre).
    J'ai l'impression que le cout de cette alternative est plus important que le cout du test 'est_une_lettre'.
    (ça serait à vérifier).

    >>> message = "l'informatique c'est de la balle!"    
    >>> cle = "ensg"
    >>> tab = table_vigenere()
    >>> cryptage_vigenegre(message, cle, tab, True) == cryptage_vigenegre_avec_lc(message, cle, tab, True)
    True
    >>> print(cryptage_vigenegre_avec_lc(message, cle, tab, True))
    p'vflseegxviai p'wyx qw re osrpr!
    """
    list_func = [lambda args: args[0],
                 lambda args: lettre_decodee(*args),
                 lambda args: lettre_codee(*args)
                 ]
    one_plus_mode = 1 + mode

    def choose_func(lettre):
        """

        :param lettre:
        :return:
        """
        return list_func[est_une_lettre(lettre) * one_plus_mode]

    n = len(cle)

    return "".join(
            map(
                lambda incr_lettre: choose_func(incr_lettre[1])(
                    (incr_lettre[1], cle[incr_lettre[0] % n], tab)
                ),
                zip(
                    accumulate([0] + map(est_une_lettre, message)[1:]),
                    message
                )
            )
    )


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
    'ensgomatiqu'
    """
    cle_ok = ""
    for lettre in cle:
        if ord(lettre) in range(97, 123) and lettre not in cle_ok:
            # c'est une lettre et elle n'est pas déjà dans la clé normalisée
            cle_ok += lettre
    return cle_ok


def nettoyage_cle_avec_dictionnaire_ordonnee(cle):
    """
    Pareil que 'nettoyage_cle'

    :Example:
    >>> nettoyage_cle_avec_dictionnaire_ordonnee("ensg geomatique") == nettoyage_cle("ensg geomatique")
    True
    """
    return "".join(
        collections.OrderedDict.fromkeys(
            filter(est_une_lettre, "ensg geomatique")
            ).keys()
        )


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
    >>> print cryptage_substitution("Message à crypter", "cle", True)
    Mcssagc à lryptcr
    """
    # Préparation de la clé : on supprime les caractères en double
    cle_ok = nettoyage_cle(cle)

    # Cryptage
    message_ok = ""  # message crypté initialisé par une chaîne vide
    for lettre in message:
        if lettre in cle_ok:
            # On remplace la lettre par la suivante de la clé
            pos = cle_ok.index(lettre)  # indice de la lettre dans la clé
            if mode:
                # indice de la lettre de remplacement dans la clé
                pos_ok = (pos + 1) % len(cle_ok)
            else:
                # indice de la lettre de remplacement dans la clé
                pos_ok = (pos - 1) % len(cle_ok)
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
    'jsxl'
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
    """

    :param texte:
    :return:
    """
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
    """

    :param message_code:
    :param dico_freq:
    :return:
    """
    max_freq = max(dico_freq.values())
    lettres_frequentes = [
        cle for cle, valeur in dico_freq.items() if valeur == max_freq]
    messages_ok = []
    for lettre in lettres_frequentes:
        decalage = ord(lettre) - ord('e')
        message_ok = cryptage_cesar(message_code, decalage, False)
        # print(message_ok)
        messages_ok.append(message_ok)
    return messages_ok


def cassage_code_avec_tri(message_code, dico_freq, nb_lettres_a_essayer=1):
    """

    >>> b = "r'otluxsgzowak i'kyz jk rg hgrrk. ut e lgoz jky zxaiy vxgzowaky sgoy lgaz goskx rky sgznksgzowaky."
    >>> dico = analyse_frequentielle(b)
    >>> cassage_code(b, dico) == cassage_code_avec_tri(b, dico, 2)
    True
    """
    list_items_from_dico_freq = dico_freq.items()
    list_items_from_dico_freq.sort(key=itemgetter(1), reverse=True)
    return map(
        lambda lettre: cryptage_cesar(message_code, ord(lettre) - ord('e'), False),
        map(itemgetter(0), list_items_from_dico_freq)[0:nb_lettres_a_essayer]
        )


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
    print cassage_code(b, dico)
