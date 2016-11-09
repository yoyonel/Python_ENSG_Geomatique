# -*- coding: utf-8 -*-

"""
Jeu de mastermind en python.
"""

from random import randint, sample
from copy import deepcopy
import numpy as np
from itertools import groupby, compress
from collections import defaultdict
import operator
from operator import itemgetter
import multiprocessing


codesCouleurs = {"R": 0, "B": 1, "J": 2, "V": 3, "N": 4, "M": 5, "F": 6, "O": 7}
couleursCodes = {0: "R", 1: "B", 2: "J", 3: "V", 4: "N", 5: "M", 6: "F", 7: "O"}
nomsCouleurs = {"R": "Rouge", "B": "Bleu", "J": "Jaune", "V": "Vert", "N": "Noir", "M": "Marron", "F": "Fushia",
                "O": "Orange"}


def verification(sol, prop):
    """
    Fonction de vérification d'une combinaison.

    Retourne le nombre de pions biens placés et le nombre de pions présents
    dans la solution mais mal placés.

    Usage
    -----
    verification(int[] sol, int[] prop)


    Tests
    -----
    >>> verification([1, 4, 2, 1], [1, 2, 5, 4])
    (1, 2)

    >>> verification([1, 1, 2, 2], [1, 2, 1, 1])
    (1, 2)

    """
    nb_bien = 0  # nombre de pions bien placés
    nb_mal = 0  # nombre de pions présents mais à la mauvaise place
    n = len(sol)  # taille de la combinaison

    # Détection des couleurs bien placées
    i = 0
    while i < n:
        if sol[i] == prop[i]:
            # La couleur est bien placée
            nb_bien += 1
            # On modifie les combinaisons pour éviter compter 2 fois les doubles
            sol[i] = "x"
            prop[i] = "y"
        i += 1

    # Détection des couleurs mal placées
    i = 0
    while i < n:
        j = 0
        while j < n:
            if sol[i] == prop[j]:
                # La couleur est présente dans la solution mais mal positionnnée
                nb_mal += 1
                # Modification pour éviter les erreurs dus aux doubles
                sol[i] = "x"
                prop[j] = "y"
                break
            j += 1
        i += 1

    return nb_bien, nb_mal


def verification_v2(sol, prop):
    """
    Idem que verification mais en programmation fonctionnelle (avec groupby et tri)

    Usage
    -----
    verification(int[] sol, int[] prop)


    Tests
    -----
    >>> verification_v2([1, 4, 2, 1], [1, 2, 5, 4]) == verification([1, 4, 2, 1], [1, 2, 5, 4])
    True

    >>> verification_v2([1, 1, 2, 2], [1, 2, 1, 1]) == verification([1, 1, 2, 2], [1, 2, 1, 1])
    True

    """
    # Détection des couleurs bien placées
    nb_bien = sum((np.array(sol) - np.array(prop)) == 0)

    # Détection des couleurs mal placées
    nb_mal = 0
    dicts_gp_sol_prop = map(
        lambda gb: defaultdict(int, {k: len(list(v)) for k, v in gb}),
        map(
            groupby,
            map(
                sorted,
                zip(
                    *filter(
                        lambda sol_prop: sol_prop[0] is not sol_prop[1],
                        zip(sol, prop)
                    )
                )
            )
        )
    )
    if dicts_gp_sol_prop:
        dict_gb_sol, dict_gb_prop = dicts_gp_sol_prop
        nb_mal = sum(
            map(
                lambda tup_gb_sol: min(tup_gb_sol[1], dict_gb_sol[tup_gb_sol[0]]),
                dict_gb_prop.items()
            )
        )

    return nb_bien, nb_mal


def verification_v3(sol, prop, nb_couleurs):
    """
    Idem que verification mais en programmation fonctionnelle (avec histogram)

    Usage
    -----
    verification(int[] sol, int[] prop)


    Tests
    -----
    >>> verification_v3([1, 4, 2, 1], [1, 2, 5, 4], 5) == verification([1, 4, 2, 1], [1, 2, 5, 4])
    True

    >>> verification_v3([1, 1, 2, 2], [1, 2, 1, 1], 3) == verification([1, 1, 2, 2], [1, 2, 1, 1])
    True

    """
    np_sol, np_prop = np.array(sol), np.array(prop)
    # Détection des couleurs bien placées
    bools_for_compress = np_sol != np_prop

    # Détection des couleurs bien placées
    nb_bien = len(np_sol) - sum(bools_for_compress)

    # Détection des couleurs mal placées
    nb_mal = sum(
        map(
            min,
            zip(
                *map(
                    lambda np_l: np.histogram(np_l, bins=range(nb_couleurs + 1))[0],
                    map(
                        lambda l: tuple(compress(l, bools_for_compress)),
                        [np_sol, np_prop]
                    )
                )
            )
        )
    )

    return nb_bien, nb_mal


