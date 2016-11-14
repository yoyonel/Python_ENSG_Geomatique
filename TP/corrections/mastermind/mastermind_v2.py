# -*- coding: utf8 -*-
# import numpy as np
# from itertools import groupby, compress
from collections import Counter
# from collections import defaultdict
# from copy import deepcopy
# from operator import itemgetter

from mastermind import *


def verification_v2(sol, prop):
    """
    Idem que verification mais en programmation fonctionnelle (avec groupby et
    tri)

    :param sol: solution, liste de référence
    :param prop: proposition, liste à comparer à la référence
    :return: nb bien placées, nb couleur présente mais mal placée

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


def verification_v2b(sol, prop):
    """
    Idem que verification mais en programmation fonctionnelle (avec groupby et
    tri)

    :param sol: solution, liste de référence
    :param prop: proposition, liste à comparer à la référence
    :return: nb bien placées, nb couleur présente mais mal placée

    Tests
    -----
    >>> verification_v2b([1, 4, 2, 1], [1, 2, 5, 4]) == verification([1, 4, 2, 1], [1, 2, 5, 4])
    True
    >>> verification_v2b([1, 1, 2, 2], [1, 2, 1, 1]) == verification([1, 1, 2, 2], [1, 2, 1, 1])
    True
    """
    zip_sol_prop = zip(sol, prop)

    # Détection des couleurs bien placées
    nb_bien = len([1 for s, p in zip_sol_prop if s == p])

    # Détection des couleurs mal placées
    s1 = Counter([s for s, p in zip_sol_prop if s != p])
    p1 = Counter([p for s, p in zip_sol_prop if s != p])
    cle_communes = set(s1.keys()) & set(p1.keys())
    nb_couleurs = sum([min(s1[x], p1[x]) for x in cle_communes])

    return nb_bien, nb_couleurs


def verification_v2c(sol, prop):
    """
    Idem que verification mais en programmation fonctionnelle (avec groupby et
    tri)

    :param sol: solution, liste de référence
    :param prop: proposition, liste à comparer à la référence
    :return: nb bien placées, nb couleur présente mais mal placée

    Tests
    -----
    >>> verification_v2c([1, 4, 2, 1], [1, 2, 5, 4]) == verification([1, 4, 2, 1], [1, 2, 5, 4])
    True
    >>> verification_v2c([1, 1, 2, 2], [1, 2, 1, 1]) == verification([1, 1, 2, 2], [1, 2, 1, 1])
    True
    """
    # on mutualise le zip des solutions propositions
    zip_sol_prop = zip(sol, prop)

    # Détection des couleurs bien placées
    nb_bien = sum([s == p for s, p in zip_sol_prop])

    # Détection des couleurs mal placées
    # on mutualise le test s!=p pour s et p [MAP]
    zip_filter_sol_prop = [(s, p) for s, p in zip_sol_prop if s != p]
    # on dezip les listes [REDUCE]
    # url: http://stackoverflow.com/questions/19339/a-transpose-unzip-function-in-python-inverse-of-zip
    s1, p1 = zip(*zip_filter_sol_prop)
    # Application du 'Counter' sur s1, p1 [MAP]
    s1, p1 = map(Counter, (s1, p1))
    # On calcul le nombre de couleurs présentes mais mal placées [REDUCE]
    nb_couleurs = sum([min(s1[s1_key], p1[s1_key]) for s1_key in s1.iterkeys() if s1_key in p1])

    return nb_bien, nb_couleurs


def verification_v3(sol, prop):
    """
    Idem que verification mais en programmation fonctionnelle (avec histogram)

    :param sol: solution, liste de référence
    :param prop: proposition, liste à comparer à la référence
    :return: nb bien placées, nb couleur présente mais mal placée.

    Tests
    -----
    >>> verification_v3([1, 4, 2, 1], [1, 2, 5, 4]) == verification([1, 4, 2, 1], [1, 2, 5, 4])
    True
    >>> verification_v3([1, 1, 2, 2], [1, 2, 1, 1]) == verification([1, 1, 2, 2], [1, 2, 1, 1])
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
                    lambda np_l: np.histogram(np_l, bins=range(8 + 1))[0],
                    map(
                        lambda l: tuple(compress(l, bools_for_compress)),
                        [np_sol, np_prop]
                    )
                )
            )
        )
    )

    return nb_bien, nb_mal


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


if __name__ == '__main__':
    sol = [1, 4, 2, 1]
    prop = [1, 2, 5, 4]
    print(verification_v2b(sol, prop))
    sol = [1, 1, 2, 2]
    prop = [1, 2, 1, 1]
    print(verification_v2b(sol, prop))
    sol = [1, 1, 2, 2]
    prop = [1, 2, 1, 1]
    print(verification_v3(sol, prop))
