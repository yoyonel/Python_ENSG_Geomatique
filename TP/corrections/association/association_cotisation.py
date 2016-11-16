from association.association_log import log

log_nom_fichier = "association.log"


# Q 3.8-9-10
def calculCotisation(dico_act, liste_act):
    """
    Calcul de la cotisation du par un adhérent
    en fonction des activités auxquelles il est inscrit.

    Usage
    -----
    calculCotisation(dico_act dict, liste_act str[]) -> cotisation int

    Tests
    -----
    >>> calculCotisation({'Flute': 50, 'Piano': 155, 'Theatre': 10}, ['Flute', 'Theatre'])
    60

    >>> calculCotisation({'Piano': 155, 'Flute': 50, 'Danse': 200, 'Theatre': 10}, ['Danse', 'Theatre', 'Flute', 'Piano'])
    379.5

    """
    cotisation = 0
    liste_cotis = []
    activite = None

    try:
        if len(liste_act) < 3:
            # S'il y a moins de 3 activités, il n'y a pas de réduction à appliquer
            for activite in liste_act:
                cotisation += dico_act[activite]
        else:
            # 3 activités ou plus : on applique 10% de réduction au activités les plus chères
            for activite in liste_act:
                liste_cotis.append(dico_act[activite])

            # on trie la liste des cotisations (selon le prix)
            liste_cotis.sort()

            for i in range(0, 2):
                # Plein tarif pour les 2 premières activités
                cotisation += liste_cotis[i]
            for i in range(2, len(liste_cotis)):
                # Réduction de 10% pour les activités suivantes.
                cotisation += liste_cotis[i] * 0.9
    except KeyError:
        # print("La clé {} n'est pas présente dans le dictionnaire des activités/cotisations.".format(activite))
        log(log_nom_fichier, 'ERROR',
            "La clé {} n'est pas présente dans le dictionnaire des activités/cotisations.".format(activite))

    return cotisation


def appliquerReduction(prix, reduction):
    """

    :param cotisation:
    :param reduction: en pourcent
    :return:

    :Example:
    >>> appliquerReduction(200, 10)
    180.0
    """
    return prix * (1.0 - reduction/100.0)


def calculCotisation_v2(dico_act, liste_act, reduction=10):
    """
    Calcul de la cotisation du par un adhérent
    en fonction des activités auxquelles il est inscrit.

    Usage
    -----
    calculCotisation_v2(dico_act dict, liste_act str[]) -> cotisation int

    Tests
    -----
    >>> calculCotisation_v2({'Flute': 50, 'Piano': 155, 'Theatre': 10}, ['Flute', 'Theatre'])
    60

    >>> calculCotisation_v2({'Piano': 155, 'Flute': 50, 'Danse': 200, 'Theatre': 10}, ['Danse', 'Theatre', 'Flute', 'Piano'])
    379.5

    """
    # LOG
    log(log_nom_fichier, 'INFO',
        "calculCotisation_v2({}, {}, {})".format(dico_act, liste_act, reduction))

    cotisation = 0
    liste_cotis = []
    try:
        for activite in liste_act:
            liste_cotis.append(dico_act[activite])

        # 3 activités ou plus
        if len(liste_act) >= 3:
            # on trie la liste des cotisations (selon le prix)
            liste_cotis.sort()

            # Pourcentage de reduction appliquée à partir de la 3ème activité
            # On itère à partir de la 3ème activité jusqu'à la fin de la liste des activités
            for cotis_act in liste_cotis[2:]:
                # On met à jour la cotisation en prenant en compte les réductions
                cotisation += appliquerReduction(cotis_act, reduction)

        # Plein tarifs sur les 2 premières activités
        cotisation += sum(liste_cotis[:2])

        # LOG
        log(log_nom_fichier, 'INFO',
            "cotisation calculée = {}".format(cotisation))
    except KeyError:
        # print("La clé {} n'est pas présente dans le dictionnaire des activités/cotisations.".format(activite))
        # LOG
        log(log_nom_fichier, 'ERROR',
            "La clé {} n'est pas présente dans le dictionnaire des activités/cotisations.".format(activite))

    return cotisation