def verification_v4(sol, prop, nb_couleurs):
    """
    Idem que verification mais en programmation fonctionnelle (avec histogram "simple")

    Usage
    -----
    verification(int[] sol, int[] prop)


    Tests
    -----
    >>> verification_v4([1, 4, 2, 1], [1, 2, 5, 4], 5) == verification([1, 4, 2, 1], [1, 2, 5, 4])
    True

    >>> verification_v4([1, 1, 2, 2], [1, 2, 1, 1], 3) == verification([1, 1, 2, 2], [1, 2, 1, 1])
    True

    """
    # [linear]
    np_sol, np_prop = np.array(sol), np.array(prop)
    # Détection des couleurs bien placées
    bools_for_compress = np_sol != np_prop

    # [linear]
    # Détection des couleurs bien placées
    nb_bien = len(np_sol) - sum(bools_for_compress)

    # Détection des couleurs mal placées
    # [linear]
    histo_sol = [0] * (nb_couleurs+1)
    histo_prop = [0] * (nb_couleurs+1)
    # ps: random access pour update histo_[sol|prop]
    # => i varie aléatoirement
    # [linear]
    for i in compress(np_sol, bools_for_compress):
        histo_sol[i] += 1
    for i in compress(np_prop, bools_for_compress):
        histo_prop[i] += 1

    # [linear]
    #
    nb_mal = sum(
        map(
            min,
            zip(histo_sol, histo_prop)
        )
    )

    return nb_bien, nb_mal


def update_histo(args):
    """

    :param args:
    :return:
    """
    for i in list(compress(args[1], args[0])):
        args[2][i] += 1


def verification_v4b(sol, prop, list_empty_for_histo):
    """
    Idem que verification mais en programmation fonctionnelle (avec histogram "simple")

    Usage
    -----
    verification(int[] sol, int[] prop)


    Tests
    -----
    >>> list_empty_for_histo = np.array([0] * (5+1))
    >>> verification_v4b([1, 4, 2, 1], [1, 2, 5, 4], list_empty_for_histo) == verification([1, 4, 2, 1], [1, 2, 5, 4])
    True

    >>> verification_v4b([1, 1, 2, 2], [1, 2, 1, 1], list_empty_for_histo) == verification([1, 1, 2, 2], [1, 2, 1, 1])
    True

    """
    np_sol, np_prop = np.array(sol), np.array(prop)

    nb_jobs = 4

    # Split des entrees
    np_sols = np.array_split(np_sol, nb_jobs)
    np_props = np.array_split(np_prop, nb_jobs)

    # Il faut creer une shared memory pour les resultats
    # url: https://pythonhosted.org/joblib/parallel.html
    histo_sol = [deepcopy(list_empty_for_histo) for _ in range(nb_jobs)]
    histo_prop = [deepcopy(list_empty_for_histo) for _ in range(nb_jobs)]

    # Détection des couleurs bien placées
    bools_for_compress = map(lambda tup: operator.ne(*tup), zip(np_sols, np_props))
    nb_bien = np_sol.size - sum(map(lambda arr_bool: sum(arr_bool), bools_for_compress))

    # Détection des couleurs mal placées
    zip_sols_compress_histo = zip(bools_for_compress, np_sols, histo_sol)
    zip_props_compress_histo = zip(bools_for_compress, np_props, histo_prop)

    # [linear]
    map(update_histo, zip_sols_compress_histo)
    map(update_histo, zip_props_compress_histo)

    #
    histo_sol = reduce(operator.add, map(itemgetter(2), zip_sols_compress_histo))
    histo_prop = reduce(operator.add, map(itemgetter(2), zip_props_compress_histo))

    #
    nb_mal = sum(map(min, zip(histo_sol, histo_prop)))

    return nb_bien, nb_mal


def copie(liste):
    """
    Fonction de copie profonde d'une liste
    """
    copie = []
    i = 0
    while i < len(liste):
        copie.append(liste[i])
        i += 1
    return copie


