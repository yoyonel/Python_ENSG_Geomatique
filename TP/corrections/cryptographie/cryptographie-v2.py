# -*- coding: utf8 -*-
import collections
from cryptographie import est_une_lettre, lettre_codee, lettre_decodee


def nettoyage_cle(cle):
    """
    Fonction nettoyant une clé pour un cryptage par substitution.

    La clé ne doit pas contenir de caractère en double. Nous ne conservons
    que la première occurence de chaque caractère. Les espaces et signes de
    ponctuation sont également supprimés.

    :param cle: clé de chiffrement
    :return: clé normalisée

    :Example:
    >>> print(nettoyage_cle("ensg geomatique"))
    ensgomatiqu
    """
    cle_ok = "".join(
        collections.OrderedDict.fromkeys(
            filter(est_une_lettre, cle)
        ).keys()
    )
    return cle_ok


def table_vigenere():
    """
    Méthode retournant une table de Vigenère.
    """
    return [[chr(97 + (i + j) % 26) for i in range(26)] for j in range(26)]


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
    :param cle: clé de chiffrement
    :param tab: table de Vigenère
    :param mode: True=>chiffrage / False=>déchiffrage
    :return: texte crypté

    >>> cle = "ensg"
    >>> tv = table_vigenere()
    >>> print(cryptage_vigenegre("l'informatique c'est de la balle!", nettoyage_cle(cle), tv, True))
    p'vflseegxviai p'wyx qw re osrpr!
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
        message_ok += lettre_ok

    return message_ok