def deep_copy(liste):
    """
    Fonction de copie profonde d'une liste

    :param liste:
    :return:

    url: https://docs.python.org/2/library/copy.html
    """
    return deepcopy(list)


def tirage_aleatoire(nb_pions, nb_couleurs, double=True):
    """
    Fonction de tirage alétoire de couleurs. Par défaut les tirages de couleur
    en double sont autorisés.

    :param nb_pions:
    :param nb_couleurs:
    :param double:
    :return:
    """
    combi = []

    i = 0
    while i < nb_pions:
        c = randint(0, nb_couleurs)
        while c in combi and not double:
            c = randint(0, nb_couleurs)
        combi.append(c)
        i += 1

    return combi


def tirage_aleatoire_v2(nb_pions, nb_couleurs, double=True):
    """
    Fonction de tirage alétoire de couleurs. Par défaut les tirages de couleur
    en double sont autorisés.

    :param nb_pions:
    :param nb_couleurs:
    :param double:
    :return:

    url: https://docs.python.org/2/library/random.html
    """
    return [randint(0, nb_couleurs - 1) for _ in range(nb_pions)] if double else sample(range(nb_couleurs), nb_pions)


def affiche_indications(nb_places, nb_couleurs, prop):
    """
    Fonction permettant d'afficher les indications données au joueur (nombre
    bien placés, nom mal placés, rappel de la proposition

    :param nb_places:
    :param nb_couleurs:
    :param prop:
    :return:
    """
    nb_pions = len(prop)

    msg = ""

    for i in range(nb_pions - nb_couleurs):
        msg += "   "

    for i in range(nb_couleurs):
        msg += " * "

    msg += " "

    for c in prop:
        msg += couleursCodes[c]

    msg += " "

    for i in range(nb_places):
        msg += " * "

    print(msg)


def saisie(nb_pions):
    """
    Fonction permettant la saisie d'une combinaison par l'utilisateur
    """
    saisie_proposition = input("Votre proposition ? ").upper()

    # On vérifie que la proposition comporte le bon nombre d'entrées
    if len(saisie_proposition) != nb_pions:
        print("La proposition doit contenir " + str(nb_pions) + " couleurs !")
        return None

    # On vérifie que les entrées sont bien des couleurs admises
    for c in saisie_proposition:
        if c not in codesCouleurs.keys():
            print(str(c) + " : valeur incorrect. La proposition doit contenir uniquement des couleurs de " + str(
                codesCouleurs.keys()))
            return None

    # La saisie est correcte : on transforme en liste d'entiers.
    prop = []
    for c in saisie_proposition:
        prop.append(codesCouleurs[c])

    return prop


def jouer(nb_pions, nb_coups, nb_couleurs=8, double=True):
    """
    Méthode permettant de jouer.

    :param nb_pions:
    :param nb_coups:
    :param nb_couleurs:
    :param double:
    :return:
    """
    # Préparation
    # sol = tirage(nb_pions, nb_couleurs, double)  # combinaison à découvrir
    sol = tirage_aleatoire(nb_pions, nb_couleurs, double)  # combinaison à découvrir
    print("Tirage de " + str(nb_pions) + " couleurs effectué.")
    print("Vous avez " + str(nb_coups) + " coups pour découvrir la solution.")

    # Début de la partie
    n = 0
    trouve = False
    while n < nb_coups and not trouve:
        # Tant que l'on a pas atteind le nombre de coups max ou touvé la solution, on continue
        prop = saisie(nb_pions)  # Saisie d'une proposition
        while prop is None:
            prop = saisie(nb_pions)

        # Vérification de la proposition par rapport à la solution
        copie_sol = copie(sol)
        copie_prop = copie(prop)

        nb_bien, nb_mal = verification(copie_sol, copie_prop)

        # afficheIndications(nb_pions, nb_bien, nb_mal, prop)
        affiche_indications(nb_bien, nb_pions, prop)

        # if (nb_places == nb_pions):
        if nb_bien == nb_pions:
            # si tous les pions sont bien placés, on a trouvé la solution
            trouve = True

        n += 1

    # Fin de la partie
    if trouve:
        print("Bravo ! Vous avez trouvé la solution en " + str(n) + "coups")
    else:
        msg = ""
        for c in sol:
            msg += couleursCodes[c]
        print("Perdu ! La solution était : " + msg)


if __name__ == "__main__":
    jouer(2, 12, 2, False)